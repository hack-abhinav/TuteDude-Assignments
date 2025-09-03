a=[]
for i in range(10):
    a.append((i+1))
print("Original list: ",a)
b=a[:5]
print("Extracted first five elements: ",b)
c=b[::-1]
print("Reversed extracted elements: ",c)