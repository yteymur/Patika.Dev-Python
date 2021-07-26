def StringChanges(strParam):
  list1=list(strParam)
  for _ in range(len(list1)):
    if "M" in list1 and list1.index("M") == 0:
        list1.pop(0)

  for _ in range(len(list1)):
    if "N" in list1:
      try:
        temp=list1.index("N")
        list1.pop(list1.index("N"))
        list1.pop(temp)
      except IndexError:
        pass
        
  for _ in range(len(list1)):
    if "M" in list1 and list1.index("M") == 0:
        list1.pop(0)
  for _ in range(len(list1)):
    if "M" in list1 and list1.index("M") != 0:
        list1[list1.index("M")] =list1[(list1.index("M")-1)]
  strParam="".join(list1)
  return strParam

# keep this function call here 
print(StringChanges(input()))