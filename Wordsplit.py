def WordSplit(strArr):
  l1=strArr[0]
  l2=strArr[1].split(",")
  new=[]
  for char in range(len(l2)) :
      if l2[char]  in l1 :
          new.append(l2[char])
  for char in range(len(new)):
      for char2 in range(len(new)):
          if len(new[char])+len(new[char2]) and new[char]+new[char2] == l1:
              return (new[char]+","+new[char2])
  return 'not possible'
# keep this function call here 
print(WordSplit(input()))