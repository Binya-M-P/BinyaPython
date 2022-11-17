d={1:4,0:2,3:4,2:1}
print("Original dictionary : ",d)
sd = sorted(d.items())
print("Dictionary in ascending order by keys : ",sd)
sd = sorted(d.items(),reverse=True)
print("Dictionary in descending order by keys : ",sd)
