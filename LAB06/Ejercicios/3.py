import random
class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0

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

class Vehicle:
    def __init__(self, arrival_time):
        self.arrival_time = arrival_time

class TrafficLight:
    def __init__(self, green_duration, red_duration):
        self.green_duration = green_duration
        self.red_duration = red_duration
        self.cycle_duration = green_duration + red_duration

    def is_green(self, time):
        return (time % self.cycle_duration) < self.green_duration

class Intersection:
    def __init__(self, green_duration, red_duration, lane_capacity):
        self.lanes = {
            'north_south': CircularQueue(lane_capacity),
            'east_west': CircularQueue(lane_capacity)
        }
        self.traffic_lights = {
            'north_south': TrafficLight(green_duration, red_duration),
            'east_west': TrafficLight(green_duration, red_duration)
        }
        self.current_direction = 'north_south'
        self.time = 0
        self.wait_times = []
        self.max_queue_lengths = {'north_south': 0, 'east_west': 0}

    def simulate(self, total_time, arrival_probability):
        for t in range(total_time):
            self.time = t
            # Vehicle arrivals
            for direction in self.lanes:
                if random.random() < arrival_probability:
                    vehicle = Vehicle(t)
                    try:
                        self.lanes[direction].enqueue(vehicle)
                    except OverflowError:
                        pass  # Queue is full; vehicle cannot enter

            # Update max queue lengths
            for direction in self.lanes:
                self.max_queue_lengths[direction] = max(
                    self.max_queue_lengths[direction], len(self.lanes[direction])
                )

            # Determine which direction has green light
            if self.traffic_lights[self.current_direction].is_green(t):
                # Allow one vehicle to pass if queue is not empty
                if not self.lanes[self.current_direction].is_empty():
                    vehicle = self.lanes[self.current_direction].dequeue()
                    wait_time = t - vehicle.arrival_time
                    self.wait_times.append(wait_time)
            else:
                # Switch direction if the current light is red
                self.current_direction = (
                    'east_west' if self.current_direction == 'north_south' else 'north_south'
                )

        # Calculate statistics
        average_wait = sum(self.wait_times) / len(self.wait_times) if self.wait_times else 0
        max_queue_ns = self.max_queue_lengths['north_south']
        max_queue_ew = self.max_queue_lengths['east_west']

        return average_wait, max_queue_ns, max_queue_ew

# Test the simulation

if __name__ == "__main__":
    random.seed(42)
    intersection = Intersection(green_duration=5, red_duration=5, lane_capacity=10)
    avg_wait, max_ns, max_ew = intersection.simulate(total_time=100, arrival_probability=0.3)
    print(f"Tiempo de espera promedio: {avg_wait:.2f}")
    print(f"Longitud máxima de la cola norte-sur: {max_ns}")
    print(f"Longitud máxima de la cola este-oeste: {max_ew}")


# Test case 1: Trafico moderado
intersection1 = Intersection(green_duration=5, red_duration=5, lane_capacity=10)
avg_wait1, max_ns1, max_ew1 = intersection1.simulate(total_time=100, arrival_probability=0.3)
print("Test Case 1 - Trafico Moderado")
print(f"Average Wait: {avg_wait1:.2f}, Max NS: {max_ns1}, Max EW: {max_ew1}\n")

# Test case 2: Mucho trafico
intersection2 = Intersection(green_duration=3, red_duration=3, lane_capacity=5)
avg_wait2, max_ns2, max_ew2 = intersection2.simulate(total_time=100, arrival_probability=0.7)
print("Test Case 2 - Mucho trafico")
print(f"Average Wait: {avg_wait2:.2f}, Max NS: {max_ns2}, Max EW: {max_ew2}\n")

# Test case 3: Poco trafico
intersection3 = Intersection(green_duration=6, red_duration=4, lane_capacity=15)
avg_wait3, max_ns3, max_ew3 = intersection3.simulate(total_time=100, arrival_probability=0.1)
print("Test Case 3 - Poco trafico")
print(f"Average Wait: {avg_wait3:.2f}, Max NS: {max_ns3}, Max EW: {max_ew3}")
