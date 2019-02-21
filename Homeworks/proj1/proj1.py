#File name:   proj1.py
#Author:      Brandon Nguyen
#Date:        10/31/15
#Lab Section: 20
#E-mail:      Brando15@umbc.edu
#Description: This program prompts the user to enter dimensions for a grid. After creating a grid full of '.'s, the program asks the user which cells they would like
#             to turn 'on' (shown by an 'A'). Then the user is asked how many iterations they would like to run the game. During each iteration, each cell has its 
#             number of neighbors counted up. Depending on how many neighbors a certain cell has, the cell either dies, remains alive, or is brought to life.
#             This program simulates Conway's Game of Life.



#Prompts the user for dimensions of the board, changed cells, and iterations. Should be ran ONCE
def startGame():
    rows = -1
    while rows < 1:
        rows = int(input("Please enter the number of rows: "))
        if rows < 1:
            print("\tThat is not a valid value; please enter a number\n\tgreater than or equal to 1")

    columns = -1
    while columns < 1:
        columns = int(input("Please enter the number of columns: "))
        if columns < 1:
            print("\tThat is not a valid value; please enter a number\n\tgreater than or equal to 1")

    print()
    newRow = []
    newColumn = []
    row = -1
    #Until the user enters 'q' as the row
    while row != 'q':
        row = -1
        
        #until the row = 'q' or it's a valid number
        while row != 'q' and (row < 0 or row > rows-1):
            row = input("Please enter the row of a cell to turn on (or q to exit): ")
            if row != 'q':
                row = int(row)
                if (row < 0 or row > rows-1):
                    print("\tThat is not a valid value; please enter a number\n\tbetween 0 and", rows-1, "inclusive...")        
        #if the input is valid
        if row != 'q':
            row = int(row)
            newRow.append(row)

        if row != 'q':
            column = -1
            while column < 0 or column > columns -1:
                column = int(input("Please enter a column for that cell: "))
                if column < 0 or column > columns - 1:
                    print("\tThat is not a valid value; please enter a number\n\tbetween 0 and", columns-1, "inclusive...")        
                else:
                    newColumn.append(column)
                    print()



    print()
    
    iterations = int(input("How many iterations should i run? "))
    while iterations < 0:
        print("\tThat is not a valid value; please enter a number\n\tgreater than or equal to 0")
        iterations = int(input("How many iterations should i run? "))
    
    return rows, columns, newRow, newColumn, iterations


#Creates the starting board and should only be ran ONCE
def spawnGrid(rows, columns, newRow, newColumn):
    grid = []
    
    #Creates a blank board with the given dimensions
    for length in range(rows):
        row = []
        for i in range(columns): 
            row.append(".")
        grid.append(row)
    
    #Changes the status of the cells asked to be alive
    for i in range(len(newRow)):
        grid[newRow[i]][newColumn[i]] = 'A'

    return grid

#Takes in the current grid and prints it out
def printGrid(grid):
    
    for column in range(len(grid)):
        for row in range(len(grid[column])):
            print(grid[column][row], end = "")
        print()
    print()

