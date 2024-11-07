class MyList:
    int_list = None

    def __init__(self, ints):
        self.int_list = ints

    def bubble_sort(self, reverse=False):
        for i in range(len(self.int_list)):
            for j in range(0, len(self.int_list) - i - 1):
                if reverse:
                    if self.int_list[j] < self.int_list[j + 1]:
                        self.int_list[j], self.int_list[j + 1] = self.int_list[j + 1], self.int_list[j]
                else:
                    if self.int_list[j] > self.int_list[j + 1]:
                        self.int_list[j], self.int_list[j + 1] = self.int_list[j + 1], self.int_list[j]
        print(self.int_list)

    def smallest(self):
        s = self.int_list[0]
        for i in range(len(self.int_list)):
            if i < len(self.int_list):
                if self.int_list[i] < s:
                    s = self.int_list[i]
        print(s)

    def largest(self):
        s = self.int_list[0]
        for i in range(len(self.int_list)):
            if i < len(self.int_list):
                if self.int_list[i] > s:
                    s = self.int_list[i]
        print(s)

    def even_count(self):
        c = 0
        for i in range(len(self.int_list)):
            b = self.int_list[i]
            if b % 2 == 0:
                c = c + 1
        print('Even count is :-', c)

    def odd_count(self):
        c = 0
        for i in range(len(self.int_list)):
            b = self.int_list[i]
            if b % 2 == 1:
                c += 1
        print('Odd count is:-', c)

    def sum_list(self):
        b = self.int_list[0] + self.int_list[1]
        for i in range(2, len(self.int_list)):
            b = b + self.int_list[i]
        print(b)

    def update_list(self, extra_list):
        self.int_list.extend(extra_list)
        print(self.int_list)

    def count_get(self, n):
        count = 0
        for num in self.int_list:
            if n == num:
                count += 1
        print(n, "=", count)

    def get_all_count(self):
        n2 = 0
        for num in self.int_list:
            if n2 != num:
                number.count_get(num)
                n2 = num


number = MyList([1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 4, 10, 5, 6, 6, 6, 7, 7, 8, 9, 9, 9, 9, 9, 9])
number.bubble_sort()
number.bubble_sort(reverse=True)
number.smallest()
number.largest()
number.even_count()
number.odd_count()
number.sum_list()
number.update_list([8, 9, 4, 3, 2, 22, 88])
number.count_get(8)
number.get_all_count()
