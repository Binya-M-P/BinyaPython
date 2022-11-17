s=input("Enter the string : ")
l=s.split(" ")
d={}
for i in l:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
print("Occurance of the words :")
for i,j in d.items():
    print(i,j)