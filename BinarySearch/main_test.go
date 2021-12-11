package main

import (
	"fmt"
	"testing"
)

func Test_11Array(t *testing.T) {
	a := []int{1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10}
	fmt.Println(a)

	ret := binarySearch(a, 5)
	if !(ret == [2]int{4, 5}) {
		t.Error(ret)
	}

}

func Test_20Array(t *testing.T) {
	a := []int{1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 16, 17, 18}
	fmt.Println(a)

	ret := binarySearch(a, 16)
	if !(ret == [2]int{16, 17}) {
		t.Error(ret)
	}

}

func Test_EqualElements(t *testing.T) {
	a := []int{1, 1, 1}
	fmt.Println(a)

	ret := binarySearch(a, 1)
	if !(ret == [2]int{0, 2}) {
		t.Error(ret)
	}

}

func Test_EqualElements2(t *testing.T) {
	a := []int{2, 2}
	fmt.Println(a)

	ret := binarySearch(a, 2)
	if !(ret == [2]int{0, 1}) {
		t.Error(ret)
	}

}
