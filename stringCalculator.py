def StringCalculate(strParam):
  stringlist=list(strParam)
  operators="+*/("
  for i in range(1,len(stringlist)):
    if stringlist[i] == "(" and stringlist[i-1] not in operators:
      stringlist.index(i,"*")
  strParam="".join(stringlist)
  return int(eval(strParam))

# keep this function call here 
print(StringCalculate(input()))