package main

func isValid(s string) bool {
	stack := []rune{}
	for _, sym := range s {
		switch sym {
		case '(', '[', '{':
			stack = append(stack, sym)
		default:
			if length := len(stack); length == 0 ||
				(sym == ')' && stack[length-1] != '(') ||
				(sym == '}' && stack[length-1] != '{') ||
				(sym == ']' && stack[length-1] != '[') {
				return false
			}
			stack = stack[:len(stack)-1]
		}
	}
	return len(stack) == 0
}
