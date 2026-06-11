import random

random_number = random.randint(1, 100)

while True:
    guess = int(input("Zgadnij liczbe: "))

    if guess < random_number:
        print("za malo")
    elif guess > random_number:
        print("za duzo")
    else:
        print("udalo ci sie!")
        break