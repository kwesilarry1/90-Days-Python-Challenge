#Simple age checker to see if a user is eligible for certain service
age = int(input("How old are you?"))
if age >= 18:
    print("Grandpa, You are old enough to drive")
else:
    print("kid, You are not eligible to drive")