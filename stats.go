// Lab 1: The Multi-Paradigm Tour -- Go implementation.
//
// Compile: go build -o stats_go stats.go
// Run:     ./stats_go 4 8 15 16 23 42
//
// Complete the TODO section. See the assignment,
// Part B, for the full shared contract (all three language versions
// must match it exactly, including the tie-breaking mode rule).

package main

import (
	"fmt"
	"os"
	"sort"
	"strconv"
)

func computeStats(nums []int) (float64, float64, int) {
	// TODO: compute mean, median, and mode from nums.
	// - median: for an even count, average the two middle values of a SORTED copy.
	// - mode: most frequent value; on a tie, the SMALLEST tied value.
	// sort.Ints(sortedCopy) and a map[int]int frequency count will help.
	var mean float64
	var median float64
	var mode int

	n := len(nums)

	// mean
	if n > 0 {
		total := 0
		for _, v := range nums {
			total += v
		}
		mean = float64(total) / float64(n)
	}

	// median
	sortedCopy := make([]int, n)
	copy(sortedCopy, nums)
	sort.Ints(sortedCopy)

	if n > 0 {
		mid := n / 2
		if n%2 == 0 {
			median = float64(sortedCopy[mid-1]+sortedCopy[mid]) / 2.0
		} else {
			median = float64(sortedCopy[mid])
		}
	}

	// mode
	frequency := make(map[int]int)
	for _, v := range nums {
		frequency[v]++
	}

	if len(frequency) > 0 {
		maxFreq := 0
		for _, v := range sortedCopy { // ascending order, so ties resolve to smallest
			f := frequency[v]
			if f > maxFreq {
				maxFreq = f
				mode = v
			}
		}
	}
	return mean, median, mode
}

func main() {
	if len(os.Args) < 2 {
		os.Exit(1)
	}

	nums := make([]int, 0, len(os.Args)-1)
	for _, arg := range os.Args[1:] {
		n, err := strconv.Atoi(arg)
		if err != nil {
			os.Exit(1)
		}
		nums = append(nums, n)
	}

	mean, median, mode := computeStats(nums)
	fmt.Printf("Mean: %.2f\n", mean)
	fmt.Printf("Median: %.2f\n", median)
	fmt.Printf("Mode: %d\n", mode)
	_ = sort.Ints // keep import used even before TODO is filled in
	os.Exit(0)
}
