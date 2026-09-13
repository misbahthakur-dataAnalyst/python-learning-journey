# AI Study Buddy- rule-based chat assistant in python

import datetime
import time

name= input("swagat hai, enter your name:")
presentHour= datetime.datetime.now().hour

if 5<= presentHour <= 11:
    print=("good morning", name)
elif 11<= presentHour <= 17:
    print("good afternoon", name)
elif 17<= presentHour <= 20:
    print("good evening", name)
else:
    print("good night", name)



print("Hi! welcome to your buddy chatBot")
print("you can ask me basic question, type 'bye' to exit from the bot")

# chatbot memory creation [dictionary of responses]

responses= {
    "hello": "hi, welcome. how can i help you?",
    "how are you": "i am very fine. Thank you",
    "who are you": "i am your smart AI chatBOT",
    "motivate me": "keep going. every bug of your project makes you a better developer",
    "happy": "great to hear that",
    "functions kya hotai hai": "ja kar chapter7 pado"
}


# method/function to get response of chatBot


def getResponseBot(userQuestion):
    userQuestion= userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]




    return "i am not able totell that yet. i will learn that soon"
#take user input
while True:
    userInput= input("please ask your question:")
    reply= getResponseBot(userInput)
    print(" Bot response :", reply)


    if"bye" in userInput.lower():
        break
