from classes import interest_rate, mortgage

# Rates and repayments
rate_1 = interest_rate()
rate_1.set_rate(4.59/100.0)
rate_1.set_start_month(0)
rate_1.set_end_month(12*5)
rate_1.set_repayment(660.81)
rate_2 = interest_rate()
rate_2.set_rate(4.99/100.0)
rate_2.set_start_month(12*5)
rate_2.set_end_month(1000)
rate_2.set_repayment(691.80)

# Mortgage
m = mortgage()
m.set_total_amount(138000)
m.add_rate(rate_1)
m.add_rate(rate_2)

# Options
do_overpayment = (input("Run overpayment calculator [y/n] : ") == "y")
if do_overpayment:
	amount = float(input("Enter amount to pay instead : "))
	for r in m.rates:
		r.set_repayment(amount)

m.calculate(verbose=False)

print (f"Mortgage repaid after {m.final_month} months (approx. {m.final_month/12:.1f} years). Total repaid : {m.amount_repaid:.2f}")