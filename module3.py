list_values = [
[10, 2, 1, 2], #r=0 , c=0
[1, 20, 2, 4], #r=1 , c=1
[1, 2, 30, 4], #r=2 , c=2
[2, 2, 1, 40],  #r=3 , c=3
]


for row in list_values:

    for col in row :
        count= 0

        if col == row[count]:
            print(row[count])
