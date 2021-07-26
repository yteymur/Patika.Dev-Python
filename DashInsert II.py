def DashInsertII(num):
  num=str(num)
  stringnumber=list(num)
  for i in range((len(stringnumber)*2)):
    try:
      if int(stringnumber[i]) % 2 == 0 and int(stringnumber[i+1]) % 2 == 0 and (int(stringnumber[i]) != 0 and int(stringnumber[i+1]) != 0) :
        stringnumber.insert(i+1, "*")
      if int(stringnumber[i]) % 2 !=0 and int(stringnumber[i+1]) % 2 != 0 and (int(stringnumber[i]) != 0 and int(stringnumber[i+1]) != 0) :
        stringnumber.insert(i+1,"-")
    except ValueError:
      pass
    except IndexError:
      break
  num="".join(stringnumber)

  return num

# keep this function call here 
print(DashInsertII(input()))