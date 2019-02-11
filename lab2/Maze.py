from queue import Queue

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


def my_search(map):
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
                    temp[current[1]] = "."
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


if __name__ == '__main__':
    my_search(lava_map1)
