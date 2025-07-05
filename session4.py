def calculator(a=20,b=30,operation="add"): 
     if operation =="add":
        return a+b
     elif operation=="subtract":
        return a-b
     elif operation=="multiply":
        return a*b
     elif operation=="divide":
      if b==0:
        return "error: division by Zero"
      return a/b
     else:
      return"invalid operation"
     print(calculator(20,30,"add"))