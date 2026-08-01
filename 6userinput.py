#in python it is simpe to take input from the user  , just type input()

input() #when we run this program we will see that the compiler will tell the user to enter the input 
# but user my get confused what kind of input i should write like name . number , or email etc
#so comes prompt which we will write in the parenthesis in the input command to let the user know what he has to enter
input("Enter your name")

#we can store this input into some identifier , like shown below
name = input("enter your full name")

#adding two numbers
first_num = input ("Enter the first number")
second_num  = input("Enter the second number")

result = first_num + second_num
print(result)

#as we see in the results addition is not done , instead of that they are just concatinated like strings
#so we got that whatever input we send by the user will be send as string to the programmer
#so we use TYPE CONVERSION to change the input type so that we can easily operate on them 

#we can check the datatype of thing by type() function

type(3)
type('adeal')
type (True)