def flatten(userinput=[[1,'a',['cat'],2],[[[3]],'dog'],4,5],result=[]):
    for i in userinput:
        if type(i) == list:
            flatten(i,result)
        else:
            result.append(i)
    return result



def reverse(userinput=[[1, 2], [3, 4], [5, 6, 7]]):
    for i in range(0,len(userinput)):
        if type(userinput[i]) == list:
            userinput[i]=userinput[i][::-1]
            reverse(userinput[i])
    return userinput[::-1]

print("""-----------------------------------------------------------------------
                  PATIKA.DEV PYTHON PROJECT
        Actions;
        
        1-Flatten the list //// Default value= [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
        
        2-Reverse the list ////  Default value= [[1, 2], [3, 4], [5, 6, 7]]
        
        Press "q" to exit.
        
      
-----------------------------------------------------------------------
      """)
  
while True:
    action=(input("Select the action you want to do:"))
    if action == "1" :
        print(flatten())
    if action == "2" :
        print(reverse())
    if action == "q" :
        break
