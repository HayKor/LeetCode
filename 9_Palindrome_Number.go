package main

import (
	"strconv"
)

func isPalindrome(x int) bool {
	str := strconv.Itoa(x)
	for i, j := 0, len(str)-1; i < len(str)/2; i, j = i+1, j-1 {
		if str[i] != str[j] {
			return false
		}
	}
	return true
}
