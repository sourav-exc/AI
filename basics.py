def greet():
    print("hii")
    print("This is AI Agent Workshop")

def takeInput():
    userInput = input("Enter your Symptom : ")
    print(userInput)
    return userInput

class Agent:
    def __init__(self, name):
        self.name = name

    def giveAdvice(self, symptom):
        if symptom == "cough":
            print("take xyz medicine")
        elif symptom == "fever":
            print("visit Doctor")
        else:
            print("You are thinking too much!")

greet()

name = "Ayush"
age = 25

symptomList = [{
    "name" : "cough",
    "severity" : "mild",
    "duration" : "2 days",
    "priority" : 1
},
{
    "name" : "fever",
    "severity" : "high",
    "duration" : "5 days",
    "priority" : 2
},
{
    "name" : "Headache",
    "severity" : "low",
    "duration" : "1 days",
    "priority" : 2
}]

symptom = takeInput()

agent = Agent("HealthBot1.0")
agent.giveAdvice(symptom)

print("Thank you for using our bot")
    