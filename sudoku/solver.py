from math import log10
import knight.grid, knight.solver
import classic.grid, classic.solver
import between.grid, between.solver

def score(g, variant, verbose = False):
	'''return the difficulty score for this puzzle.
	the score increases linearly with respect to the hardest type of tactic that has to be used.'''

	g = [[x for x in row] for row in g]
	return solve(g, variant, verbose)

def solve(g, variant, verbose = False):
	'''solve this puzzle.'''

	variant = variant.upper()

	if variant == 'KNIGHT':
		score = knight.score(g, verbose)

	elif variant == 'CLASSIC':
		score = classic.score(g, verbose)

	elif variant == 'BETWEEN':
		score = between.score(g, verbose)

	else:
		raise Exception('unsupported variant')

	return -1 if score <= 0 else round(log10(score), 2)