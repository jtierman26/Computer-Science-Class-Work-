class Stack:

	def __init__(self, cap = 10 ):
		self._storage = list()
		self._cap = cap
		self._size = 0
		self._top = -1

		x = 0 
		while x < self._cap :
			self._storage.append(None)
			x += 1

	def push(self,e):
		self._top += 1
		if self._top <= (self._cap - 1):
			self._storage[self._top] = e
			self._size += 1
		else:
			print('Cant store element')

	def pop(self, a):
		a = None 
		if self._size == 0:
			print('this is empty')
		else:
			a = self._storage[self._top]
			self._storage[self._top] = None
			self._top -= 1
			self._size -= 1
		return a 

	def top(self):
		if self._size > 0:
			a = self._storage[self._top]
		else:
			a = None

	def is_smpty(self):
		if self._size > 0:
			a = False
		else:
			a = True
		return a

	def length(self):
		return self._size

	def show(self):
		if len(self._storage) < 0:
			print('This is Empty')
		else:
			print(self._storage)


s = Stack(10)

s.push(14)
s.push(12)
s.push(10)
s.push(8)
s.push(6)
s.push(4)
s.push(2)
s.push(1)
s.push(-1)

s.show()

s.pop(0)

s.show()