class Product(object):
	def __init__(self, price, item_name, weight, brand, status):
		self.price = price
		self.item_name = item_name
		self.weight = weight
		self.brand = brand
		self.cost = 0
		self.status = "for sale"

	def sell(self):
		self.status = "sold"
		return self
	def reason(self, reason):
		if reason == "defective":
			self.status = "defective"
			self.price = 0
		if reason == "in-box":
			self.status = "for sale"
		if reason == "out-of-box":
			self.status = "used"
			self.price = (self.price - (self.price * .2))
		return self
	def add_tax(self, tax):
		self.cost = (self.price + (self.price * tax))
		return self
	def display_info(self):
		print "Price:", self.price
		print "Item:", self.item_name
		print "Weight:", self.weight
		print "Brand:", self.brand
		print "Cost after tax:", self.cost
		print "Status:", self.status
		return self

product1 = Product(100, "game", "1lb", "Nintendo", "returned")

product1.sell().reason("out-of-box").add_tax(0.08).display_info()

