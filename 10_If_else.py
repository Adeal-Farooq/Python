#correct email = campusx@gmail.com
#pssword = 1234

email = input("Enter your E-mail : ")
if '@' in email:
  password = input("Enter your password : ")

  if email == "campusx@gmail.com" and password == "1234":
    print("Welcome")
  elif email == "campusx@gmail.com" and password != "1234":
    print("Password incorrect")
    password = input("Enter passsword again : ")

    if password == "1234":
      print("finally Correct")
    else:
      print("still incorrect")
  else:
    print("incorrect Credentials")

else:
  print("Email format not correct")



#there is the format  of if else we can also use that i:e val1 if cond else val2
#age =20
#status = "Adult" if age >= 18 else "Minor"
#print(status)  
