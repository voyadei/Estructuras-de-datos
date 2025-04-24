#Suma de subconjuntos dando el valor de n
"""
                []
                /   \
               /     \
              /       \
             /         \
         [1]          []
         /\             /\
        /  \           /  \
       /    \         /    \
  [1,2]   [1]        [2]        []
   /\          /\      /\      /   \
  /  \        /  \    /  \     /   \
[1,2,3][1,2]  [1,3][1] [2,3][2] [3]  []
×        ✓    ×     ×   ×   ×   ✓    ×

"""

def subset_sum(n, subset=[], current_sum=0, start=1):
    if current_sum == n:
        print(subset)  
        return

    if current_sum > n:  
        return

    for i in range(start, n + 1):  
        subset_sum(n, subset + [i], current_sum + i, i + 1)  

if __name__ == "__main__":
    n =10
    subset_sum(n)
