import sys
import os
# Initialize User Interface
print("This program will ask you a few basic questions about your credit line in order to show you the real impact of your interest rates and spending habits.")
statementBalancesString: str = input("Please enter a list of 3 or more of your most recent statement balances. ")
statementBalances = []
cardName = input("Please enter your card name (e.g. Mastercard). ")
# Figure out user's spending limit
spendingLimit = float(input("What is your card's spending limit in dollars? "))
# Function for terminal's user interface
def apr():
    percentage = input("What is your current annual APR? ")
    decimalString = percentage
    float1 = float(decimalString)
    return float1
# Function that determines your average utilization using prior statements
def avg_utilization():
    for i in statementBalancesString.split(','):
        statementBalances.append(float(i))
    avgStatementBalance: float = (sum(statementBalances) / len(statementBalances))
    avg_utilization1 = avgStatementBalance/spendingLimit
    return avg_utilization1
def count_statements():
    return len(statementBalances)
# Assign variables to value of function calls
user_apr = apr()
user_avg_utilization = avg_utilization()
# Change these values depending on the credit card's factors
class CreditAccount:
    def __init__(self, cardName, user_apr, user_avg_utilization, spendingLimit):
        self.cardName = cardName
        self.user_apr = user_apr
        self.user_avg_utilization = user_avg_utilization
        self.spendingLimit = spendingLimit
# Create and store instance of user's individual card line
creditAccount_1 = CreditAccount(cardName, user_apr, user_avg_utilization, spendingLimit)
#This function will display and ask for confirmation regarding user's individual credit card line. If the
#information was correct, the components are cleared to be used in the next python script: "RealInterestCosts.py"
def confirmation():
    print("Reviewing your credit line information...")
    print("Credit Card Name: %s" % cardName)
    print("Spending Limit: %d" % spendingLimit)
    print("Your APR: %d" % user_apr)
    confirmation_answer = input("Is this information correct? (Answer y or n)")
    if confirmation_answer == "y" or "Y":
        boolean_answer = True
    else:
        boolean_answer = False
    if boolean_answer is False:
        print("Restarting shell..")
        restart_program()
    else:
        print("Your information will now be used to calculate certain information about your interest costs.")
    return boolean_answer
# Determine the quality of your utilization rate
def get_utilization_score(user_avg_utilization):
    global utilization_score
    if user_avg_utilization > 0.60:
        utilization_score = "poor"
    elif user_avg_utilization <= 0.60:
        utilization_score = "average"
    elif user_avg_utilization <= 0.30:
        utilization_score = "good"
    elif user_avg_utilization <= 0.10:
        utilization_score = "excellent"
    return utilization_score
def restart_program():
    #Restarts the current program. Note: this function does not return. Any cleanup action (like
    #saving data) must be done before calling this function.
    python = sys.executable
    os.execl(python, python, * sys.argv)
confirmation()
# basic apparatus that customizes rating display
message = "Your average utilization rate is"
message2 = "percent "
def message3function():
    if get_utilization_score(user_avg_utilization) == "excellent":
        message3var = "(excellent)."
    elif get_utilization_score(user_avg_utilization) == "good":
        message3var = "(good)."
    elif get_utilization_score(user_avg_utilization) == "average":
        message3var = "(average)."
    elif get_utilization_score(user_avg_utilization) == "poor":
        message3var = "(poor)."
    return message3var
message3 = message3function()
# display the custom rating and message about utilization
print(message, round((100*user_avg_utilization), 2), message2, message3)
# Interest related functions
class Interest:
    @staticmethod
    def display():
        monthly_apr = user_apr / 12
        monthly_interest = round((monthly_apr * (user_avg_utilization * spendingLimit) / 100) , 2)
        monthly_interest_string = str(monthly_interest)
        message4 = "If you maintain these spending habits, you will be spending approximately"
        message5 = monthly_interest_string
        message6 = "dollars per month on interest alone."
        count_statements_string = str(count_statements())
        message7_math = str(monthly_interest * count_statements())
        message7 = 'This also means you have spent approximately {} dollars on interest in the past {} months for your {} card.'.format(message7_math, count_statements_string, cardName)
        print(message4, message5, message6, message7)
Interest.display()
