user_principle: float = float(input("How much is the principle amount of your loan?"))
def get_boolean_user_plans():
    user_answer: str = input("Do you plan to pay off at least some of it soon? Answer 'yes' or 'no'.")
    if user_answer != 'yes' or 'Yes' or 'YES' or 'y' or 'Y':
        return False
    else:
        return True
user_plans:bool = get_boolean_user_plans()
def get_user_apr() -> float:
    u_apr: float = float(input("How much is your APR? Use a percentage without a symbol."))
    return u_apr
user_apr = get_user_apr()
print('Your interest rate is {}%.'.format(user_apr))
def get_user_daily_interest() -> float:
    user_daily_interest: float = user_principle * (user_apr / 365 / 100)
    return user_daily_interest
daily_interest: float = get_user_daily_interest()
print('You are spending ${} on interest every day.'.format(daily_interest))
user_pay_period: int = int(input("How many days long is your pay period?"))
def get_pay_check_cost() -> float:
    weekly_interest_cost = daily_interest * 7
    biweekly_interest_cost = daily_interest * 14
    monthly_interest_cost = daily_interest * 30
    if user_pay_period > 6:
        pay_period_interest_cost = weekly_interest_cost
    elif user_pay_period > 13:
        pay_period_interest_cost = biweekly_interest_cost
    elif monthly_interest_cost > 27:
        pay_period_interest_cost = monthly_interest_cost
    return round(pay_period_interest_cost, 2)

pay_check_cost: float = 2*round(get_pay_check_cost(),2)
user_pay_check_amount = float(input("How much do you get paid every pay period?"))
def get_paycheck_percentage():
    pay_check_percentage1: float = round((pay_check_cost / user_pay_check_amount * 100), 2)
    return pay_check_percentage1
pay_check_percentage = round(get_paycheck_percentage() , 2)
# determine how much money you will save on each minimum payment if you pay down a certain principle amount.
def pay_down_implications():
        payment_more_than_minimum: float = float(str(input("How much do you want to pay toward the principle this pay-check?")))
        new_daily_interest = (user_principle - payment_more_than_minimum)/365/100*user_apr
        new_pay_check_percentage: float = round((100*(new_daily_interest * user_pay_period) / user_pay_check_amount), 2)
        new_pay_check_cost:float = round((new_pay_check_percentage/100*user_pay_check_amount) , 2)
        message = 'If you make a payment of ${} before the next due date, this loan will change to taking up %{} of your pay-checks. This means that your next payment would be ${}'.format(payment_more_than_minimum, new_pay_check_percentage, new_pay_check_cost)
        return message
print('Your pay period is {} days long'.format(user_pay_period))
print('You are spending approximately ${} per pay-check on this loan'.format(pay_check_cost))
print('Your high-interest loan will eat up %{} of your paycheck this pay period.'.format(pay_check_percentage))
print(pay_down_implications())
