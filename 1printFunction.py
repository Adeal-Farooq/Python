print ("Hello World ")
print ("hi")
print(True)
print("6")
print (6)
print (5.6)
print(False)
# print (false)       false and False are different
print("india", "pakistan", "nepal")   #as we see in this pprint function the output has spaces between them , so we got in python spaces are printed by default by the parameter sep (we can change it )
print("india", 5 , True)
print("india", "pakistan", "nepal", sep = '/')    #we changed the sep parameter by / so now the default value which is space gets replaces by / , as we see in the output
print("india", "pakistan", "nepal", sep = '-')  # same in this case the space is replaced here by - 

#there is also another thing in print function that is end parameter , anf by default it id \n which MEANS next line , we can also change thid parameter as shown below
print("hello")
print ("world")#these two print functions will be printed in two different lines as end parameter is not defined 


print("hello", end = " ")
print("world") # these teo print functionds will be printed in same line as end parameter is defined by " " i;e space here 


print("hello", end = "-")
print("world") #here end parameter is defimned by - 

