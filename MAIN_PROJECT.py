'''Paper= 1
rock = 0
scissors = -1'''
 
#  ROCK PAPER SCISSORS GAME CODE

import random
def swg(computer,youstr):
    
    youdict={"p":1,"r":0,"s":-1}
    if youstr not in youdict:
        print("Invalid entry")
        exit()
    you=youdict[youstr]
    reversedict={1:"📄",0:"🪨",-1:"✂️"}

    print(f"\nYou chose: {reversedict[you]}\n\nComputer chose: {reversedict[computer]}\n\n")

    if computer==you:
        print("It's a draw !\n")
        return "draw"

    else:
        if computer==1 and you==0:
            print("You lost!\n")
            return "loss"
        elif computer==1 and you==-1:
            print("You won!\n")
            return "win"
        elif computer==0 and you==1:
            print("You won!\n")
            return "win"
        elif computer==0 and you==-1:
            print("You lost!\n")
            return "loss"
        elif computer==-1 and you==0:
            print("You won!\n")
            return "win"
        elif computer==-1 and you==1:
            print("You lost!\n")
            return "loss"
        else:
            print("Something went wrong!!!\n")

print("BIT BY BIT STUDIOS presents:\n\nTHE ROCK 🪨 PAPER📄 SCISSORS✂️  GAME!!!!\n")
name=input("Enter your name: ")
print("Welcome to THE ROCK 🪨   PAPER📄   SCISSORS ✂️   GAME ",name)
        

def playgame():
   while True:
      try:
         choose=int(input("\nChoose number of rounds [1,2,3]: "))
         if choose in [1,2,3]:
            break
         else:
            print("❌ Invalid number. Please enter 1, 2, or 3.")

      except ValueError:
         print("❌ Invalid entry. Please enter a number like 1, 2, or 3.")

   print("\n\n")

   if choose==1:
         wins=0
         losses=0
         draws=0
         print("Round 1: \n")
         a=swg(random.choice([1,0,-1]),input("Enter your choice: ").lower())
         
         if a=="win":
            wins+=1
         elif a=="loss":
            losses+=1
         elif a=="draw":
            draws+=1

         print(f"wins: {wins}   losses: {losses}   draws:{draws}")
          
         if wins>losses:
             print("You Won!🥳🎉\n\nGame over\nThank-you🙏")
         elif losses>wins:
             print("You Lost!😢💔\n\nGame over\nThank-you🙏")
         elif losses==wins:
             print("It's a Draw🤝\n\nGame over\nThank-you🙏")


   if choose==2:
       wins=0
       losses=0
       draws=0
       print("Round 1: \n")
       a=swg(random.choice([1,0,-1]),input("Enter your choice: ").lower())
       if a=="win":
          wins+=1
       elif a=="loss":
          losses+=1
       elif a=="draw":
          draws+=1

       print("Round 2: \n")
       b=swg(random.choice([1,0,-1]),input("Enter your choice: ").lower())

       if b=="win":
          wins+=1
       elif b=="loss":
          losses+=1
       elif b=="draw":
          draws+=1

       print(f"wins: {wins}   losses: {losses}   draws: {draws}")

       if wins>losses:
          print("You Won!🥳🎉\n\nGame over\nThank-you🙏")
       elif losses>wins:
          print("You Lost😢💔\n\nGame over\nThank-you🙏")
       elif losses==wins:
          print("It's a Draw🤝\n\nGame over\nThank-you🙏")

    
   if choose==3:
       wins=0
       losses=0
       draws=0
       print("Round 1: \n")
       a=swg(random.choice([1,0,-1]),input("Enter your choice: ").lower())
       if a=="win":
          wins+=1
       elif a=="loss":
          losses+=1
       elif a=="draw":
          draws+=1
        
       print("Round 2: \n")
       b=swg(random.choice([1,0,-1]),input("Enter your choice: ").lower())
       if b=="win":
          wins+=1
       elif b=="loss":
          losses+=1
       elif b=="draw":
          draws+=1

       print("Round 3: \n")
       c=swg(random.choice([1,0,-1]),input("Enter your choice: ").lower())
       if c=="win":
          wins+=1
       elif c=="loss":
          losses+=1
       elif c=="draw":
          draws+=1

       print(f"wins: {wins}   losses: {losses}   draws: {draws}")
       
       if wins>losses:
          if wins==3:
             print("Its a hat-trick!🎩🏆🏆🏆\n\nYOU ARE A CHAMPION!!💪🔥")
          else:
             print("You won🥳🎉\n\nGame over!!\nThank-you🙏")

       elif losses>wins:
          if losses==3:
             print("You lost!!😞  Don't worry U CAN DO IT!!✨🙌")
          else:
             print("You lost😢💔\n\nGame over!!\nThank-you🙏")

       elif wins==losses:
          print("Its a draw🤝\n\nGame over!!\nThank-you🙏")

while True:
    playgame()
    choice = input("\n🔁 Type [re] to play again or [qi] to quit: ").lower()
    if choice == "re":
       continue
    elif choice == "qi":
      print("👋 Thanks for playing! See you next time.")
      break
    else:
        print("Invalid input. Exiting.")
        break
