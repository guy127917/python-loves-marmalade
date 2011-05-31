import random 
import maze
import time

def go(pos, d):
    xd, yd = maze.DIRECTIONS[d][0]
    return pos[0] + xd, pos[1] + yd

def generate_maze(width, height):
    m = maze.Maze(width, height)
    stack = [(random.randint(0, width-1), random.randint(0, height-1))]
    
    visited = set()
    for x in range(width):
        visited.add((x, -1))
        visited.add((x, height))
    for y in range(height):
        visited.add((-1, y))
        visited.add((width, y))

    while stack:
        pos = stack[-1]
        visited.add(pos)

        # choose a direction to a square we haven't yet visited
        possible_routes = [ d for d in maze.DIRECTIONS.keys()
            if go(pos, d) not in visited ]
        if not possible_routes:
            stack.pop()
            continue

        # choose a random available direction and use it
        direction = random.choice(possible_routes)
        m[pos].cut(direction)
        stack.append(go(pos, direction))
        
        print m
        #time.sleep(0.02)
    return m

if __name__ == "__main__":
    print generate_maze(15,15)
