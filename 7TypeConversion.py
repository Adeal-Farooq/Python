 #TypeCasting -- converting one dtatype into other datatype , which are CONVERTABLE 
#we can not convert kolkata which is a string into integer , so we should be aware of these kind of things
#so string is the universal datatype we can store any kind of data type into string type .. but can not store sting into ny other data type .. as shown by the above example of kolkata.. which can not be stored as integer or anyother dats type

#two types of typeconversion 1) implicit   2) explicit
#implicit :- when python does typeconversion by itself , so as a programmer we dont have to  tell to convert
#explicit :- in this TypeConversion we have to tell python that we have to convert data this time i;e we have to do TypeConversion 

4 + 5.5     #implicit .. python khud se in dono p add karega .. khud behind the scenes typeconversion karega

5 + 6+7j
4.5 + 5+5j

#but in certain scenarios phthon can't do this by itself .. so  programmer has to explicitly tell to do typeConversion

first_num = input("enter the first number :")
second_num = input("Enter the second number :")

result = first_num + second_num
print(result)

#as we see in the above example no implicit TypeConversion will happen so we have to do explicitly Typeconversion
#e;g we can use int .. it can chage any compatible dattype into integer
int(4.5)
int('2')

float(4)

str(5)

bool(1)
complex(4)
list('hello')

#we can don like this like int('kolkata')


a = 4.5
int(a)  #output will be 4 , which is integer

#but if we will print a again it will print 4.5, so we get that int(a) does not change the original value of a  but it creates a another interger and prints that .. so there is no effect ion original value of a

first_num = input("enter the first number :")
second_num = input("Enter the second number :")

result = int(first_num) + int(second_num)
print(result)           #this will give the correct result


#but it would be best when you take the input from the user and only at that time you apply the typeconversion
first_num = int(input("enter the first number :"))
second_num = int(input("Enter the second number :"))

result = first_num + second_num
print(result)