def checkNeighbors(tempGrid, column, row):
    
    neighbors = 0
    #if on the first row
    if row == 0:
        #if on the first column
        if column == 0:
            neighbors += checkE(tempGrid, column, row)
            neighbors += checkS(tempGrid, column, row)
            neighbors += checkSE(tempGrid, column, row)
        #if on the last column
        elif column == len(tempGrid[row])-1:
            neighbors += checkW(tempGrid, column, row)
            neighbors += checkS(tempGrid, column, row)
            neighbors += checkSW(tempGrid, column, row)
        #if on the first row and NOT first/last column
        else:
            neighbors += checkW(tempGrid, column, row)
            neighbors += checkE(tempGrid, column, row)
            neighbors += checkSE(tempGrid, column, row)
            neighbors += checkS(tempGrid, column, row)
            neighbors += checkSW(tempGrid, column, row)
    #if in the last row
    elif row == len(tempGrid) - 1:
        #if on the first column
        if column == 0:
            neighbors += checkN(tempGrid, column, row)
            neighbors += checkNE(tempGrid, column, row)
            neighbors += checkE(tempGrid, column, row)
        #if on the last column
        elif column == len(tempGrid[row])-1:
            neighbors += checkN(tempGrid, column, row)
            neighbors += checkNW(tempGrid, column, row)
            neighbors += checkW(tempGrid, column, row)
        #if neither first nor last column
        else:
            neighbors += checkE(tempGrid, column, row)
            neighbors += checkW(tempGrid, column, row)
            neighbors += checkNE(tempGrid, column, row)
            neighbors += checkNW(tempGrid, column, row)
            neighbors += checkN(tempGrid, column, row)
    #first column, but in a 'middle' row
    elif row != 0 and row != len(tempGrid) - 1 and column == 0:
        neighbors += checkN(tempGrid, column, row)
        neighbors += checkNE(tempGrid, column, row)
        neighbors += checkE(tempGrid, column, row)
        neighbors += checkS(tempGrid, column, row)
        neighbors += checkSE(tempGrid, column, row)

    #Last column, but in a 'middle' row
    elif row != 0 and row != len(tempGrid) - 1 and column == len(tempGrid[row]) - 1:
        neighbors += checkN(tempGrid, column, row)
        neighbors += checkNW(tempGrid, column, row)
        neighbors += checkW(tempGrid, column, row)
        neighbors += checkSW(tempGrid, column, row)
        neighbors += checkS(tempGrid, column, row)
    #Any cell that is in a 'middle' row and 'middle' column
    else:
        neighbors += checkN(tempGrid, column, row)
        neighbors += checkNE(tempGrid, column, row)
        neighbors += checkE(tempGrid, column, row)
        neighbors += checkSE(tempGrid, column, row)
        neighbors += checkS(tempGrid, column, row)
        neighbors += checkSW(tempGrid, column, row)
        neighbors += checkW(tempGrid, column, row)
        neighbors += checkNW(tempGrid, column, row)
    return neighbors


def checkNW(tempGrid, column, row):
    neighbors = 0
    if tempGrid[row-1][column-1] == 'A':
        neighbors = 1
    return neighbors

def checkN(tempGrid, column, row):
    neighbors = 0
    if tempGrid[row-1][column] == 'A':
        neighbors = 1
    return neighbors

def checkNE(tempGrid, column, row):
    neighbors = 0
    if tempGrid[row-1][column+1] == 'A':
        neighbors = 1
    return neighbors

def checkW(tempGrid, column, row):
    neighbors = 0
    if tempGrid[row][column-1] == 'A':
        neighbors = 1
    return neighbors

def checkE(tempGrid, column, row):
    neighbors = 0
    if tempGrid[row][column+1] == 'A':
        neighbors = 1
    return neighbors

def checkSW(tempGrid, column, row):
    neighbors = 0
    if tempGrid[row+1][column-1] == 'A':
        neighbors = 1
    return neighbors

def checkS(tempGrid, column, row):
    neighbors = 0
    if tempGrid[row+1][column] == 'A':
        neighbors = 1
    return neighbors


def checkSE(tempGrid, column, row):
    neighbors = 0
    if tempGrid[row+1][column+1] == 'A':
        neighbors = 1
    return neighbors



def neighbors(grid):
    tempGrid = grid[:]
    listNeighbors = []
    for row in range (len(tempGrid)):
        tempList = []
        for column in range(len(tempGrid[row])):
            neighbors = checkNeighbors(tempGrid, column, row)
            tempList.append(neighbors)
        listNeighbors.append(tempList)


    return listNeighbors


def change(grid, listNeighbors):        
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if grid[row][column] == 'A' and listNeighbors[row][column] < 2:
                grid[row][column] = '.'
                
            if grid[row][column] == 'A' and (listNeighbors[row][column] == 2 or listNeighbors[row][column] == 3):
                grid[row][column] = 'A'

            if grid[row][column] == 'A' and listNeighbors[row][column] > 3:
                grid[row][column] = '.'

            if grid[row][column] == '.' and listNeighbors[row][column] == 3:
                grid[row][column] = 'A'

    return grid

def main():
    rows, columns, newRow, newColumn, iterations = startGame()
    grid = spawnGrid(rows, columns, newRow, newColumn)
    print("Starting Board:\n ")
    printGrid(grid)
    
    for gameLength in range (1, iterations+1):
        
        listNeighbors = neighbors(grid)
        grid = change(grid, listNeighbors)
        print("Iteration "+ str(gameLength)+ ":")
        print()
        printGrid(grid)

main()
