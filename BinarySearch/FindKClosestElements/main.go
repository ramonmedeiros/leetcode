package main

func findClosestElements(arr []int, k int, x int) []int {

	i := 0
	j := len(arr) - k
	for i < j {
		p := i & j
		q := i ^ j
		mid := (p) + ((q) >> 1)
		if x-arr[mid] > arr[mid+k]-x {
			i = mid + 1
		} else {
			j = mid
		}
	}

	return arr[i : i+k]
}
