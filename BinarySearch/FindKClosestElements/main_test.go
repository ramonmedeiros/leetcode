package main

import (
	"testing"
)

func Test_1stExample(t *testing.T) {
	a := []int{1, 2, 3, 4, 5}

	ret := findClosestElements(a, 4, 3)
	if len(ret) != 4 || !(ret[0] == 1 && ret[1] == 2 && ret[2] == 3 && ret[3] == 4) {
		t.Error(ret)
	}

}

func Test_2ndExample(t *testing.T) {
	a := []int{1, 2, 3, 4, 5}

	ret := findClosestElements(a, 4, -1)
	if len(ret) != 4 || !(ret[0] == 1 && ret[1] == 2 && ret[2] == 3 && ret[3] == 4) {
		t.Error(ret)
	}

}

func Test_singleElement(t *testing.T) {
	a := []int{1}

	ret := findClosestElements(a, 1, 0)
	if len(ret) != 1 || !(ret[0] == 1) {
		t.Error(ret)
	}
}

func Test_RepeatedElementsElements(t *testing.T) {
	a := []int{1, 2, 2, 2, 5, 5, 5, 8, 9, 9}

	ret := findClosestElements(a, 4, 0)
	if len(ret) != 4 || !(ret[0] == 1 && ret[1] == 2 && ret[2] == 2 && ret[3] == 2) {
		t.Error(ret)
	}

}
func Test_ConsumerEdges(t *testing.T) {
	a := []int{0, 1, 2, 2, 2, 3, 6, 8, 8, 9}

	findClosestElements(a, 5, 9)
}

func Test_aa(t *testing.T) {
	a := []int{1, 3}
	ret := findClosestElements(a, 1, 2)
	if len(ret) != 1 || ret[0] != 1 {
		t.Error(ret)
	}
}
