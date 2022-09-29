class interest_rate(object):
	def __init__(self):
		self.rate = 0.0
		self.start_month = 0
		self.end_month = 0
		self.repayment = 0

	def set_rate(self, rate):
		self.rate = rate / 12.0
	
	def set_start_month(self, month):
		self.start_month = month
	
	def set_end_month(self, month):
		self.end_month = month

	def set_repayment(self, amount):
		self.repayment = amount

class mortgage(object):
	def __init__(self):
		self.total_amount = 0
		self.amount_repaid = 0
		self.interest_accrued = 0
		self.rates = []
		self.final_month = 0

	def set_total_amount(self, amount):
		self.total_amount = amount

	def add_rate(self, rate):
		self.rates.append(rate)

	def get_rate_for_month(self, month):
		for r in self.rates:
			start = r.start_month
			end   = r.end_month
			if month >= start and month < end:
				return r

	def calculate(self, verbose):
		i_month = -1
		while self.total_amount > 0:
			i_month += 1
			current_r = self.get_rate_for_month(i_month)
			self.amount_repaid += current_r.repayment
			self.interest_accrued += current_r.rate*self.total_amount
			this_interest = current_r.rate*self.total_amount
			this_excess   = current_r.repayment - this_interest
			self.total_amount -= this_excess
			if verbose:
				print (f"Month {i_month} : {current_r.repayment} : {self.interest_accrued} : {this_excess} : {self.amount_repaid} : {self.total_amount}")
			
		self.final_month = i_month

