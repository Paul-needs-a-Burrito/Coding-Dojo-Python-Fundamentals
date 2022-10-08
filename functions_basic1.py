# Assignment: Functions Basic I

# For each of the following code snippets, first predict the output (what you will see printed to the terminal). Once you've made a prediction, run the code snippet to see if you are correct!

#1 PREDICTION: 5  RESULT: 5
def a():
    return 5
print(a())

#2 PREDICTION: 10  RESULT: 10
def a():
    return 5
print(a()+a())

#3 PREDICTION: 5  RESULT: 5
def a():
    return 5
    return 10
print(a())

#4 PREDICTION: 5  RESULT: 5
def a():
    return 5
    print(10)
print(a())

#5 PREDICTION: 5  RESULT: 5  NONE
def a():
    print(5)
x = a()
print(x)

#6 PREDICTION: 3  5  8  RESULT: 3  5  TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))

#7 PREDICTION: 25 RESULT: 25
def a(b,c):
    return str(b)+str(c)
print(a(2,5))

#8 PREDICTION: 100  10  RESULT: 100  10
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())

#9 PREDICTION: 7  14  21 RESULT: 7  14  21
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))

#10 PREDICTION: 8 RESULT: 8
def a(b,c):
    return b+c
    return 10
print(a(3,5))

#11 PREDICTION: 500  500  300  500  RESULT: 500  500  300  500
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)

#12 PREDICTION: 500  500  300  500  RESULT: 500  500  300  500
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)

#13 PREDICTION: 500  500  300  300  RESULT: 500  500  300  300
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b = a()
print(b)

#14 PREDICTION: 1  3  2  RESULT: 1  3  2
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()

#15 PREDICTION: 1  3  5  10  RESULT: 1  3  5  10
def a():
    print(1)
    x = b()
    print(x)
    return 10

def b():
    print(3)
    return 5
y = a()
print(y)

