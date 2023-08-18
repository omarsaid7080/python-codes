a = int(input("enter the first number :"))
b = int(input("enter the second  number :"))
operator = str(input("""
enter one  for multiplication
enter two for  division
enter three for Summation
enter four for Subtraction  : """))
if operator == "one" :
  print(a * b)
  if operator== "two":
    print(a / b)
    if operator == "three" :
      print(a + b)
      if operator ==  "four" :
        print(a - b)
else   :
 print("enter the correct operation")