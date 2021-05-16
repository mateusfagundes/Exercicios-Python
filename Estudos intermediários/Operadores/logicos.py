b1 = True
b2 = False
b3 = True

print(b1 and b2 and b3) # E
print(b1 or b2 or b3) # OU
print(b1 != b2) # != Equivale ao XOR
print(not b1) # NÃO
print(not b2) 

print(b1 and not b2 and b3)

x = 3
y = 4

print(b1 and not b2 and x < y)