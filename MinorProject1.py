import csv
import pandas as pd

df = pd.read_csv(r"C:\Users\rohit\Downloads\Task_Training_Data .csv")

print(df.get(['Name', 'Email']))

def River(grid):

    L=[]
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            k = [0]
            if grid[r][c] == "1":
                compute(grid, r, c, k)
                L.append(k)
    return L



def compute(grid, i, j, k):
    directions = [[-1, 0], [0, 1], [0, -1], [1, 0]]
    grid[i][j] = "0"
    k[0]+=1
    for dir in directions:
        newr, newc = i + dir[0], j + dir[1]
        if newr >= 0 and newc >= 0 and newr < len(grid) and newc < len(grid[0]):
            if grid[newr][newc] == "1":
                compute(grid, newr, newc, k)



def authenticate():
    count = 1
    login_success = False

    while count <= 2 and login_success == False:
        x = input('Enter your name')
        y = input('Enter your Email')
        for i in df.index:
            if x == df['Name'][i].strip() and y == df['Email'][i].strip():
                login_success = True
                break
        if count <= 1 and login_success == False:
            count += 1
            print('Incorrect Details. You have 1 more attempt left')

        elif login_success == False:
            print('Sorry!, incorrect details')
            break
    if login_success == True:
        x = open(r"C:\Users\rohit\Downloads\welcome_note.txt", 'r')
        print(x.read())
        a = input('Do you want to continue, Yes or No? ')
        if a == 'Yes' or a == 'yes':
            while True:
                try:
                    p = input('Press P to Play')
                    if p == 'p' or p == 'P':

                        row = int(input('Enter the value for row of your matrix '))
                        col = int(input('Enter the value for column of your matrix '))

                        matrix = []
                        print("Enter the entries rowwise ", row * col, " times:")

                        for i in range(row):
                            print('Enter value for Row ', i + 1)
                            a = []
                            for j in range(col):  # A for loop for column entries
                                a.append((input()))
                            matrix.append(a)

                        # For printing the matrix
                        for i in range(row):
                            for j in range(col):
                                print(matrix[i][j], end=" ")
                            print()

                        riv = River(matrix)
                        print('Lengths of all rivers: ',riv)
                        break

                    else:
                        raise

                except:
                    print('You Entered the wrong choice, Enter P to play ')

        elif a == 'No' or 'no':
            print('Good Bye')
            return



authenticate()





#a=[['0','1','1','0'],
#      ['0','1','0','0'],
#      ['1','0','0','0'],
#      ['0','1','1','1'],]
#riv = River(matrix)
#print(riv)