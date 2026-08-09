#range function
print(list(range(1,11,1)))    #prints [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#range(start, stop, step)
#by default start =1
#by default step =1
#stop we have to give everytime
range(5)  #prints 1-4
range(3,11)  #prints 3-10
range(10, 0, 2)  #prints 10 8 6 4 2
range(1,11,3)   #prints 1,4,7,10

#sequence : list , tuples, sets



for i in range(1,11):
  print(i)


print("for loop for sequence of characters or string")
for i in "kolkata":
  print(i)



print("for loop for  list ... sequence")
for i in [1,2,3,4,5]:
  print(i)

print("for loop for tuples .. sequence")
for i in (1,3 ,5 ,6):
  print(i)

print("for loop for sets  .. sequence ")
for i in {1,3 ,5 ,6}:
  print(i)


#to b yeh smj aaya ki aap for loop k andr koi b range yaan sequence provide karo , for loop us pe iterate karta jayega ,, aur output deta jayega


