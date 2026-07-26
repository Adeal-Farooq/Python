#variables
#variables are the containers for future use
#in languages like c we have to declare what kind of variables we are using like int a = 5 , means integer variable
#but in ython we do not declare variables , compiler itself knows what kind of variables we are using   , i;e no variable decleration
name = 'Adeal'
print(name)

name = 'Hello World'
name = 'Hello'
print (name)

#as we see in the above two print statements ,the name is declared two times , but the compiler will take the variable which we have declared last, so in this print statement it will take hello AS the declared variable 

#python --- dynamic typing , means no variable decleration
#STATIC TYPING ----- variables should be declared 

#as seen in othre languages if we declare the variable as int then we can only store integer i that varisble called  STATIC BINDING , but in python we can store any kind of datatype in variable -----this feature is called DYNAMIC BINDING 

name = 'adeal' 
print (name)
name = 9
print(name)
name = True 
print(name)


#special syntrx 
a=5;b=6;c=3
print(a,b,c)

a,b,c = 4,5,6
print(a,b,c)

a=b=c=2
print (a, b, c)