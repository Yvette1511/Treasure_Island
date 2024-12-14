import time

print("Welcome to Treasure Island!")
time.sleep(1.5)
print("You find a crossroad.")
time.sleep(1.5)
direction = input("Would you like to go left or right?: ").lower()
time.sleep(0.5)
if direction != "left":
    print("You fell into a hole! Game Over!")
else:
    print("You went the right way! You come across a river.")
    time.sleep(1.5)
    swim_wait = input("Will you swim or wait?: ").lower()
    time.sleep(0.5)
    if swim_wait != "wait":
        print("You got attacked by trout. Game Over!")
    else:
        print("Whilst you waited, you saw another way across. At the other end, you see 3 doors.")
        time.sleep(1.5)
        door = input("Do you want to go through door red, blue or yellow?: ").lower()
        time.sleep(0.5)
        if door == "red":
            print("You got burned. Game Over!")
        elif door == "blue":
            print("You got eaten by beasts. Game Over!")
        elif door == "yellow":
            print("Congratulations, you found the treasure!")
        else:
            print("Game Over!")

time.sleep(1.5)
print(" ")
print("Thanks for playing!")
time.sleep(1)


