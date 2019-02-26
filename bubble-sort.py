def bubble_steps(numbers):
    for i in range(len(numbers)):
        swap = False
        for j in range(0, len(numbers)-i-1):
            if numbers[j] > numbers[j + 1]:
                print(numbers)
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swap = True
        if swap == False:
            break
    
    return numbers

def bubble(numbers):
    for i in range(len(numbers)):
        swap = False
        for j in range(0, len(numbers)-i-1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swap = True
        if swap == False:
            break
    
    return numbers

print(bubble_steps([4, 5, 1, 2, 0, 10, -5, -1, 12, 42, -8, 0]))
print("--------")
print(bubble([4, 5, 1, 2, 0, 10, -5, -1, 12, 42, -8, 0]))