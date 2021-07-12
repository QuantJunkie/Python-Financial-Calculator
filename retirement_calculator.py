class RetirementCalculator:
    def __init__(self, retirement_target, compounding_periods,
        annual_interest_rate):
        self.retirement_target = retirement_target
        self.compounding_periods = compounding_periods
        self.annual_interest_rate = annual_interest_rate
        
    def calculate_monthly_payment(self):
        monthly_payment = ((self.retirement_target * self.annual_interest_rate/12)/
                           (((1 + self.annual_interest_rate/12) ** self.compounding_periods) -1))
        return monthly_payment


