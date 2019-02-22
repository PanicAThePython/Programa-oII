x1 = int(input("X1:"))
y1 = int(input("Y1:"))
x2 = int(input("X2:"))
y2 = int(input("Y2:"))
x3 = int(input("X3:"))
y3 = int(input("Y3:"))


eq1 = (x2-x1)/(y2-y1)
eq2 = (x3-x2)/(y3-y2)

if eq1 == eq2:
    print("Os três pontos estão alinhads!")
else:
    print("Pontos não alinhados...")