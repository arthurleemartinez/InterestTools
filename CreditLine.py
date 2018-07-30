import sys
import os
# Initialize User Interface
print("This program will ask you a few basic questions about your credit line in order to show you the real impact of your interest rates and spending habits.")
statementBalancesString = input("Please enter a list of 3 or more of your most recent statement balances.")
statementBalances = []
cardName = input("Please enter your card name (e.g. Mastercard).")
# Figure out user's spending limit
spendingLimit = float(input("What is your card's spending limit in dollars?"))
# Function for terminal's user interface
def APR():
    percentage = input("What is your current annual APR?")
    decimalString = percentage
    intfloat1 = round(int(float(decimalString)), 2)
    return intfloat1
# Function that determines your average utilization using prior statements
def AvgUtilization():
    statementBalances = []
    for i in statementBalancesString.split(','):
        statementBalances.append(int(i))
    avgStatementBalance = (sum(statementBalances) / len(statementBalances))
    avgutilization1 = avgStatementBalance/spendingLimit
    return avgutilization1
# Assign variables to value of function calls
user_APR = APR()
user_AvgUtilization = AvgUtilization()
# Change these values depending on the credit card's factors
class CreditAccount:
    def __init__(self, cardName, user_APR, user_AvgUtilization, spendingLimit):
        self.cardName = cardName
        self.user_APR = user_APR
        self.user_AvgUtilization = user_AvgUtilization
        self.spendingLimit = spendingLimit
# Create and store instance of user's individual card line
creditAccount_1 = CreditAccount(cardName, user_APR, user_AvgUtilization, spendingLimit)
#This function will display and ask for confirmation regarding user's individual credit card line. If the
#information was correct, the components are cleared to be used in the next python script: "RealInterestCosts.py"
def confirmation():
    print("Reviewing your credit line information...")
    print("Credit Card Name: %s" % cardName)
    print("Spending Limit: %d" % spendingLimit)
    print("Your APR: %d" % user_APR)
    confirmation_answer = input("Is this information correct? (Answer y or n)")
    if confirmation_answer == "y":
        boolean_answer = True
    else:
        boolean_answer = False
    if boolean_answer is False:
        print("Restarting shell..")
        restart_program()
    else:
        print("Your information will now be used to calculate certain information about your interest costs.")
    return boolean_answer
def restart_program():
    #Restarts the current program. Note: this function does not return. Any cleanup action (like
    #saving data) must be done before calling this function.
    python = sys.executable
    os.execl(python, python, * sys.argv)
message = "Your average utilization rate is"
print(message, user_AvgUtilization)
confirmation()
