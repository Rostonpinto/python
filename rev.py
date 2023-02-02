# n ='python how are you'.split(' ')
# print(n)
# 2D list taking value from user 
row = int(input("enter the row "))
column = int(input("enter the column"))
ls = [] # fist list 
print("enter the vlues  ")
# For user input

for i in range(row):# A for loop for row entries
    a=[] #second list 
    for j in range(column):# A for loop for colum  entries
       a.append(input("")) 
    ls.append(a)
# for print valuse 
for i in range(row):
    for j in range(column):
        print(ls[i][j], end=" ")
    print()
 



