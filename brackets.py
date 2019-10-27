# This is a small code to validate parentheses
# @autor CristopherA96 

def brackets(word):
	stackw = []
	par = {"(": ")", "{": "}", "[": "]"}
	for parentheses in word:
		if parentheses in par:
			stackw.append(parentheses)
		elif len(stackw) == 0 or par[stackw.pop()] != parentheses:
			return False
	return len(stackw) == 0

print(brackets("[[(){}[]]]"))
print(brackets("([)]{}"))
