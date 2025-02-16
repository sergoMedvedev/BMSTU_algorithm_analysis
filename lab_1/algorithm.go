package main


// Сортировка пузырьком
// лучший O(n)
// худший O(n^2)
func BubbleSort(arr []int)  {
	for i := 0; i < len(arr)-1; i++ {
		for j := 0; j < len(arr)-i-1; j++ {
			if arr[j] > arr[j+1] {
				arr[j], arr[j+1] = arr[j+1], arr[j]
			}
		}
	}
	
}

// сортировка слиянием через буфферные массивы
// лучший O(n)
// худший O(n log(n))
func Merge(left, right []int) []int {
	result := make([]int, 0, len(left)+len(right))
	i, j := 0, 0
	for i < len(left) && j < len(right) {
		if left[i] < right[j] {
			result = append(result, left[i])
			i++
		} else {
			result = append(result, right[j])
			j++
		}
	}
	result = append(result, left[i:]...)
	result = append(result, right[j:]...)
	return result
}

func MergeSort(arr []int) []int {
	if len(arr) <= 1 {
		return arr
	}
	mid := len(arr) / 2
	left := MergeSort(arr[:mid])
	right := MergeSort(arr[mid:])
	return Merge(left, right)
}

// быстрая сортировка
// лучший O(n log(n))
// худший O(n^2)
func QuickSort(arr []int) []int {
	if len(arr) <= 1 {
		return arr
	}
	pivot := arr[len(arr)/2]
	left := []int{}
	right := []int{}
	middle := []int{}

	for _, num := range arr {
		if num < pivot {
			left = append(left, num)
		} else if num > pivot {
			right = append(right, num)
		} else {
			middle = append(middle, num)
		}
	}

	left = QuickSort(left)
	right = QuickSort(right)
	return append(append(left, middle...), right...)
}

