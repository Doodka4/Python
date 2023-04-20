def calc(a=1,b=1,mode="nothing"):
    s = 0
    if mode in ["+","-","/","*"]:
        pass
    else:
        error_msg=""
        return "Error: No such mode exists"
    match mode:
        case "+":
            s = a+b
            return s
        case "-":
            s = a-b
            return s
        case "/":
            try:
                s = a/b
            except ZeroDivisionError as ZeroDivisionMsg:
              print("Error: Cannot divide by zero")
            return s
        case "*":
            s = a*b
            return s
        case _:
            return "Error: No such case exists"

input_flag = True
while input_flag:
  try:
    a = int(input("A = "))
    b = int(input("B = "))
    mode = str(input("input an arithmetical operator: "))
    print(calc(a,b,mode))
  except ValueError:
      print("Error: Wrong input type \nInput again")
  input_flag = False
      
      
 
    







