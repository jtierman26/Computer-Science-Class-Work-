class StackAdapter:

	def __init__(self):
		self._storage = list()

	def push(self,e):
		self._storage.append(e)

	def pop(self,x):
		if len(self._storage) > 0:
			leave = self._storage.pop(0)
		else:
			print('This is empty')
			leave = None
		return leave

	def length(self):
		return len(self._storage)

	def top(self):
		if self.is_empty():
			return None
		else:
			return self._storage[-1]

	def is_empty(self):
		if len(self._storage) > 0:
			leave = False
		else:
			leave = True
		return leave

	def show(self):
		if len(self._storage) < 0:
			print('This is Empty')
		else:
			print(self._storage)

s = StackAdapter()
s.push(14)
s.push(12)
s.push(10)
s.push(8)
s.push(6)
s.show()
s.pop(0)
s.pop(0)
s.show()


