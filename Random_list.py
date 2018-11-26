import random 
  
# Function to generate 
# and append them  
# start = starting range, 
# end = ending range 
# num = number of   elements needs to be appended
# my_list= random list
# list_len= Length of random list 
def Random_list(start, end, num): 
    my_list = [] 
  
    for j in range(num): 
        my_list.append(random.randint(start, end)) 

    print("the random list:", my_list)
    list_len=len(my_list)
    n=int(listlen/2)
    if len list_len!=0:
        print("List is not partitionable")
    else:
        print("Split the two equal")
        final=final = [my_list[i * n:(i + 1) * n] for i in range((len(my_list) + n - 1) // n )]

    return final
        
        
              

