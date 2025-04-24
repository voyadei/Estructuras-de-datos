from collections import deque
import random

class Customer:
    def __init__(self, customer_id, item_count):
        self.customer_id = customer_id
        self.item_count = item_count

class CheckoutLane:
    def __init__(self, lane_id, processing_rate):
        self.lane_id = lane_id
        self.processing_rate = processing_rate
        self.queue = deque()  # Customers in line
        self.current_time = 0  # Current time for processing

    def add_customer(self, customer):
        self.queue.append(customer)

    def process_customer(self):
        if self.queue:
            customer = self.queue[0]
            processing_time = customer.item_count / self.processing_rate
            self.current_time += processing_time
            return customer, processing_time
        return None, 0

    def is_available(self):
        return not self.queue  # A lane is available if it has no customers

class Supermarket:
    def __init__(self, num_lanes, processing_rates):
        self.lanes = [CheckoutLane(i, rate) for i, rate in enumerate(processing_rates)]
        self.customers_processed = 0
        self.total_wait_time = 0

    def add_customer(self, customer):
        shortest_lane = min(self.lanes, key=lambda lane: len(lane.queue))
        shortest_lane.add_customer(customer)

    def simulate_checkout(self):
        for lane in self.lanes:
            customer, processing_time = lane.process_customer()
            if customer:
                self.customers_processed += 1
                self.total_wait_time += processing_time
                print(f"Customer {customer.customer_id} processed in lane {lane.lane_id} in {processing_time:.2f} time.")

    def get_average_wait_time(self):
        if self.customers_processed == 0:
            return 0
        return self.total_wait_time / self.customers_processed

    def get_throughput(self):
        return self.customers_processed

if __name__ == "__main__":
    # Example setup: 3 checkout lanes with different processing rates
    processing_rates = [1.5, 1.0, 2.0]  # Items per unit of time for each lane
    supermarket = Supermarket(num_lanes=3, processing_rates=processing_rates)

    # Simulate customers arriving
    customers = [Customer(i, random.randint(5, 15)) for i in range(10)]

    # Add customers to lanes
    for customer in customers:
        supermarket.add_customer(customer)

    # Simulate the checkout process
    supermarket.simulate_checkout()

    # Display statistics
    print(f"Average wait time: {supermarket.get_average_wait_time():.2f} time units")
    print(f"Total customers processed: {supermarket.get_throughput()}")
