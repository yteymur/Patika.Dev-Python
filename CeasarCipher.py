import string
def CaesarCipher(strParam,num):
  operators=" .,'\"-;:...!&()="
  alphabet=list(string.ascii_letters)
  stringlist=list(strParam)
  for i in range(len(strParam)):
    if stringlist[i] in operators:
      pass
    elif stringlist[i].islower():
      stringlist[i] = alphabet[((alphabet.index(stringlist[i])+num) % 26)]
    elif stringlist[i].isupper():
      stringlist[i] = alphabet[(((alphabet.index(stringlist[i])+num) % 26)+26)]
  strParam="".join(stringlist)
  return strParam

# keep this function call here 
print(CaesarCipher(input()))