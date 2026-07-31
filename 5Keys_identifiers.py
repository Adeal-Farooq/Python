#KEYWORD -- keyword is a word which is  reserved by program because the word has special meaning . there are set of 33 keywords in python 
import keyword
print(keyword.kwlist) 

#we can use keywords as variables 


#IDENTIFIER ---a identifier is a name used to identify a variable , function , class , module, or other object 

#rules for identifiers 
#1. can only start with an alphabet or _
#2. followed by 0 or more letters , _,and digits 
#3. kewords cannot be used as an identifier 

#correct identifiers 
name = 'adeal'
print(name)


_ = "adeal"
_1ade = 'adea;l'
adeal12__ = 'adeal'

#incorrect identifier 
#2 = 'adeal'
#@ = 'adeal'
#-adeal = 'name'
#1name = 'adeal'
#False = 'adeal'

