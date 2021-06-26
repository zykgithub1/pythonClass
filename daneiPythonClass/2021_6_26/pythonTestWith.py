"""
with语法
"""
with open("111.jpg","rb")as f:
    data=f.read()
    print(data.istitle())
add=lambda a,b:a+b
ans=lambda file:open(file)
print(type(ans("dest.txt")))
