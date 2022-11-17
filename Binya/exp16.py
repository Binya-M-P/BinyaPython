n=int(input("Enter the number of elements : "))
print("Enter the elements : ")
l=[]
for i in range(0,n):
    a=int(input())
    if(a>100):
        a="over"
    l.append(a)
print(l)