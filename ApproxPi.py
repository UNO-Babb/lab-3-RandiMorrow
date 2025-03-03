#ApproxPi.py
#Name:
#Date:
#Assignment:
import math
import time


#PLEASE NOTE - This is an optional, extra credit portion of the lab.

def main():
  realPi = math.pi

  #ask user for decimal percision (up to 10)
  number = int(input("Enter a decimal precision between 1 and 10: "))

  start = time.time()
  #calculate pi using the approximation technique
  #Loop until the level of percision is reached
  approxPi = 4/1
  sign = -1
  denom = 3

  while True:
    new_approxPi = round(approxPi, number)
    new_realPi = round(realPi, number) 

    if new_approxPi == new_realPi:
      break

    approxPi = approxPi + (sign * 4 / denom) 
    sign = sign * -1 
    denom = denom + 2


  end = time.time()

  elapsedTime = end - start
  print(elapsedTime)

if __name__ == '__main__':
  main()
