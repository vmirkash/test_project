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
s1 = y[:(len(y)//2)+1]
s2 = y[len(y)//2:]
if len(y)%2 == 0:
    print(s1, s2)
else:
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

# task 6
a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print(3)
elif a == b or b == c or c == a:
    print(2)
else:
    print(0)

# task 7 (1)
num = 10
while num > 0:
    print(num)
    num -= 1

# task 7 (2)
num1 = 20
while num1 >= 1:
    print(num1, end = ' ')
    num1 -= 1

# task 7 (3)
num3 = int(input())
count = 0
while num3 % 2 == 0:
    num3 //= 2
    count += 1
print(count)

# task 8 (1)
list1 = [1, 3, 32, 56, 2, 14]
while list1:
    print(list1.pop(0))

# (3)
list2 = [1, 3, 32, 56, 2, 14]
while list2:
    list2.sort(reverse=True)
    print(list2.pop())



