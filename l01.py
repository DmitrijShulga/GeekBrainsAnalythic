''' print ("print int")
a = int(input("a = "))
b = int(input("b = "))
print (a + b)

# format
print (f"{a} - {b}")

# round
x = 1.234
y = 2.456
z = round (x * y, 2)
print(z)

# lists
q = [1,2,3]
print (5 in q)

# odd
w = [1,2,3]
is_odd = w[1] % 2 == 0
print(is_odd)

# if - else
if a > b:
    print(a)
elif a < b:
    print(b)
else:
    print("they are equal")

# while
original = 213
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
    print(inverted)
else:
    print("that's enough :--)") 

# for
r = range(10)
for i in r:
    print(i**2)

# increment in range
for i in range(1, 5, 2):
    print(i) 

# strings
text = "qwerty asdf"
print(len(text))
print('q' in text)
print(text.isdigit())
print(text.isupper())
print(text.replace('q', '2'))
print(text[len(text)-1]) 

# lists 2
color = ['red', 'green', 'blue']
color.append('gray')
color.remove('red')
del(color)
print(color) '''

# functions
def f(x):
    if x == 1:
        return "Целое"
    elif x == 2.3:
        return 23
    else:
        return

arg = 1
print(f(arg))
print(type(f(arg)))
