
#global variables
welcomeMessage = "Welcome to the tip calculator."
priceMessage = "What was the total on the bill? "
personCountMessage = "How many people are splitting the bill? "
tipMessage = "What percentage tip would you like to add? "

priceErrorMessage = "That didn't look like a number. "
personCountError = "Hmm, that didn't seem to be a valid number of people. "
tipError = "That didn't seem to be a valid number. "

totalMessage = "The total bill including the tip is:"
paymentAmountMessage = "Each person should pay:"
tipAmountIncludedMessage = "This includes the tip:"
finalMessage = "Bai"



def calculateTip(price,tipPercentage):
    total = price * (1 + (tipPercentage/100))
    tipAmount = price * (tipPercentage/100)
    return(total,tipAmount)

def splitBill(price,numberOfPeople):
    pricePerPerson = price / numberOfPeople
    return(pricePerPerson)

def main():
    print(welcomeMessage)

# PRICE INPUT
    while True:
        try:
            price = float(input(priceMessage))
        except ValueError:
            print(priceErrorMessage)
        else:
            break


# PERSON INPUT
    while True:
        try:
            personCount = int(input(personCountMessage))
        except ValueError:
            print(personCountError)
        else:
            break

# TIP INPUT
    while True:
        try:
            tipPercentage = float(input(tipMessage))
        except ValueError:
            print(tipError)
        else:
            break

    total,tipAmount = calculateTip(price,tipPercentage)
    totalPerPerson = splitBill(total,personCount) #the amount each person has to pay
    tipPaidPerPerson = splitBill(tipAmount,personCount) #how much each person contributed to the tip (just an FYI)
    print(totalMessage, round(total,2))
    print(paymentAmountMessage,round(totalPerPerson,2),tipAmountIncludedMessage,round(tipPaidPerPerson,2)) #Each person should pay: 110.0 This includes the tip: 10.0
    print(finalMessage)

main()

