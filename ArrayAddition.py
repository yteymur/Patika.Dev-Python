from itertools import chain, combinations
def powerset(arr):
  return chain.from_iterable(combinations(arr, r) for r in range(len(arr)+1))

def ArrayAddition(arr):
  maxval=max(arr,key=int)
  arr.remove(maxval)
  liste2=list(powerset(arr))
  for i in range(1,len(liste2)):
    if sum(liste2[i]) == maxval:
        return True

  return False

# keep this function call here 
print(ArrayAddition(input()))