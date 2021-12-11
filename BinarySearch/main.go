package main

func binarySearch(nums []int, target int) [2]int {
	if len(nums) == 0 {
		return [2]int{-1, -1}
	}

	left := 0
	right := len(nums) - 1

	for left+1 < right {
		// Prevent (left + right) overflow
		mid := left + (right-left)/2
		if nums[mid] == target {
			foundLeft := searchLeft(nums, mid)
			foundRight := searchRight(nums, mid)
			return [2]int{foundLeft, foundRight}

		} else if nums[mid] < target {
			left = mid
		} else {
			right = mid
		}
	}

	// Post-processing:
	// End Condition: left + 1 == right
	if nums[left] == target {
		foundLeft := searchLeft(nums, left)
		foundRight := searchRight(nums, left)
		return [2]int{foundLeft, foundRight}
	}
	if nums[right] == target {
		foundLeft := searchLeft(nums, right)
		foundRight := searchRight(nums, right)
		return [2]int{foundLeft, foundRight}
	}

	return [2]int{-1, -1}
}

func searchLeft(array *[]int, foundIndex int) int {
	found := foundIndex
	for found > 0 && array[found-1] == array[foundIndex] {
		found = found - 1
	}

	return found
}

func searchRight(array *[]int, foundIndex int) int {
	found := foundIndex
	length := len(*array)
	for found < (length-1) && array[found+1] == array[foundIndex] {
		found = found + 1
	}

	return found
}
