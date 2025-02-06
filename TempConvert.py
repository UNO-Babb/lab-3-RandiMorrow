#TempConvert.py
#Name:
#Date:
#Assignment:


def main():
  #Prompt the user for a Fahrenheit temperature
  #Convert that temperature to celsius, rounding to 1 decimal percision
  #Output converted temperature.
 
  tempF = input ("Enter a temperature in Fahrenheit: ")
  tempF = float(tempF)
  tempC = (5/9) * (tempF - 32) 

  tempC = round(tempC, 1)
  

  print(tempF, "is ", tempC, "degrees celsius.")
if __name__ == '__main__':
  main()
 