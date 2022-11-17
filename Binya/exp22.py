n=int(input("Enter the number of strings : "))
print("Enter the strings : ")
l1=[]
for i in range(0,n):
    x=input()
    l1.append(x)
print(l1)
c=0
for i in l1:
    for j in i:
        if(j=="a" or j=="A"):
            c=c+1
print("Number of a= ",c)