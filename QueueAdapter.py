class QueueStack:

	def __init__(self):
		self._storage = list()

	def length(self):
		return len(self._storage)

	def enqueue(self,element):
		self._storage.append(element)

	def dequeue(self):
		if len(self._storage) > 0:
			final = self._storage.pop(0)
		else:
			print('no elements')
			final = None
		return final

	def is_empty(self):
		if len(self._storage) > 0:
			final = True
		else:
			final = False
		return final

	def show(self):
		if len(self._storage) < 0:
			print('This is Empty')
		else:
			print(self._storage)

q = QueueStack()

q.enqueue(10)
q.enqueue(12)
q.enqueue(14)
q.enqueue(16)
q.enqueue(18)
q.enqueue(20)

q.show()

q.enqueue(22)
q.enqueue(24)
q.enqueue(26)
q.enqueue(28)

q.show()

q.enqueue(30)

q.dequeue()
q.dequeue()

q.enqueue(2)


q.show()