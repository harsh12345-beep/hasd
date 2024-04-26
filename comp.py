# Subtracting diagonals of the array
lis = [[1,2,3],[4,5,6],[7,8,9]]
temporary = 0
temp = 0
for i in range(len(lis)):
    for j in range(len(lis)):
            if(i == j):
                temporary = temporary + lis[i][j]
print(temporary)
for x  in reversed(range(len(lis))):
     for y in reversed(range(len(lis))):
          if(x==y):
            temp = temp + lis[x][y]
print(temporary-temp)       