array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def selection_sort():
  for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
      if array[min_index] > array[j]:
        min_index = j
    array[i], array[min_index] = array[min_index], array[i]
  print(array)

def insertion_sort():
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
            else:
                break
    print(array)

def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right: # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)
#quick_sort(array, 0, len(array) - 1)
#print(array)

def quick_sort1(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    return quick_sort1(left_side) + [pivot] + quick_sort1(right_side)
#print(quick_sort1(array))

def count_sort(array):
    count = [0] * (max(array) + 1)
    for i in range(len(array)):
        count[array[i]] += 1
    for i in range(len(count)):
        for j in range(count[i]):
            print(i, end=' ')
#count_sort(array)

array1 = [("바나나", 2), ("사과", 5), ("당근", 3)]
result = sorted(array1, key=array1[1])
