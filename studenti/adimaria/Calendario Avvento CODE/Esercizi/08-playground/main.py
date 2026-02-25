'''
Soluzione per Exercise 8: Playground
Goal: Connect closest 1000 pairs, then multiply sizes of 3 largest circuits.
'''

import math
from parser import parse_exercise

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.size[root_i] < self.size[root_j]:
                root_i, root_j = root_j, root_i
            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]
            return True
        return False

def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)

def main():
    points = parse_exercise("./demo.txt")
    n = len(points)
    
    # Calculate all pairwise distances
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            d = distance(points[i], points[j])
            edges.append((d, i, j))
    
    # Sort by distance
    edges.sort(key=lambda x: x[0])
    
    # Connect top K pairs
    # Note: Example says "After making the ten shortest connections...".
    # Problem prompt: "connect together the 1000 pairs of junction boxes which are closest together."
    # Since demo has only 20 points, 20*(19)/2 = 190 total pairs.
    # The example mentions "shortest 10 connections".
    # The full input will be larger, hence "1000".
    # For demo, I should adjust K to 10 to match the example logic?
    # Or should I stick to 1000? If I use 1000 on demo (190 pairs), it just connects everything.
    # The example output 40 is derived "After making the ten shortest connections".
    # I will adapt K based on input size for the sake of the demo check.
    # But usually valid logic should handle the hardcoded 1000.
    # If I run logic with 1000 on demo, it connects everything -> 1 component size 20.
    # But for verification I need to match 40.
    # I will switch K to 10 IF len(points) is small (like 20), else 1000.
    
    if n <= 20:
        K = 10
    else:
        K = 1000
        
    uf = UnionFind(n)
    count = 0
    for _, u, v in edges:
        if count >= K:
            break
        # Just "connect" them. 
        # "Since 162... is already connected... there is now a single circuit..."
        # We perform the union operation regardless of whether they are already in same component?
        # "The next two junction boxes are... Because these two... were already in the same circuit, nothing happens!"
        # This implies we iterate through the sorted list and TRY to connect.
        # But wait, "connect together the 1000 pairs...".
        # Does that mean we perform 1000 "add edge" operations?
        # Yes.
        # So we iterate top K edges, and Union them.
        uf.union(u, v)
        count += 1
        
    # Get component sizes
    # We need to find root for all to update path compression
    # and just collect sizes of roots.
    root_sizes = {}
    for i in range(n):
        r = uf.find(i)
        root_sizes[r] = uf.size[r]
        
    sizes = sorted(list(root_sizes.values()), reverse=True)
    
    # "Multiplying together the sizes of the three largest circuits"
    if len(sizes) >= 3:
        result = sizes[0] * sizes[1] * sizes[2]
    elif len(sizes) == 2: # Fallback just in case
        result = sizes[0] * sizes[1]
    else:
        result = sizes[0]
        
    print(f"Product of 3 largest: {result}")

if __name__ == "__main__":
    main()
