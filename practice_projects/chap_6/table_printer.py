tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    width=[]
    # To check the max length for column width
    for i in range(len(table)):
        col=[]
        for j in range(len(table[i])):
            col.append(len(table[i][j]))
        col.sort()
        width.append(int(col[len(col)-1]))
    # To make the table
    # T-loop
    for i in range(len(table[0])):
        for j in range(len(table)):
            print(table[j][i].rjust(width[j]),end=' ')
        print()

printTable(tableData)

# What if the length of all inner lists was not same? Make changes accordingly, in the T-loop.
