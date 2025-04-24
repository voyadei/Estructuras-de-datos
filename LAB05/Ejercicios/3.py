import random
from collections import deque

def hot_potato(players, max_passes):
    if not players:
        return None

    queue = deque(players)

    while len(queue) > 1:
        passes = random.randint(1, max_passes)
        for _ in range(passes):
            queue.append(queue.popleft())  # Pass the hot potato
        queue.popleft()  # Eliminate the holder

    return queue[0]

if __name__ == "__main__":
    random.seed(42)  # For consistent test results

    players_list = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
    max_passes = 5 

    winner = hot_potato(players_list, max_passes)
    print("Winner of Hot Potato:", winner)

# Test Case 1: Minimal input
assert hot_potato(["Zoe"], 3) == "Zoe"

# Test Case 2: Two players, deterministic
random.seed(1)
assert hot_potato(["Anna", "Elsa"], 5) in ["Anna", "Elsa"]

# Test Case 3: Standard test with different players
random.seed(100)
assert hot_potato(["Tom", "Jerry", "Spike", "Tyke"], 4) in ["Tom", "Jerry", "Spike", "Tyke"]
