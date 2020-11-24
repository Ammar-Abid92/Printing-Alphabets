
print("\t"*3, "  *")
b = 13
c = 0
while c <= 11:
    print(b*" ", "*", c*"  ", "*")
    b = b-1
    c = c+1
    if b == 7:
        print("", b*" ", 7*" -")
