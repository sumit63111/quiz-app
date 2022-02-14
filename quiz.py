print("Welcome to my Computer quiz! ")

playing=input("Do you wannt to play👋 ")
score=0

if playing !="yes":
    quit()
print("okay! Lets play 😀") 

answer= input("What does CPU Stands for❓ ")
if answer.lower() =="central processing unit":
    print("correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("What Does GPU Stand for❓ ")
if answer.lower()=='graphics processing unit':
    print("correct!👍")
    score+=1
else:
    print("Incorrect!👎")
    print(score,"out of 7")

answer=input("What Does RAM Stand for❓ ")
if answer.lower()=='random access memory':
    print("correct!👍")
    score+=1
else:
    print("Incorrect!👎")
    print(score,"out of 7")

answer=input("When was the first computer invented❓ ")
if answer.lower()=='1943':
    print("correct!👍")
    score+=1
else:
    print("Incorrect!👎")
    print(score,"out of 7")

answer=input("Who is known as the father of computers❓")
if answer.lower()=='charles babbage':
     print("correct!👍")
     score+=1
else:
    print("Incorrect!👎")
    print(score,"out of 7")

answer=input("What was the first computer system that used color display❓ ")
if answer.lower()=='apple1':
    print("correct!👍")
    score+=1
else:
    print("Incorrect!👎")
    print(score,"out of 7")

answer=input("What was the first mass-produced computer❓ ")
if answer.lower()=='ibm650':
    print("correct!👍")
    score+=1
    print(score,"out of 7")
    print("you done it👋👋👋👋👋👋👋!")
else:
    print("Incorrect!👎")
    print(score,"out of 7")





    
