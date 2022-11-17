l1=[1,2,3,4,5]
l2=[2,3,5,4,6]
a=len(l1)
b=len(l2)
if(a==b):
    print("These two lists are in same length.")
else:
    print("Length of list are not equal.")

if(sum(l1)==sum(l2)):
    print("Sum are equal.")
else:
    print("Sum are not equal.")
print("Values occure in both :")
for i in l1:
    if i in l2:
        print(i)