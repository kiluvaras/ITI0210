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


def read_map(map):
    start_row = 0
    start_col = 0
    width = 0
    height = 0

    for row in map:
        height += 1
        if "s" in row:
            start_row = height - 1
            start_col = row.index("s")
        if "D" in row:
            print(height - 1, ",", row.index("D"))
        width = len(row)

    print("We have a " + str(width) + "x" + str(height) + " sized maze.")
    #find_neighbours((start_row - 1, start_col), width, height)
    #find_neighbours(lava_map1, (6, 10), width, height)
    #print("Jou - " + map[14][16])


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

    #print(move_names)
    #print("Possible moves: " + str(possible_moves))
    #print("row: " + str(row) + "\ncolumn: " + str(col))
    return possible_moves

# -----------------------------------------------------------
def minu_otsing(kaart):
    start_row = 0
    start_col = 0
    width = 0
    height = 0
    diamond = ()
    path = []
    map_with_path = list(kaart)

    for row in kaart:
        height += 1
        if "s" in row:
            start_row = height - 1
            start_col = row.index("s")
        width = len(row)

    start = (start_row, start_col)

    # start (algolek) on näiteks tuple kujul (x, y)

    frontier = Queue()
    frontier.put(start)
    came_from = {}
    came_from[start] = None

    while not frontier.empty():
        current = frontier.get()
        if kaart[current[0]][current[1]] == "D":
            print("Found the diamond!")
            diamond = current
            print(diamond)
            while current != start:
                path.append(current)
                temp = list(map_with_path[current[0]])
                temp[current[1]] = "@"
                "".join(temp)
                map_with_path[current[0]] = temp
                #map_with_path[current[0]][current[1]] = "X"
                current = came_from[current]
            path.append(start)
            path.reverse()
            break

        # meid ei huvita kõik teed, seega peaks kontrollima, kas current on teemant.
        # Kui on, siis katkestame otsingu
        # (ja loomulikult jätame teemandi koordinaadid meelde)

        for next in find_neighbours(kaart, current, width, height):  # see osa tuleb suht palju ümber teha.
                                               # tuleb leida sobivad naaberruudud kaardilt
                                               # nagu ta meile ette on antud (ülal, all,
                                               # paremal ja vasakul olev ruut)
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current


    # Kui teemant on leitud, tuleb ka teekond rekonstrueerida
    # mis andmestruktuurina teekonda esitada, pole oluline,
    # aga loomulik viis oleks list
    print(path)
    #for row in map_with_path:
        #print(row)
        #print("\n")
    return path


if __name__ == '__main__':
    #read_map(lava_map1)
    minu_otsing(lava_map1)
