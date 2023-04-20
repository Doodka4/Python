def division(a=1,b=1):
    try:
        s = a/b
        return s
    except ZeroDivisionError:
        return "cant divide by zero"
    
a = int(input("a="))
b = int(input("b="))
print(division(a,b))