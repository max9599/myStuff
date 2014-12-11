#
#Programeerimise süvendatud algkursus. Kodune ül. Binary tree
#Autor: Maxim Gromov, mtrkl.nr.:142686
#Dec 2014


class Node:
	'''
		Node class
	'''
	def __init__(self, value, count, left = None, right = None):
		self.value = value
		self.count = count
		self.left = left
		self.right = right

	def insert(self, value, count):
		'''
			Insert values in abc order (recursive)
		'''
		if value < self.value:
			if self.left is None:
				self.left = Node(value, count)
			else:
				self.left.insert(value, count)
		elif value > self.value:
			if self.right is None:
				self.right = Node(value, count)
			else:
				self.right.insert(value, count)

	def maxDepth(self):
		'''
			Returns max depth of binary tree
		'''
		if self.left == self.right == None:
			return 1
		elif self.left == None:
			return max(0, self.right.maxDepth()) + 1
		elif self.right == None:
			return max(self.left.maxDepth(), 0) + 1
		else:
			return max(self.left.maxDepth(), self.right.maxDepth()) + 1

	def minValue(self):
		'''
			Return word and count with min value (first in abc)
		'''
		while self.left != None:
			return self.left.minValue()
		return {self.value : self.count}

	def search(self, word, depth = 0):
		'''
			args: word value
			return: information: if found - word, count, depth where found
								 if not found - notification, that not found
		'''
		if self.value == word:
			print('Founded: ' + 'depth: ' + str(depth) + '; word: ' + self.value + '; count: ' + str(self.count) + ';')
		else:
			depth += 1
			if self.value > word and self.left is not None:
				self.left.search(word, depth)
			elif self.value < word and self.right is not None:
				self.right.search(word, depth)
			else:
				print('Word ' + word + ' not found!')

 	def print_tree(self):
 		'''
 			prints tree items recursively in abc order
 		'''
		if self.left != None:
			self.left.print_tree()
		print({self.value:self.count})
		if self.right != None:
			self.right.print_tree()

def doWords(thefile):
	'''
		arg: file with words
		return: dictionary with words and counts
	'''
	wordNodes = {}
	current_word = ""
	file = open(thefile)
	for symb in "".join([line for line in file]):
		if symb.isalpha():
			current_word += symb
		else:
			if current_word != "":
				current_word = current_word.lower()
				if current_word in wordNodes.keys():
					wordNodes[current_word] += 1
				else:
					wordNodes[current_word] = 1
			current_word = ""
	file.close()

	return wordNodes

def doTree(file):
	'''
		args: file with words
		returns: binary tree with words and counts from file (in abc order)
	'''
	dicty = doWords(file)
	dkeys = dicty.keys()
	root = Node(dkeys[0], dicty[dkeys[0]])

	for word in dicty.keys()[1:]:
		root.insert(word, dicty[word])

	return root

def main():
	'''
		Main
	'''
	tree = doTree('input.txt')
	tree.print_tree()

if __name__ == '__main__':
	main()