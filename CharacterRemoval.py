def CharacterRemoval(strArr):
  firststring=strArr[0]
  wordslist=strArr[1].split(",")
  wordslist.sort(key=len,reverse=True)
  output=9999999
  for i in range((len(wordslist))):
    counter=0
    templist=list(wordslist[i])
    for j in range((len(templist)+1)):
      try:
        if templist[j] not in firststring:
          break
      except IndexError:
        pass
      if (j == len(templist)):
        find=False
        for k in range(len(templist)):
          for l in range(len(templist)):
            try:
              if firststring.count(firststring[k]) == 1:
                if k < l and (firststring.rindex(templist[k])) > firststring.rindex(templist[l]):
                  find=True
                  break
              else:
                if k < l and (firststring.rindex(templist[k]) > firststring.rindex(templist[l],(firststring.rindex(templist[k])+1))):
                  find=True
                  break
            except ValueError:
              pass
          if find:
            break
        if find:
          break
        result=len(firststring)-counter
        output=min(output,result)
      else:
        if templist.count(templist[j]) > firststring.count(templist[j]):
          break
        else:
          counter +=1
  if output == 9999999:
    return -1 
  return output

# keep this function call here 
print(CharacterRemoval(input()))