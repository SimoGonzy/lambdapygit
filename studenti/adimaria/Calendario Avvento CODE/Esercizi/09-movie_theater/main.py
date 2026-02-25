'''
Soluzione per Exercise 9: Movie Theater
Goal: Largest rectangle area with red tile corners.
'''

from parser import parse_exercise

def main():
    red_tiles = parse_exercise("./demo.txt")
    
    max_area = 0
    
    n = len(red_tiles)
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = red_tiles[i]
            x2, y2 = red_tiles[j]
            
            # "The largest rectangle that uses red tiles for two of its opposite corners"
            # Area = width * height
            # Coordinates are discrete tiles?
            # Example: 2,5 and 9,7 -> area 24.
            # (9 - 2 + 1) * (7 - 5 + 1) ?
            # (7+1) = 8. (2+1) = 3. 8*3 = 24. Yes, inclusive.
            
            width = abs(x1 - x2) + 1
            height = abs(y1 - y2) + 1
            area = width * height
            
            if area > max_area:
                max_area = area
                
    print(f"Max area: {max_area}")

if __name__ == "__main__":
    main()
