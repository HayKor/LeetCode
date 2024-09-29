package main

import (
	"slices"
)

func longestCommonPrefix(strs []string) string {
	var res string

	slices.Sort(strs)
	first := strs[0]
	last := strs[len(strs)-1]

	for i := range min(len(first), len(last)) {
		if first[i] != last[i] {
			return res
		}
		res += string(first[i])
	}

	return res
}
