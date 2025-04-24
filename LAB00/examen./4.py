def filter_tuples_by_min_score(data, min_score):
    def recurse(index):
        if index == len(data):
            return []
        head = data[index]
        rest = recurse(index + 1)
        if head[1] >= min_score:
            return [head] + rest
        else:
            return rest

    return (True, recurse(0))

# Test
duplas = [("Ana", 15), ("Luis", 9), ("Carla", 18)]
print(filter_tuples_by_min_score(duplas, 10) == (True, 
[("Ana", 15), ("Carla", 18)]))
