# My Python Program
# Task:  use if statements to output the result of the game fizzbuzz.  
# Start at 1
# For multiples of 3, output   Fizz
# For multiples of 5, output   Buzz
# For multiples of 15, output   FizzBuzz
# End at 32

result = ""

for x in range(32):
  myNum = x+1
  if myNum % 15 == 0:
    print("FizzBuzz")
  elif myNum % 5 == 0:
    print("Buzz")
  elif myNum % 3 == 0:
    print("Fizz")
  else:
    print(myNum)
    result = result + str(myNum) + "\n"
