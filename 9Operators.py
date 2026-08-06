#operators :- Operators are used in pyton to perform operations on varaibles and values . Python has the following Operators
#1.	Arithmetic Operators
#2.	Comparison (Relational) Operators
#3.	Logical Operators
#4.	Bitwise Operators
#5.	Assignment Operators
#6.	Identity Operators
#7.	Membership Operators

#Arithmetic Operators
x = 5
y = 2
print(x+y)        #addition
print(x-y)        #substraction
print(x/y)        #divsion
print(x*y)        #multiplication
print(x**y)       #power x to the power y
print(x//y)       #integer division gies the Quotient


#2.	Comparison (Relational) Operators
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
print(x == y)
print(x != y)

#Logical Operators
x  = True
y = False
print(x and y)
print(x or y)
print(not y)


#Bitwise Operators
a =  2
b = 3
print(a & b)    #010 & 110 = 010   bitwise AND
print(a | b)    #010 | 110 = 110    Bitwie OR
print( a >> 2)  #010 >> 2 = 000     Right Shift
print(b << 3)   #110 << 3 =110000   Left Shift
print(~a)       #1's complement   Bitwise NOT converts 0 into 1 and 1 into 0 eg  x = -(x + 1)
print(a ^ b)    #Bitwise XOR


#5.	Assignment Operators
c = 3
print(c)

c+=2
print(c)

c -= 1
print(c)      #everytime c value is updated


c *= 2
print(c)

c &= 3
print(c)

#in python we can't use a++ or a-- we have to use like a += 1 or a -= 1



#6.	Identity Operators
#it is used to if two variables are present at the same memory location or not 
d = 4
e = 4
print(d is e)

f = "Hello"
g = "Hello"
print( f is g)

h = [1,2,3]
i = [1,2,3]
print(h is i)

j = "Hello-world"
h = "Hello-World"
print(j is h)

k = 257
l = 257
print(k is  l)
print(id(k), id(l))



#7.	Membership Operators
#it checks if the given character/value is present in the sequence 
m = "delhi"
print("d" in m)
print("d" not in m)

h = [1,2,3]
print(1 in h)
print(5 not in h)

