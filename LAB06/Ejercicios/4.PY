class CircularQueue:
    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.capacity = capacity
        self.size = 0
        self.front = 0
        self.rear = 0

    def enqueue(self, item):
        if self.size == self.capacity:
            raise OverflowError("Queue is full")
        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise IndexError("Queue is empty")
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size


class Process:
    def __init__(self, pid, burst_time):
        self.pid = pid
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.waiting_time = 0
        self.turnaround_time = 0
        self.last_executed = 0


def round_robin_scheduling(processes, time_quantum):
    n = len(processes)
    queue = CircularQueue(n)
    current_time = 0

    for process in processes:
        queue.enqueue(process)

    while not queue.is_empty():
        process = queue.dequeue()
        process.waiting_time += current_time - process.last_executed

        execution_time = min(time_quantum, process.remaining_time)
        current_time += execution_time
        process.remaining_time -= execution_time
        process.last_executed = current_time

        if process.remaining_time > 0:
            queue.enqueue(process)
        else:
            process.turnaround_time = current_time

    result = {
        "average_waiting_time": sum(p.waiting_time for p in processes) / n,
        "average_turnaround_time": sum(p.turnaround_time for p in processes) / n,
        "processes": [(p.pid, p.waiting_time, p.turnaround_time) for p in processes]
    }
    return result


# Test
if __name__ == "__main__":
    processes = [Process("P1", 10), Process("P2", 5), Process("P3", 8)]
    time_quantum = 4
    result = round_robin_scheduling(processes, time_quantum)

    for pid, wait, turn in result["processes"]:
        print(f"Process {pid}: Waiting Time = {wait}, Turnaround Time = {turn}")
    print(f"Tiempo promedio de espera: {result['average_waiting_time']:.2f}")
    print(f"Tiempo promedio de respuesta: {result['average_turnaround_time']:.2f}")


# Test case 1: Procesos mixtos (tiempos variados)
processes1 = [Process("P1", 10), Process("P2", 5), Process("P3", 8)]
quantum1 = 4
result1 = round_robin_scheduling(processes1, quantum1)
print("Test Case 1 - Procesos Mixtos")
for pid, wait, turn in result1["processes"]:
    print(f"Process {pid}: Waiting Time = {wait}, Turnaround Time = {turn}")
print(f"Average Waiting Time: {result1['average_waiting_time']:.2f}")
print(f"Average Turnaround Time: {result1['average_turnaround_time']:.2f}\n")

# Test case 2: Procesos largos
processes2 = [Process("P1", 20), Process("P2", 25), Process("P3", 15)]
quantum2 = 6
result2 = round_robin_scheduling(processes2, quantum2)
print("Test Case 2 - Procesos Largos")
for pid, wait, turn in result2["processes"]:
    print(f"Process {pid}: Waiting Time = {wait}, Turnaround Time = {turn}")
print(f"Average Waiting Time: {result2['average_waiting_time']:.2f}")
print(f"Average Turnaround Time: {result2['average_turnaround_time']:.2f}\n")

# Test case 3: Procesos cortos (menores que el quantum)
processes3 = [Process("P1", 2), Process("P2", 1), Process("P3", 3)]
quantum3 = 5
result3 = round_robin_scheduling(processes3, quantum3)
print("Test Case 3 - Procesos Cortos")
for pid, wait, turn in result3["processes"]:
    print(f"Process {pid}: Waiting Time = {wait}, Turnaround Time = {turn}")
print(f"Average Waiting Time: {result3['average_waiting_time']:.2f}")
print(f"Average Turnaround Time: {result3['average_turnaround_time']:.2f}")
