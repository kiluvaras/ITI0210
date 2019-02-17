from queue import Queue, PriorityQueue
import time

lava_map1 = [
    "      **               **      ",
    "     ***     D        ***      ",
    "     ***                       ",
    "                      *****    ",
    "           ****      ********  ",
    "           ***          *******",
    " **                      ******",
    "*****             ****     *** ",
    "*****              **          ",
    "***                            ",
    "              **         ******",
    "**            ***       *******",
    "***                      ***** ",
    "                               ",
    "                s              ",
]

lava_map2 = [
    "     **********************    ",
    "   *******   D    **********   ",
    "   *******                     ",
    " ****************    **********",
    "***********          ********  ",
    "            *******************",
    " ********    ******************",
    "********                   ****",
    "*****       ************       ",
    "***               *********    ",
    "*      ******      ************",
    "*****************       *******",
    "***      ****            ***** ",
    "                               ",
    "                s              ",
]

lava_map3 = [
    "     **********************    ",
    "   *******        **********   ",
    "   *******                     ",
    " ****************    **********",
    "***********          ********  ",
    "            *******************",
    " ********    ******************",
    "********                   ****",
    "*****       ************       ",
    "***               *********    ",
    "*      ******      ************",
    "*****************       *******",
    "***      ****            ***** ",
    "                               ",
    "D               s              ",
]


def find_neighbours(map, location, width, height):
    row = location[0]
    col = location[1]
    possible_moves = []
    move_names = []

    if row < 0 or row >= height or col < 0 or col >= width:
        return

    # NORTH
    if row - 1 >= 0 and map[row - 1][col] != "*":
        possible_moves.append((row - 1, col))
        move_names.append("north")
    # SOUTH
    if row + 1 < height and map[row + 1][col] != "*":
        possible_moves.append((row + 1, col))
        move_names.append("south")
    # WEST
    if col - 1 >= 0 and map[row][col - 1] != "*":
        possible_moves.append((row, col - 1))
        move_names.append("west")
    # EAST
    if col + 1 < width and map[row][col + 1] != "*":
        possible_moves.append((row, col + 1))
        move_names.append("east")

    return possible_moves


def bfs(map):
    start_row = 0
    start_col = 0
    width = 0
    height = 0
    diamond = ()
    path = []
    map_with_path = list(map)

    for row in map:
        height += 1
        if "s" in row:
            start_row = height - 1
            start_col = row.index("s")
        width = len(row)

    start = (start_row, start_col)

    frontier = Queue()
    frontier.put(start)
    came_from = {}
    came_from[start] = None

    while not frontier.empty():
        current = frontier.get()
        if map[current[0]][current[1]] == "D":
            print("Found the diamond!")
            diamond = current
            print(diamond)
            while current != start:
                path.append(current)
                temp = list(map_with_path[current[0]])
                if temp[current[1]] != "D":
                    temp[current[1]] = "@"
                    temp = "".join(temp)
                    map_with_path[current[0]] = temp
                current = came_from[current]
            path.append(start)
            path.reverse()
            break
        for next in find_neighbours(map, current, width, height):
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current

    print(path)
    for row in map_with_path:
        print(row)
    return path


def greedy(map, goal):
    begin = time.time()
    start_row = 0
    start_col = 0
    width = 0
    height = 0
    diamond = ()
    path = []
    map_with_path = list(map)

    for row in map:
        height += 1
        if "s" in row:
            start_row = height - 1
            start_col = row.index("s")
        width = len(row)

    start = (start_row, start_col)

    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {}
    came_from[start] = None

    while not frontier.empty():
        _, current = frontier.get()
        if map[current[0]][current[1]] == "D":
            print("Found the diamond!")
            diamond = current
            print(diamond)
            while current != start:
                path.append(current)
                temp = list(map_with_path[current[0]])
                if temp[current[1]] != "D":
                    temp[current[1]] = "@"
                    temp = "".join(temp)
                    map_with_path[current[0]] = temp
                current = came_from[current]
            path.append(start)
            path.reverse()
            break
        for next in find_neighbours(map, current, width, height):
            if next not in came_from:
                priority = h(next, goal)
                frontier.put((priority, next))
                came_from[next] = current
    end = time.time()
    print("Greedy time: " + str(end - begin))
    print("Greedy's steps taken: " + str(len(path)))
    #print(path)
    #for row in map_with_path:
     #   print(row)
    return path


def astar(map, goal):
    begin = time.time()
    start_row = 0
    start_col = 0
    width = 0
    height = 0
    diamond = ()
    path = []
    map_with_path = list(map)

    for row in map:
        height += 1
        if "s" in row:
            start_row = height - 1
            start_col = row.index("s")
        width = len(row)

    start = (start_row, start_col)
    cost_so_far = {}
    cost_so_far[start] = 0

    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {}
    came_from[start] = None

    while not frontier.empty():
        _, current = frontier.get()
        if map[current[0]][current[1]] == "D":
            print("Found the diamond!")
            diamond = current
            print(diamond)
            while current != start:
                path.append(current)
                temp = list(map_with_path[current[0]])
                if temp[current[1]] != "D":
                    temp[current[1]] = "@"
                    temp = "".join(temp)
                    map_with_path[current[0]] = temp
                current = came_from[current]
            path.append(start)
            path.reverse()
            break
        for next in find_neighbours(map, current, width, height):
            new_cost = cost_so_far[current] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + h(next, goal)  # g(n) + h(n)
                frontier.put((priority, next))
                came_from[next] = current
    end = time.time()
    print("A* time: " + str(end - begin))
    print("A* steps taken: " + str(len(path)))
    #print(path)
    #for row in map_with_path:
    #    print(row)
    return path


def h(node, goal):
    return abs(goal[0] - node[0]) + abs(goal[1] - node[1])


if __name__ == '__main__':
    with open("cave300x300") as f:
        map = [l.strip() for l in f.readlines() if len(l) > 1]

    print("- cave300x300 -")
    greedy(map, (295, 257))
    astar(map, (295, 257))

    with open("cave600x600") as f:
        map = [l.strip() for l in f.readlines() if len(l) > 1]

    print("\n\n- cave600x600 -")
    greedy(map, (598, 595))
    astar(map, (598, 595))

    with open("cave900x900") as f:
        map = [l.strip() for l in f.readlines() if len(l) > 1]

    print("\n\n- cave900x900 -")
    greedy(map, (898, 895))
    astar(map, (898, 895))
    # (1, 13)   D
    # (14, 16)  S
    #print(h((14, 16), (1, 13)))
