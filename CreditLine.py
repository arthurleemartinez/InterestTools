# Initialize User Interface
print "This program will ask you a few basic questions about your credit line and will tell you facts about your interest costs"
# Functions for terminal's user interface
def APR():
    percentage = raw_input("What is your current annual APR?")
    decimalString = (percentage.strip(["%"])):
    float1 = int(decimalString)
    return float1
# Assign variable to value of APR() function call
user_APR = APR()
# Tell the user what to type 
# Change these values depending on the credit card's factors
class CreditAccount:
    def __init__(self, cardName, user_APR, AvgUtilization, spendingLimit):
        self.cardName = cardName
        self.user_APR = user_APR
        self.AvgUtilization = AvgUtilization
        self.spendingLimit = spendingLimit
       
Class Statements:
    numberOfMonthlyStatements = 
    n = numberOfMonthytStatements
    
    def _init_(self, 
    # Function that determines your average utilization using prior statements

# Create and store instance of user's individual card line 
creditAccount_1 = CreditAccount("Discover", 24.74%", )
# Display user's individual card line
print creditAccount_1
