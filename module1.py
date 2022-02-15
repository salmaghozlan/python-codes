arr = [[40,40,90,90],
       [40,40,90,20],
       [33,33,70,70],
       [33,35,70,60]]
for r in range(0,len(arr)-1) :
    for c in range(0,len(arr[r])-1) :
        if arr[r+1][c]== arr[r][c+1] == arr[r][c] :
            print(arr[r][c])