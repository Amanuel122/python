import random
for rand_list_int in random.sample(range(0,101) , 10):

  if rand_list_int % 2 == 0 :
    print(str(rand_list_int) + ''+ " is even")
  else:
    if rand_list_int %2 != 0:
     print(str(rand_list_int) + ''+ " is odd")
