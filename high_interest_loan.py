user_principle: float = float(input("How much is the principle amount of your loan?"))
def get_user_apr() -> float:
    u_apr: float = float(input("How much is your APR? Use a percentage without a symbol."))
    return u_apr
user_apr = get_user_apr()
print('Your interest rate is {}%.'.format(user_apr))

def get_user_daily_interest() -> float:
    user_daily_interest: float = 2 * user_principle * (user_apr / 365 / 100)
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
pay_check_cost: float = round(get_pay_check_cost(),2)


def get_paycheck_percentage():
    user_pay_check_amount = float(input("How much do you get paid every pay period?"))
    pay_check_percentage1: float = pay_check_cost / user_pay_check_amount * 100
    return round(pay_check_percentage1,2)
pay_check_percentage = get_paycheck_percentage()


print('Your pay period is {} days long'.format(user_pay_period))
print('You are spending approximately ${} per pay-check on this loan'.format(pay_check_cost))
print('Your high-interest loan will eat up %{} of your paycheck this pay period.'.format(pay_check_percentage))
