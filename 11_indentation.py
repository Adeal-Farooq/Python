#in other languages we use ; and {} to cdefine a block of code but in pyton we do not use ; and {}, instead we use indentation to specify the block of code
#indentation increases code readability
name = "xyz"
age = 19
gender = "male"
if name == "xyz":
  print("line1")
  print("line2")
  if age == 19:
    print("is adult")
    if gender == "male":
      print("is male")
else:
  print("line3")