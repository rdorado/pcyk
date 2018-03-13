import sys
import re
import math

class Grammar:

	def __init__(self):
		self.rules = {}
		self.terminals = {}
		self.backrule = {}

	def addRule(self, left_side, right_side):
		try:
			self.rules[left_side].append(right_side)
		except KeyError:
			self.rules[left_side] = [right_side]
		try:
			self.backrule[tuple(right_side)].append(left_side)
		except KeyError:
			self.backrule[tuple(right_side)] = [left_side]
		
	def addTerminal(self, left_side, right_side):
		try:
			self.terminals[right_side].append(left_side)
		except KeyError:
			self.terminals[right_side] = [left_side]		

	def print(self):
		print(self.rules)
		print(self.terminals)
		print(self.backrule)
		
	def getTerminalRules(self, terminal):
		resp = ["OOV"]
		try:
			resp = self.terminals[terminal]
		except KeyError: pass 		
		return resp

	def getSymbolFromRule(self, rule):
		resp = []
		try:
			resp = self.backrule[tuple(rule)]
                        
		except KeyError: pass
			
		return resp


def table_print(table):
	for row in table:
		line = ""
		for col in row:
			line+=str(col)+"\t"
		print(line)

def cky(grammar, sentence, debug=False):
	n = len(sentence)
	table = [[[] for i in range(n-j)] for j in range(n)]
	unaries = [[{} for i in range(n-j)] for j in range(n)]
	nodes_back = [[[] for i in range(n + 1)] for j in range(n + 1)]

	#Initialize table
	for w in range(1, n + 1):
		symbols = grammar.getTerminalRules(sentence[w-1])
		table[0][w-1].extend( symbols )
                # Add unaries 
		for S in symbols:
			rules = grammar.getSymbolFromRule([S])
			for U in rules:
				if S not in unaries[0][w-1] and U not in table[0][w-1]:
					table[0][w-1].append(U)
					unaries[0][w-1][U] = True
	

	if debug: table_print(table)
	for l in range(0, n-1):
		for s in range(n-l-1):
			for p in range(l+1):
				for X in table[p][s]:
					for Y in table[l-p][s+p+1]:
						symbols = grammar.getSymbolFromRule([X, Y])
						table[l+1][s].extend(symbols)

                				# Add unaries 
						for S in symbols:
							rules = grammar.getSymbolFromRule([S])
							for U in rules:			
								if U not in unaries[l+1][s] and U not in table[l+1][s]:
									table[l+1][s].append(U)
									unaries[l+1][s][U] = True
		if debug:
			print()				
			table_print(table)

	return table[0][n-1]

'''
def printParseTrees(nodes_back):

	check = False
	for node in nodes_back:
		if node.root == 'TOP':
			print(getParseTree(node, 5))
			check = True

	if not check:
		print('The given sentence is not valid according to the grammar.')

def getParseTree(root, indent):
	"""
	getParseTree() takes a root and constructs the tree in the form of a
	string. Right and left subtrees are indented equally, providing for
	a nice display.

	@params: root node and an indent factor (int).
	@return: tree, starting at the root provided, in the form of a string.
	"""
	if root.status:
		return '(' + root.root + ' ' + root.terminal + ')'

	# Calculates the new indent factors that we need to pass forward.
	new1 = indent + 2 + len(root.left.root) #len(tree[1][0])
	new2 = indent + 2 + len(root.right.root) #len(tree[2][0])
	left = getParseTree(root.left, new1)
	right = getParseTree(root.right, new2)
	return '(' + root.root + ' ' + left + '\n' \
			+ ' '*indent + right + ')'

'''
def load_grammar(grammar_filename):
	grammar = Grammar()
	pattern = re.compile(".+->.+( .+)?")
	
	nline = 0
	with open(sys.argv[1], 'r') as f:
		lines = f.readlines()
		for line in grammar_text:
			nline+=1
			line = line.strip()
			if len(line) == 0 or line[0] == '#' : continue
			if not pattern.match(line):
				raise ValueError("Error reading grammar on file '"+grammar_filename+"' line "+nline)
				
			rule = [x.strip() for x in line.split('->')]
			right_side = rule[1].split()

			if len(right_side) == 1 and right_side[0] == right_side[0].lower():
				grammar.addTerminal(rule[0],right_side[0])	
			else:                        
				grammar.addRule(rule[0], right_side)

	return grammar



def main():
	if len(sys.argv) != 3:
		printError(0)
	elif not os.path.isfile(sys.argv[1]):
		printError(0)

	parse(sys.argv[1], sys.argv[2])


if __name__ == '__main__':
	main()



