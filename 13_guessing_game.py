import random
jackpot = random.randint(1, 100)

number = int(input("Guess the number : "))
counter = 1
while number != jackpot:
  if number < jackpot:
    print("Wrong,  guesss higher")
  else:
    print("Wrong,  Guess lower")

  number = int(input("Guess number again : "))
  counter += 1

print(f"you guessed the number correctly which is {jackpot}")
print(f"you guessed the number in {counter} attempts")