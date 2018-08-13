user_principle: float = float(input("How much is the principle amount of your loan?"))
def get_user_apr() -> float:
    u_apr: float = float(input("How much is your APR? Use a percentage without a symbol."))
    return u_apr
user_apr = get_user_apr()
print('Your interest rate is {}%.'.format(user_apr))
def get_user_daily_interest() -> float:
    user_daily_interest: float = user_principle * (user_apr / 365 / 100)
    return user_daily_interest
daily_interest: float = get_user_daily_interest()
print('Your daily interest is ${}.'.format(daily_interest))
