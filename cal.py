import numpy as np

SLIDES_NUM = 10

f = open(r"58424 1974.txt")
line = f.readline()
# data_list = []
num = list(map(int, line.split()))
line = f.readline()
while line:
    num += list(map(int, line.split()))
    # data_list.append(num)
    line = f.readline()
f.close()
data_array = np.array(num)


# print(data_array.size)
# print(data_array)

def calendar(leap, n):
    if leap is True:
        if n <= 31:
            print("1月", n, "日")
        elif n <= 59:
            print("2月", (n - 31), "日")
        elif n <= 90:
            print("3月", n - 59, "日")
        elif n <= 120:
            print("4月", (n - 90), "日")
        elif n <= 151:
            print("5月", (n - 120), "日")
        elif n <= 181:
            print("6月", (n - 151), "日")
        elif n <= 212:
            print("7月", (n - 181), "日")
        elif n <= 243:
            print("8月", (n - 212), "日")
        elif n <= 273:
            print("9月", (n - 243), "日")
        elif n <= 304:
            print("10月", (n - 273), "日")
        elif n <= 334:
            print("11月", (n - 304), "日")
        else:
            print("12月", (n - 334), "日")
    else:
        if n <= 31:
            print("1月", n, "日")
        elif n <= 60:
            print("2月", (n - 31), "日")
        elif n <= 91:
            print("3月", n - 60, "日")
        elif n <= 121:
            print("4月", (n - 91), "日")
        elif n <= 152:
            print("5月", (n - 121), "日")
        elif n <= 182:
            print("6月", (n - 152), "日")
        elif n <= 213:
            print("7月", (n - 182), "日")
        elif n <= 244:
            print("8月", (n - 213), "日")
        elif n <= 274:
            print("9月", (n - 244), "日")
        elif n <= 305:
            print("10月", (n - 274), "日")
        elif n <= 335:
            print("11月", (n - 305), "日")
        else:
            print("12月", (n - 335), "日")


class Window:
    def __init__(self, right=4):
        self.right = right
        self.window = 0
        for i in range(right - 4, right + 1):
            self.window += data_array[i]

    def slide(self):
        # if self.right < data_array.size - 1:
        if self.right <= data_array.size - 1:
            self.window -= data_array[self.right - 4]
            self.right += 1
            self.window += data_array[self.right]
        return self.window

    def next_n_window(self, n):
        if self.right + n - 1 < data_array.size - 1:
            for i in range(1, n + 1):
                win = self.window + data_array[self.right + i] - data_array[self.right - 4 + i - 1]
            return win
        return -1


tmp = 0
# 计算春季
while data_array[tmp] < 100:
    tmp += 1

window1 = Window(tmp + 2)

try:
    while True:
        if window1.window >= 500:
            note = True
            for i in range(1, SLIDES_NUM):
                if window1.next_n_window(i) < 500:
                    note = False
                    break
            if note is True:
                for i in range(0, 5):
                    if data_array[window1.right - 4 + i] >= 100:
                        # print(window1.right - 3 + i)
                        calendar(True, window1.right - 1 + i)
                        break
                break
            window1.slide()
        else:
            window1.slide()
except IndexError:
    print("没有春季")


# 计算夏季
while data_array[tmp] < 220:
    tmp += 1

window2 = Window(tmp + 2)

while True:
    if window2.window >= 1100:
        note = True
        for i in range(1, SLIDES_NUM):
            if window2.next_n_window(i) < 1100:
                note = False
                break
        if note is True:
            for i in range(0, 5):
                if data_array[window2.right - 4 + i] >= 220:
                    # print(window2.right - 3 + i)
                    calendar(True, window2.right - 1 + i)
                    break
            break
        window2.slide()
    else:
        window2.slide()

# 计算秋季
tmp = window2.right
while data_array[tmp] >= 220:
    tmp += 1

window3 = Window(tmp + 2)

while True:
    if window3.window < 1100:
        note = True
        for i in range(1, SLIDES_NUM):
            if window3.next_n_window(i) >= 1100:
                note = False
                break
        if note is True:
            for i in range(0, 5):
                if data_array[window3.right - 4 + i] < 220:
                    # print(window3.right - 3 + i)
                    calendar(True, window3.right - 1 + i)
                    break
            break
        window3.slide()
    else:
        window3.slide()

# 计算冬季
while data_array[tmp] >= 100:
    tmp += 1

window4 = Window(tmp + 2)

while True:
    if window4.window < 500:
        note = True
        for i in range(1, SLIDES_NUM):
            if window4.next_n_window(i) >= 500:
                note = False
                break
        if note is True:
            for i in range(0, 5):
                if data_array[window4.right - 4 + i] < 100:
                    # print(window4.right - 3 + i)
                    calendar(True, window4.right - 1 + i)
                    break
            break
        window4.slide()
    else:
        window4.slide()
