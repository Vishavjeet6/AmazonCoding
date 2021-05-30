def ans(area):
    row = len(area)
    col = len(area[0])

    if area[0][0] == 0:
        return -1
    elif area[0][0] == 9:
        return 0
    else:
        temp = [[0]*col for i in range(row)]
        for i in range(col):
            if area[0][i] == 1:
                temp[0][i] = i
            elif area[0][i] == 0:
                continue
            elif area[0][i] == 9:
                return i
       
        for i in range(row):
            if area[i][0] == 1:
                temp[i][0] = i
            elif area[i][0] == 0:
                continue
            elif area[i][0] == 9:
                return i        
        
        for i in range(1,row):
            for j in range(1,col):
                if area[i][j] == 0:
                    continue
                if temp[i-1][j] == 0 and temp[i][j-1] == 0:
                    temp[i][j] = 0
                elif temp[i-1][j] == 0:
                    temp[i][j] = temp[i][j-1] + 1
                    if area[i][j] == 9:
                        print(temp)
                        return temp[i][j]
                else:
                    temp[i][j] = temp[i-1][j] + 1
                    if area[i][j] == 9:
                        print(temp)
                        return temp[i][j]
        return -1
            


    return 0

area1= [
    [1,0,0],
    [1,0,0],
    [1,9,1]
]

area2 = [
    [1,1,1],
    [1,0,1],
    [0,1,9]
]

print(ans(area1))
print("********")
print(ans(area2))