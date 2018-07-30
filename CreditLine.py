import sys
import os
def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
# Initialize User Interface
print "This program will ask you a few basic questions about your credit line in order to show you the real impact of your interest rates and spending habits."
# Function for terminal's user interface
cardName = raw_input("Please enter your card name (e.g. Mastercard).")
def APR():
    percentage = raw_input("What is your current annual APR?")
    decimalString = (percentage.strip(["%"])):
    float1 = int(decimalString)
    return float1
# Function that determines your average utilization using prior statements
def AvgUtilization():
    statementBalancesString = raw_input("Please enter a list of 3 or more of your most recent statement balances.")
    statementBalances = map(int, statementBalancesString.split(','))
    avgStatementBalance = (sum(statementBalances) / len(statementBalances))
# Assign variable to value of APR() function call
user_APR = APR()
# Figure out user's spending limit
spendingLimit = int(raw_input("What is your spending limit in dollars?"))
# Change these values depending on the credit card's factors
class CreditAccount:
    def __init__(self, cardName, user_APR, AvgUtilization, spendingLimit):
        self.cardName = cardName
        self.user_APR = user_APR
        self.AvgUtilization = AvgUtilization
        self.spendingLimit = spendingLimit
    
# Create and store instance of user's individual card line 
creditAccount_1 = CreditAccount(cardName, user_APR, AvgUtilization, spendingLimit)

"""This function will display and ask for confirmation regarding user's individual credit card line. If the  
   information was correct, the componenets are cleared to be used in the next python script: "RealInterestCosts.py""""
def confirmation(CreditAccount_1):
    print "Reviewing your credit line information..."  
    print "Credit Card Name: %s" % cardName
    print "Spending Limit: %d" % spendingLimit
    print "Your APR: %d" % user_APR
    confirmation_answer = raw_input("Is this information correct? (Answer y or n)")
    if (confirmation_answer == "y"):
        boolean_answer = True
    else:
        boolean_answer = False
    if boolean_answer = False:
        print "Restarting shell.."
        restart_program()
        

if __name__ == "__main__":
    answer = raw_input("Do you want to restart this program ? ")
    if answer.lower().strip() in "y yes".split():
        
        
    
    Your credit line information: creditAccount_1
