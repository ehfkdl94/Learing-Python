from pprint import pprint
row, col = map(int, input().split())

matrix = []
for i in range(row):
    matrix.append(list(input()))
pprint(matrix, indent=2, width=30)
count =0
for i in range(row):
    for j in range(col):
        if matrix[i][j]=='.':
            if i==0:
                if matrix[i][j+1]=='*':
                    count+=1
                elif matrix[i+1][j]=='*':
                    count+=1
                elif matrix[i+1][j+1]=='*':
                    count+=1
                else:
                    pass
            
