def FizzBuzz(num):

  # code goes here
  list1=[]
  for i in range(1,num+1):
    if i % 3 == 0 and i % 5 == 0:
      list1.append("FizzBuzz")
    elif i % 3 == 0:
      list1.append("Fizz")
    elif i % 5 == 0:
      list1.append("Buzz")
    else:
      list1.append(str(i))
    num =" ".join(list1)
  return num

# keep this function call here 
print(FizzBuzz(input()))