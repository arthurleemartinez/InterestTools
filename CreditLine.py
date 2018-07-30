# Initialize User Interface
print "This program will ask you a few basic questions about your credit line "
# Function for terminal's user interface
def APR():
    percentage = raw_input("What is your current annual APR?")
    decimalString = (percentage.strip(["%"])):
    float1 = int(decimalString)
    return float1
# Function that determines your average utilization using prior statements
def AvgUtilization():
    statementBalancesString = raw_input("Please enter a list of 3 or more of your most recent statement balances.")
    statementBalances = map(int, statementBalancesString.split(','))
    avgStatementBalance = sum(statementBalances) / len(statementBalances)
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
creditAccount_1 = CreditAccount("Discover", user_APR, AvgUtilization, spendingLimit)
# Display user's individual card line
print creditAccount_1
