#Literals:- literals is a raw data given ro a variable . in Python there are various types of literals they are as follows:
#Numeric Literals
#String Literals
#Boolean Literals
#Special Literals

#Numeric Literals
a = 0b1010  #binary Literals
b = 100     #Decimal Literal
c = 0o310   #Octal Literal
d = 0x12c   #Hexadecimal Literal

#float Literal
float_1 = 0.5
float_2 = 1.5e2
float_3 = 1.5e-3


#Complex Liteeral
x = 3.14 +3j   #both real and imaginary part 
y = 2.1j       #only imaginary part


print(a,b,c,d)
print(float_1, float_2, float_3)
print(x, x.imag, x.real)
print(y, y.imag, y.real)


#String Literals
string = 'this is python '
strings = "this is python "
char = "C"    
multiline_str = """this is multiline string with more than one line code"""

unicode = u"\U0001f600\U0001F606\U0001F923"    #used to print emoji
raw_str = r"raw \n string"

print(string)
print(strings)
print(multiline_str)
print(unicode)
print(raw_str)

#boolean Literals
f = True + 4
g = False +10

print("f:",f)
print("g:", g)


#specil Literal
h = None
print(h)


#so we can not declare variables directly in python , we have to assign some value to them ... 
#if we want to declare any variable then we can store None in that