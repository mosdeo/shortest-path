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

def bfs_search(current, traget, pass_node_list):
    # 1.把起點塞入queue
    queue = [current]

    # 2.重複下述兩步驟，直到queue裡面沒有東西為止
    while len(queue)>0:
        # 2-1.queue彈出一點給head
        head, queue = queue[0], queue[1:]

        # 2-2.找出跟此點相鄰的點，並且尚未遍歷的點，通通（依照編號順序）塞入queue。
        neighbors = get_neighbor(head)    
        for neighbor in neighbors:
            x, y = neighbor
            if map_visited[x][y] == False and map[x][y] != 3:
                time_complex[0] += 1
                map_visited[x][y] = True
                map_parent[x][y] = head #標記其起節點
                queue += [[x, y]]

                # 從尾找到頭，記錄中間的路徑
                if [x, y] == traget:
                    pass_node_list += [traget]
                    while neighbor != start_node:
                        _x, _y = neighbor
                        neighbor = map_parent[_x][_y]
                        pass_node_list += [neighbor]
    return pass_node_list

if __name__ == "__main__":
    # 不斷找出尚未遍歷的點當作起點
    pass_node_list = []
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map_visited[x][y] == False:
                pass_node_list = bfs_search(current=[x, y], traget=end_node, pass_node_list=pass_node_list)

    # 根據搜尋好的節點，繪製路徑
    map = [[str(element).replace("0", " ") for element in row] for row in map]

    for node in pass_node_list:
        x, y = node
        if map[x][y] in {'1' ,'2'}:
            continue 
        map[x][y] = "A"
        
    for m in map:
        print(str(m).replace('\'', ''))
        
    print("time_complex={}".format(time_complex))
        