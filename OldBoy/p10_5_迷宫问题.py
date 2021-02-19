# 走迷宫
# 一个栈来维护一个路径，如果当前点无路可走，则出栈
def escape_maze(maze):
    end_r, end_c = len(maze)-2, len(maze[0])-2

    start = (1, 1)
    stack = [start]
    walked = [start]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 分别对应上下左右移动一格
    while stack:
        node = stack[-1]  # 当前点
        for dir in directions:
            i, j = node[0] + dir[0], node[1] + dir[1]  # 下一个点
            if (i, j) == (end_r, end_c):
                # 表示走出了迷宫
                stack.append((i,j))
                print(stack)
                return True
            if 1<=i<=end_r and 1<=j<=end_c and maze[i][j] != 1 and (i,j) not in walked:
                # 单元格合法，就入栈
                stack.append((i, j))
                walked.append((i, j))
                # 这个break至关重要，避免把上下左右中多个点存到栈里。因为我们是dfs，只存一个即可，实在不行就出栈
                break
        else:
            # 表示当前点的四个方向都不能走
            stack.pop()
    else:
        return False

maze = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,0,0,1,1,0,0,1],
    [1,0,1,1,1,0,0,0,0,1],
    [1,0,0,0,1,0,0,0,0,1],
    [1,0,1,0,0,0,1,0,0,1],
    [1,0,1,1,1,0,1,1,0,1],
    [1,1,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]
    ]

escape_maze(maze)

