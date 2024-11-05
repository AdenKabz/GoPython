#break statement

num=20
while num<=25:
    print(num)
    if num==23:
        break
    num+=1

#continue statement
devices=["Laptop","Phone","Tablet"]
for x in devices:
    if x=="Phone":
        continue
    print(x)
    
