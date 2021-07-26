def SwapII(strParam):
  stringlist=list(strParam.split())
  for i in range(len(stringlist)):
    templist=list(stringlist[i])
    for j in range(len(templist)):
      if templist[j].isnumeric():
          for k in range(j+2,len(templist)):
            if templist[k].isnumeric() and not templist[k-1].isnumeric() :
              temp1=templist[j]
              temp2=templist[k]
              templist[j]=temp2
              templist[k]=temp1
            else:
              pass
      elif templist[j].isupper():
        templist[j]=templist[j].casefold()
      elif templist[j].islower():
        templist[j] =templist[j].capitalize()
    stringlist[i]="".join(templist)
  strParam=" ".join(stringlist)
  return strParam
# keep this function call here 
print(SwapII(input()))