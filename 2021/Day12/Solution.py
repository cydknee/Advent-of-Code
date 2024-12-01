from collections import defaultdict

with open('Input/Day12Test.txt') as file:
	input = [ i.split('-') for i in file.read().splitlines() ]	

edges = defaultdict(list)

def iterate(edges, node):
	stack, visited = [], []
	stack.append(node)

	while len(stack) != 0:
		vertex = stack.pop()
		print(edges[vertex])
		# if vertex == 'end':
		# 	break
		# if vertex not in visited:
		# 	if vertex.islower():
		# 		visited.append(vertex)
		# 	for edge in edges[vertex]:
		# 		stack.append(edge)
	
		# 	print('stack', stack)

for i in input:
	x, y = i
	edges[x].append(y)
	edges[y].append(x)

print(edges)
iterate(edges, 'start')