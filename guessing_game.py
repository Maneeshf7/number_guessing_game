import random
print("welcome to the number guessing game ")
number=random.randint(1,100)
attempts=0
while True:
    guess=int(input("enter the guess number :"))
    attempts+=1
    if guess > number:
        print("guessed too high ,try again")
    elif guess < number:
        print("guessed too low,try again")
    else:
        print(f"huray,after this many attempts {attempts } you got it right") 
   
    
