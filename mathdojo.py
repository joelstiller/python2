class mathdojo(object):
	def __init__(self):
		self.value = 0

	def add(self, *num):
		for x in num:
			if type(x) == list:
				for y in x:
					self.value += y
			elif type(x) == tuple:
				for y in x:
					self.value += y
			else:
				self.value += x
		return self

	def subtract(self, *num):
		for x in num:
			if type(x) == list:
				for y in x:
					self.value -= y
			elif type(x) == tuple:
				for y in x:
					self.value -= y
			else:
				self.value -= x
		return self

	def result(self):
		print self.value

md = mathdojo()
md.add(2).add(2,5).subtract(3,2).result()

md.value = 0

md.add([1],3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2,[2,3],[1.1,2.3]).result()

md.value = 0

md.add((1,2,3,4,5)).result()