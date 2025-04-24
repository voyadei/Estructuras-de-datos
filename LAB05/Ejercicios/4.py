from collections import deque

def sliding_window_maximum(nums, k):
    if not nums or k <= 0:
        return []

    max_values = []
    deq = deque()

    for i in range(len(nums)):
        # Remove indices out of the current window
        while deq and deq[0] < i - k + 1:
            deq.popleft()

        # Remove indices whose corresponding values are less than nums[i]
        while deq and nums[deq[-1]] < nums[i]:
            deq.pop()

        deq.append(i)

        # Append the current max to the result list
        if i >= k - 1:
            max_values.append(nums[deq[0]])
    
    
    return max_values

if __name__ == "__main__":
    array = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print("Sliding Window Maximums:", sliding_window_maximum(array, k))
