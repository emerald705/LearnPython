number = 3
guess=int(input("Enter a number:"))
if number == guess:
    print ("GOOD! You Are Smart!")
elif guess > number:
    print ("Your Number is larger.")
else:
    print ("Your Number is smaller.")
