def abc (a,b):
    print (a+b)
abc (5,7)

lst = [7, 8, 9]
ln = len(lst)
lst[0], lst[ln-1] = lst[ln-1], lst [0]
print(lst)
for i in range(ln):
    lst[i], lst[ln-1-i] = lst[ln-1-i], lst[i]
    print(lst)