# Task:
# Determine if one replacement is enough to make strings are equal.

test_case = [['cat', 'cat'], ['cat', 'cut'], ['cat', 'cutt'], ['caaat', 'cat'], ['cat', 'cat_'], ['cat', 'dat'], ['cat', '_cat'], ['a', 'bb']]

def do_task(case):
	word1, word2 = case[0], case[1]
	p1, p2, diff_is_found = 0, 0, False
	if abs(len(word1) - len(word2)) > 1:
		return(False)
	if abs(len(word1) - len(word2)) > 0 and word1[0] != word2[0]:
		if word1[0] == word2[1]:
			p2 += 1
		if word1[1] == word2[0]:
			p1 += 1
	while p1 < len(word1) and p2 < len(word2):
		if word1[p1] == word2[p2]:
			pass
		elif p1 == p2 and not diff_is_found:
			diff_is_found = True
		else:
			return(False)
		p1 += 1; p2 += 1
	if diff_is_found and len(word1) != len(word2):
		return(False)
	return(True)

def main(cases):
	for case in cases:
		print('case: {}\t -> ret: {}'.format(case, do_task(case)))

if __name__ == '__main__': 
	main(test_case)
