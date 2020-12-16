from tkinter import *
import time

WIDTH = 900
HEIGHT = 600


class Sort_UI(Frame):
    def __init__(self, board):
        self.sorting = board
        self.parent = Tk()
        Frame.__init__(self, self.parent)

        self.row, self.col = -1, -1
        self.__initialize()

    def __initialize(self):
        self.parent.title("Sorting Algorithms Visualizer")
        self.parent.option_add("*Font", "comicsans 18")
        self.pack(fill=BOTH)

        # UI Elements
        self.canvas = Canvas(self, width=WIDTH, height=HEIGHT)
        self.canvas.pack(side=TOP, fill=BOTH)

        self.generate_button = Button(
            self, text="Generate Array", command=lambda: [self.sorting.populate_board(), self.draw_board(self.sorting.board)])
        self.generate_button.pack(side=LEFT, padx=15, pady=5)
        self.merge_button = Button(
            self, text="Merge Sort", command=lambda: self.merge_sort(self.sorting.board, 0, len(self.sorting.board)-1))
        self.merge_button.pack(side=LEFT, padx=15)
        self.quick_button = Button(self, text="Quick Sort", command=lambda: self.quick_sort(
            self.sorting.board, 0, len(self.sorting.board)-1))
        self.quick_button.pack(side=LEFT, padx=15)
        self.bubble_button = Button(
            self, text="Bubble Sort", command=lambda: self.bubble_sort(self.sorting.board))
        self.bubble_button.pack(side=LEFT, padx=15)
        self.heap_button = Button(
            self, text="Heap Sort", command=lambda: self.heap_sort(self.sorting.board))
        self.heap_button.pack(side=LEFT, padx=15)

        self.draw_board(self.sorting.board)

    def draw_board(self, board):
        self.canvas.delete("lines")
        for i in range(len(board)):
            gap = 15
            line_w = (WIDTH/len(board)) / 2
            x0 = 80 + (i*gap)
            y0 = 600
            x1 = 80 + (i*gap)
            y1 = 600 - (board[i].value * 12)
            self.canvas.create_line(
                x0, y0, x1, y1, tag="lines", fill=board[i].get_color(), width=line_w)
        self.update()
        time.sleep(0.01)

    def merge_sort(self, array, l, r):
        middle = (l+r)//2
        self.draw_board(self.sorting.board)
        if l < r:
            self.merge_sort(array, l, middle)
            self.merge_sort(array, middle+1, r)
            self.merge(array, l, middle, middle+1, r)

    def merge(self, array, x1, y1, x2, y2):
        i = x1
        j = x2
        temp = []
        for ele in array:
            ele.make_open()
        # sort the 1/4 arrays
        while i <= y1 and j <= y2:
            self.draw_board(self.sorting.board)
            if array[i].value < array[j].value:
                array[i].reset_color()
                temp.append(array[i])
                i += 1
            else:
                array[j].reset_color()
                temp.append(array[j])
                j += 1
        # merge the first two quarters
        while i <= y1:
            array[i].reset_color()
            self.draw_board(self.sorting.board)
            temp.append(array[i])
            i += 1
        # merge the last two quarters
        while j <= y2:
            array[j].reset_color()
            self.draw_board(self.sorting.board)
            temp.append(array[j])
            j += 1
        j = 0
        # merge the two halves
        for i in range(x1, y2 + 1):
            array[i] = temp[j]
            j += 1
            self.draw_board(self.sorting.board)

    def quick_sort(self, array, low, high):
        if low < high:
            pi = self.partition(array, low, high)
            self.quick_sort(array, low, pi-1)
            for ele in array:
                ele.reset_color()
            self.draw_board(self.sorting.board)
            self.quick_sort(array, pi+1, high)

    def partition(self, array, low, high):
        i = (low-1)
        pivot = array[high]

        for j in range(low, high):
            self.draw_board(self.sorting.board)
            if array[j].value <= pivot.value:
                array[j].make_open()
                i += 1
                array[i], array[j] = array[j], array[i]
        array[j].reset_color()
        self.draw_board(self.sorting.board)
        array[i+1], array[high] = array[high], array[i+1]
        return (i+1)

    def bubble_sort(self, array):
        for ele in array:
            ele.make_open()
        for i in range(len(array)-1):
            for j in range(len(array)-i-1):
                if array[j].value > array[j+1].value:
                    array[j].reset_color()
                    temp = array[j]
                    array[j] = array[j+1]
                    array[j+1] = temp
                self.draw_board(self.sorting.board)

    def heap_sort(self, array):
        n = len(array)
        for i in range(n//2-1, -1, -1):
            self.heapify(array, i, n)
        for i in range(n-1, 0, -1):
            array[i], array[0] = array[0], array[i]
            array[i].reset_color()
            self.draw_board(self.sorting.board)
            self.heapify(array, 0, i)

    def heapify(self, array, root, size):
        left = root*2+1
        right = root*2+2
        largest = root
        if left < size and array[left].value > array[largest].value:
            largest = left
        if right < size and array[right].value > array[largest].value:
            largest = right
        if largest != root:
            array[largest], array[root] = array[root], array[largest]
            self.draw_board(self.sorting.board)
            array[largest].make_open()
            array[root].make_open()
            self.heapify(array, largest, size)
            self.draw_board(self.sorting.board)
