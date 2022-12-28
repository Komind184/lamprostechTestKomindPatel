values =	{
  "I": 1,
  "V": 5,
  "X": 10,
  "L": 50,
  "C": 100,
  "D": 500,
  "M": 1000,
}

def romanToInt(str): 
  total = 0 
  i = 0

  while (i < len(str)): #find the lenght of string 
    s1 = values[str[i]] #get the value of string using 'i'(index) then store the value in var 's1'
    if (i+1 < len(str)): #find the length of string but this time increment the value of 'i' by 1
        s2 = values[str[i+1]]#Get the value of string by increment the value of 'i'
        if (s1 >= s2): #now check the S1 and S2 
          total = total + s1 # if s1 is greater than add value of s1 and total and store in total
          i = i + 1
        else: 
          total = total - s1 # if s2 is greater than sub value of s1 and total and store in total
          i = i + 1
    else: 
      total = total + s1 # here we check if only one char or value then it will be add with total and store in total 
      i = i + 1
  return total 
  
# Driver code 
inp = input("Enter The Roman Number   ")
print(romanToInt(inp)) 

