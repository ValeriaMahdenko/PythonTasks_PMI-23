import task
# Доповнити завдання №2 (програмування).
# В результуючому масиві знайти число, яке дорівнює К за допомогою бінарного пошуку.
# Вивести позицію елемента, якщо елементів декілька, то позиції всіх елементів.
# Вивести кількість операцій, необхідних для пошуку, та всі здійснені всі операції.


class Index(object):
    def __init__(self, value, index):
        self.value = value
        self.index = index


def binary_search(mas, k):
    mid = len(mas) // 2
    low = 0
    high = len(mas) - 1
    operation = 1
    result = []
    print("Check if element K = mas[", mid, "]")
    while mas[mid].value != k and low <= high:
        operation +=1
        if k > mas[mid].value:
            print("Check if element is between ", mid+1, " and ", high)
            operation += 1
            low = mid + 1
        else:
            print("Check if element is between ", low, " and ", mid-1)
            high = mid - 1
            operation += 1
        mid = (low + high) // 2
        print("Check if element K = mas[", mid, "]")

    if low > high:
        print("Element ", k, " is not in the array!")
    else:
        print("Number of operation: ", operation)
        result.append(mas[mid].index)
        duplicates(mid, mas, result)
    return result


def duplicates(mid, mas, result):
    el = mid + 1
    while el < len(mas) and mas[el].value == element:
        result.append(mas[el].index)
        el += 1
    el = mid - 1
    while el >= 0 and mas[el].value == element:
        result.append(mas[el].index)
        el -= 1

'''
Я не зрозуміла,чи треба було переробляти sort, чи просто зрозуміти вбудовану функцію sorted.
Тому у мене повністю робочі 2 варіанти 

def sort(arr):
    for i in range(len(arr)):
        lowest_value = i
        for j in range(i + 1, len(arr)):
            if arr[j].value < arr[lowest_value].value:
                lowest_value = j
        arr[i], arr[lowest_value] = arr[lowest_value], arr[i]
'''


def mas_index():
    mas_index = []
    for i in range(len(task.result)):
        mas_index.append(Index(task.result[i], i))
    #sort(mas_index)
    mas_index = sorted(mas_index, key=lambda x: x.value)
    return mas_index


mas_ = mas_index()
element = task.validate("Enter element of array: ", choice="pos&neg")
print("Index: ", binary_search(mas_, element ))

