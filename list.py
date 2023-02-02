#                                       1  accepting  data from user and returning  in list
# new_list =[""]
# data = input("enter the values").split()
# new_list = data
# print(new_list)
#                                      2 adding the new values to the existing list  depening on the user input and removing is pending
# ls = ["babe"]
# h = int( input("how many values you want to enter "))
# for x in range(h):
#     en = input("enter the value ")
#     ls.append(en)
# print(ls)
# r = input("enter the value to be removed ")
# for x in ls:
#     if x==r:
#         ls.remove(r)
#     else:
#        continue
# print(ls)

#                                    3 insert taking values from user

# ls = ["apple","orange"]
# x = int(input(" at which index you want add the element "))
# y = input("enter the value to be added ")
# ls.insert(x,y)
# print(ls)
#                                    4 palandriom method 1

# data = input("ENTER THE STRING")
# rev=""
# rev = data
# if data == rev:
#     print("its a palndriom")
# else:
#     print("its not a palandriom")
#                                   5 palandriom using list

# s1=input("enter the string ")
# lst = list(s1)
# lst2 = reversed(lst)
# if s1 == ''.join(lst2):
#     print("its a palndriom")
# else:
#     print("its not a palandriom")
#                                       use of sort in lsit
# lst = []
# n = int(input("how many values you want to enter "))
# for i in range(n):
#     new = input("enter the element ")
#     lst.append(new)
# lst.sort()
# print(lst)

fruit = []
veg = []
meat =[]
#                                   2D LIST EXAMPLE

n = int(input("how many fruits  "))
for i in range(n):
    f = input("add the fruit ")
    fruit.append(f)

o = int(input("how many veges "))
for j in range(o):
    v = input("add a vegi ")
    veg.append(v)

p = int(input("how many meat  "))
for k in range(p):
    m = input("add the meat ")
    meat.append(m)
food = [fruit,veg,meat]
print(food)
# for coll in food:
#     print(coll)











