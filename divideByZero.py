def spam(divideByZero):
    try:
        return 42 / divideByZero
    except ZeroDivisionError:
        print('Error: Invalid arguement.')

print(spam(1))
print(spam(2))
print(spam(0))
print(spam(3))            