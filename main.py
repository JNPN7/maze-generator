from multiprocessing import reduction
import matplotlib.pyplot as plt
from random import randint
import argparse
INF = 999999

def graphics(edge_hor, edge_ver):
    tree_list = []
    for i, edges in enumerate(edge_hor):
        for j, edge in enumerate(edges):
            if edge == 1:
                tree_list.extend(([j+1, j+2], [height-i, height-i]))

    for i, edges in enumerate(edge_ver):
        for j, edge in enumerate(edges):
            if edge == 1:
                tree_list.extend(([j+1, j+1], [height-i, height-i-1]))
    for i in range(0, len(tree_list), 2):
        plt.plot(tree_list[i], tree_list[i+1], 'b')
    
    # plot style
    plt.xticks([])
    plt.yticks([])
    plt.show()


def get_spanning_tree(width, height):
    vertices = [[i for i in range(j, j+width)] for j in range(0, width*height, width)]

    edge_hor = [[randint(0, 99) for i in range(width-1)] for i in range(height)]
    edge_ver = [[randint(0, 99) for i in range(width)] for i in range(height-1)]

    max_edge = width*height - 1

    edge_hor_result = [[0 for j in range(width-1)] for i in range(height)]
    edge_ver_result = [[0 for j in range(width)] for i in range(height-1)]

    visited_veritces = []
    visited_veritces.append(vertices[0][0])
    x, y = 0, 0
    x_temp, y_temp = 0, 0
    shifted = 0
    while len(visited_veritces) < max_edge:
        for i in range(max_edge):
            min = INF
            x_temp, y_temp = x, y
                
            if (x-1 >= 0) and edge_ver[x-1][y] < min and vertices[x-1][y] not in visited_veritces:
                y_temp = y
                x_temp = x-1  
                min = edge_ver[x-1][y]
            if (x < height-1) and edge_ver[x][y] < min and vertices[x+1][y] not in visited_veritces:
                y_temp = y
                x_temp = x+1
                min = edge_ver[x][y]
            if (y-1 >= 0) and edge_hor[x][y-1] < min and vertices[x][y-1] not in visited_veritces:
                y_temp = y-1
                x_temp = x
                min = edge_hor[x][y-1]
            if (y < width-1) and edge_hor[x][y] < min and vertices[x][y+1] not in visited_veritces:
                y_temp = y+1
                x_temp = x
                min = edge_hor[x][y]

            if True:
                if shifted > 0:
                    shifted = 0
                    if vertices[x-1][y] in visited_veritces:
                        edge_ver_result[x-1][y] = 1
                    elif vertices[x+1][y] in visited_veritces:
                        edge_ver_result[x][y] = 1
                    elif vertices[x][y-1] in visited_veritces:
                        edge_hor_result[x][y-1] = 1
                    elif vertices[x][y+1] in visited_veritces:
                        edge_hor_result[x][y] = 1
                    else: 
                        print("error error")


                if vertices[x][y] not in visited_veritces:
                    visited_veritces.append(vertices[x][y])

            if x == x_temp and y == y_temp:
                break

            if x == x_temp:
                if y == y_temp+1:
                    edge_hor_result[x][y-1] = 1
                else:
                    edge_hor_result[x][y] = 1
            if y == y_temp:
                if x == x_temp+1:
                    edge_ver_result[x-1][y] = 1
                else:
                    edge_ver_result[x][y] = 1

            x, y = x_temp, y_temp
            
            visited_veritces.append(vertices[x_temp][y_temp])
        
        for i in range(height):
            a = 0
            for j in range(width):
                if vertices[i][j] not in visited_veritces:
                    if vertices[i-1][j] in visited_veritces:
                        x, y = i, j
                        shifted = 1
                        a = 1
                        break
                    elif vertices[i+1][j] in visited_veritces:
                        x, y = i, j
                        shifted = 1
                        a = 1
                        break
                    elif vertices[i][j-1] in visited_veritces:
                        x, y = i, j
                        shifted = 1
                        a = 1
                        break
                    elif vertices[i][j+1] in visited_veritces:
                        x, y = i, j
                        shifted = 1
                        a = 1
                        break
            if a == 1:
                break
    return (edge_hor_result, edge_ver_result)

def get_maze_from_spanning_tree(edge_hor, edge_ver):
    ver = edge_ver
    hor = edge_hor

    # interchange value of 1 and 0
    ver = list(map(lambda v: list(map(lambda x: 0 if x == 1 else 1, v)), ver))
    hor = list(map(lambda v: list(map(lambda x: 0 if x == 1 else 1, v)), hor))

    # add boundary
    boundary_start = [0 if i==width//3 else 1 for i in range(width)]
    boundary_end = [0 if i==width - width//3 else 1 for i in range(width)]
    ver.insert(0, boundary_start)
    ver.append(boundary_end)
    hor_temp = []

    for h in hor:
        h.insert(0, 1)
        h.append(1)
        hor_temp.append(h)
    
    ver, hor = hor, ver
    return (hor, ver)

def get_argument():
    parser = argparse.ArgumentParser(description="Get height and width")
    parser.add_argument('--width', type=int, default=20)
    parser.add_argument('--height', type=int, default=20)
    args = parser.parse_args()
    return (args.width, args.height)


if __name__ == "__main__":
    width, height = get_argument()

    edge_hor, edge_ver = get_spanning_tree(width=width, height=height)

    hor, ver = get_maze_from_spanning_tree(edge_hor, edge_ver)

    graphics(hor, ver)