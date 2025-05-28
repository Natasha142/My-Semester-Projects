#Evil Marriage Counselor
#Init
couplesBroken = 0
degrees = 0
numCouples = 0
#Functions
def EvilMarriageCounselor():
   global couplesBroken
   global degrees
   print("Welcome, Evil Marriage Counselor!")
   print("Your parents, ")
   parent1 = input("Name of parent 1: ")
   parent2 = input("Name of parent 2: ")
   print (parent1 + " and " + parent2 + ", broke up when you were a teen, and your spouse, ")
   spouse = input("Name of spouse: ")
   print(spouse + ", divorced you. As revenge, you are trying to get a psychology degree and break up as many couples as you can.")
   print("If you can't be happy, no one can!")
   print("Welcome to college. It's your second day of class and you already have a test tomorrow. Do you want to: ")
   study = input("Study (S) or Party (P)?")
   if study.upper() == "S":
       print ("Congrats! You passed your test. This bodes well for your future: you continue to pass all of your tests and make it to graduation.")
       degrees = degrees + 1
       print ("You now have " + str(degrees) + " degree(s).")
       backToSchool = input("Do you want to go back to school for your master's (MA), or quit and try to get a job (J)?")
       if backToSchool.upper() == "MA":
           degrees = degrees + 1
           print("Congrats! You now have " + str(degrees) + " degrees! It's time to get working. You get hired! How many couples do you want to take on?")
           global numCouples
           numCouples = input("1-3")
           for i in range(int(numCouples)):
               help = input("Do you want to help (H) or break up (B) the couple?")
               if help.upper() == "H":
                   print ("You helped the couple work it out! They stayed together. You see the value of your profession and decide to stop your mission for evil.")
                   break
               elif help.upper() == "B":
                   couplesBroken = couplesBroken + 1
                   print("You broke up " + str(couplesBroken) + " couple(s)!")
           if help.upper() == "B":
               print("You find happiness in this revenge for a while, but start to realize that you are still not fulfilled.")
               print("You continue to break up couples until you meet your match. No matter what you do, this couple seems to only get stronger the harder you try to break them up.")
               print("You help them fix their marriage, much to your chagrin. Surprisingly, you like the feeling of helping. You decide to give up your vendetta for good.")
       elif backToSchool.upper() == "J":
           print("Despite the odds, you got a job!")
           for i in range(3):
               help = input("Do you want to help (H) or break up (B) the couple?")
               if help.upper() == "H":
                   print("You helped the couple work it out! They stayed together. You see the value of your profession and decide to stop your mission for evil.")
                   break
               elif help.upper() == "B":
                   couplesBroken = couplesBroken + 1
                   print("You broke up " + str(couplesBroken) + " couple(s)!")
           if help.upper() == "B":
               print("You find happiness in this revenge for a while, but start to realize that you are still not fulfilled.")
               print("You continue to break up couples until you meet your match.")
               print("No matter what you do, this couple seems to only get stronger the harder you try to break them up.")
               print("You help them fix their marriage, much to your chagrin. Surprisingly, you like the feeling of helping. You decide to give up your vendetta for good.")
   elif study.upper() == "P":
       print ("Uh oh, you failed your test and your academic advisor called you to her office. Do you")
       advisor = input("go (G), or party again instead(P)?")
       if advisor.upper() == "G":
           print("You go to her office expecting to be told off, but you are surprised to find her smiling.")
           print("She tells you that she knows of your secret plan for evil, and wants to invite you to train for the guild of evil marrriage counselors. Do you")
           accept = input("accept her offer (A) or realize your plan for evil is wrong and decline (D)?")
           if accept.upper == "A":
               print("You accept! After graduation, you start your job.")
               for i in range(3):
                   help = input("Do you want to help (H) or break up (B) the couple?")
                   if help.upper() == "H":
                       print("You helped the couple work it out! They stayed together. You see the value of your profession and decide to stop your mission for evil.")
                       print("Unfortunately, your old academic advisor tracks you down and poisons your tea. You knew too much.")
                       break
                   elif help.upper() == "B":
                       couplesBroken = couplesBroken + 1
                       print("You broke up " + str(couplesBroken) + " couple(s)!")
               if help.upper() == "B":
                   print("You continue on this path for revenge for some time, earning the approval of the other members of your guild. Still, you feel unfulfilled.")
                   print("One day, you march into your old academic advisor's office and announce that you are quitting.")
                   print("As you walk out of her building, a nondescript black van races around the corner and runs you over. You knew too much.")
           if accept.upper == "D":
               print("You decline. You realize that you should help people and give up your vendetta. As you walk out of the buidling, a nondescript black van races around the corner and runs you over. You knew too much.")
       elif advisor.upper() == "P":
           print("You party again but realize that this was the wrong choice. You get your life together and graduate bottom of your class.")
           degrees = degrees + 1
           print("You now have " + str(degrees) + " degree(s). Congrats!")
           print("Unfortunately, your academic advisor turned out to be the leader of the guild of evil marriage counselors and on the day of your graduation, she throws you off a bridge and you die.")


#Main
EvilMarriageCounselor()
