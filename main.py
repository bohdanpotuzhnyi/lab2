class Sort:
    def __init__(self, array = []):
        self.array = array
        self.len = len(array)

    def prepare(numbers, low, high):
        pivot = numbers[high]
        item = low - 1

        for i in range(low, high):


            # перевіряємо чи число меньше за останннє
            if numbers[i] <= pivot:
                item = item + 1

                # міняємо місцями елемент з більшим значенням і меньшим
                (numbers[item], numbers[i]) = (numbers[i], numbers[item])

        # Змінюємо місцями обраний елемент, з останнім по порядку з масиву більшим за нього
        (numbers[item + 1], numbers[high]) = (numbers[high], numbers[item + 1])

        return item + 1

    def quick_sort(array, low, high):
        # додаємо перевірку щоб зупинити виконання скрипту коли залишиться один елемент в масиві
        if low < high:
            # підготовлюємо масив до того щоб його далі сортувати, таким чином щоб елементи меньші за обраний зліва від нього, і більші справа
            pivot = Sort.prepare(array, low, high)

            # запускаємо сортування для масиву з елементами меньшими за останній елемент
            Sort.quick_sort(array, low, pivot - 1)
            # запсукаємо сортування для масиву з елементами більшими за останній елемент
            Sort.quick_sort(array, pivot + 1, high)

    def QUICKSORT(self):

        Sort.quick_sort(self.array, 0, self.len-1)

        return self.array
