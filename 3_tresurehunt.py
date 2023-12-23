print("Welcome to Tressure Hunt game!")
print("Your mission is to find the Tressure and win!")
choice1=input('You are at a crossroad. Where do you want to go? type "left" or "right".').lower()
if choice1 == "left":
    choice2 = input('You have reached a lake. There is an island in middile of lake. Type "wait" to wait for a boat or "swim" to reach the island.').lower()
    if choice2 == "wait":
        choice3 = input('You have reached the island. There are 3 doors to enter the island. One red, one yellow and one purple. Which color do you choose? "red","yellow","purple".').lower()
        if choice3 == "red":
            print("This room is full of fire. Game over -_-")
        elif choice3 == "yellow":
            print("This room is full of water. Game over -_-")
        elif choice3 == "purple":
            print("Yahoo! You have reached the Tressure hunt. Congratulations!!")
        else:
            print("you have entered a wrong door that doesnot exist.")
    else:
        print("You got attacked by a crocodile. Game over -_-")
else:
    print("You met with an accident. Game over -_- ")
