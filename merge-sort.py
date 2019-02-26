def mergeSort(numbers):
    print("Splitting ",numbers)
    if len(numbers)>1:
        mid = len(numbers)//2
        lefthalf = numbers[:mid]
        righthalf = numbers[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                numbers[k]=lefthalf[i]
                i += 1
            else:
                numbers[k]=righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            numbers[k]=lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            numbers[k]=righthalf[j]
            j += 1
            k += 1
    print("Merging ",numbers)

numbers = [54,26,93,17,77,31,44,55,20]
mergeSort(numbers)
print(numbers)
