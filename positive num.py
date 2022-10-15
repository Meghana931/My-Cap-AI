

 #to print positive numbers in a list
li=[]
n = int(input("Enter size of list "))
for i in range(0,n):
    y = int(input("Enter element of list "))
    li.append(y)
print("positive numbers in",li,"are: ")

for i in li:
    if i >= 0:
        print(i, end = " ")