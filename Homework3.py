# task 1
x = input("Text:")
print(x[3])
print(x[-1])
print(x[0:5])
print(x[0:-2])
print(x[::2])
print(x[1::2])
print(x[::-1])
print(x[::-2])
print(x[-2::-2])
print(x[-2:0:-1])
print(len(x))

# task 2
y = input("String:")
s1 = y[:len(y)//2]
s2 = y[len(y)//2:]
print(s2, s1)

# task 3
year = int(input("Birth year:"))
if year%4 == 0 and year%100 != 0 and year%400 == 0:
    print("YES")
else:
    print("NO")

# task 4
a = int(input())
b = int(input())
c = int(input())
if (a + b > c) and (c + b > a) and (a + c > b):
    print("YES")
else:
    print("NO")

