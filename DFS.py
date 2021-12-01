map = [
    [ 1, 0, 3, 3, 3, 3, 3, 0, 3, 3 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 3, 0 ],
    [ 0, 0, 0, 3, 0, 0, 3, 3, 3, 0 ],
    [ 3, 0, 0, 0, 0, 3, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 3, 0, 0, 0, 0, 0 ],
    [ 3, 0, 0, 0, 3, 0, 0, 3, 0, 3 ],
    [ 3, 0, 0, 0, 0, 3, 3, 0, 0, 2 ],
    [ 0, 0, 3, 0, 0, 0, 0, 0, 0, 0 ],
    [ 3, 3, 3, 0, 0, 3, 0, 3, 0, 3 ],
    [ 3, 0, 0, 0, 0, 3, 3, 3, 0, 3 ],
]
end_node = [6,9]
start_node = [0,0]
map_visited = [[False]*len(map[0]) for _ in range(len(map))]
map_parent = [[None]*len(map[0]) for _ in range(len(map))]
time_complex = [0]

def get_neighbor(current_node):
    nodes = []
    x, y = current_node
    if (x-1>=0):
        nodes += [[x-1,y]]
    if (x+1>=0 and x+1<len(map[0])):
        nodes += [[x+1,y]]
    if (y-1>=0):
        nodes += [[x,y-1]]
    if (y+1>=0 and y+1<len(map)):
        nodes += [[x,y+1]]
    return nodes

def dfs_search(current, origin, traget):
    x, y = current
    map_visited[x][y] = True
    neighbors = get_neighbor(current)
           
    for neighbor in neighbors:
        x, y = neighbor
        if map_visited[x][y] == False and map[x][y] != 3:
            time_complex[0] += 1
            map_parent[x][y] = current #標記其父節點
            dfs_search(current=neighbor, origin=origin, traget=traget)

            if neighbor == traget:
                return

if __name__ == "__main__":
    # 不斷找出尚未遍歷的點當作起點
    pass_node_list = []
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map_visited[x][y] == False:
                dfs_search(current=[x, y], origin=start_node, traget=end_node)

    # 從尾找到頭，記錄中間的路徑
    current = end_node
    while current != start_node:
        pass_node_list += [current]
        x, y = current
        current = map_parent[x][y]
    pass_node_list += [start_node]

    # 根據搜尋好的節點，繪製路徑
    map = [[str(element).replace("0", " ") for element in row] for row in map]

    for node in pass_node_list:
        x, y = node
        if map[x][y] in {'1' ,'2'}:
            continue 
        map[x][y] = "A"
        
    for m in map:
        print(str(m).replace('\'', ''))

    print("len(pass_node_list)={}".format(len(pass_node_list)))
    print("time_complex={}".format(time_complex))
        