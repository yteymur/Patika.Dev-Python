def SimpleMode(arr):
  maxval=-999
  idx=999
  for i in range(len(arr)):
    counter=arr.count(arr[i])
    if counter > maxval and counter >=2:
      maxval=counter
      idx=i
  if idx == 999:
    return -1
  return arr[idx]

# keep this function call here 
print(SimpleMode(input()))