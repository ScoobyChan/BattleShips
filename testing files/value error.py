i = input("Enter a number between: ")
try:
    i = int(i)
    print(i)
except ValueError:
    print(i, 'Doesnt equal a number')
