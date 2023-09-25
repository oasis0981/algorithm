def solution(keyinput, board):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    inputs = ['up', 'down', 'right', 'left']
    
    x, y = 0, 0
    range_x, range_y = board[0] // 2, board[1] // 2
    
    for key in keyinput:
        idx = inputs.index(key)
        nx = x + dx[idx]
        ny = y + dy[idx]
        if -range_x <= nx <= range_x:
            x = nx
        if -range_y <= ny <= range_y:
            y = ny
            
    return [x,y]