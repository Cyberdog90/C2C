import cv2 as cv
import tkinter.filedialog
import os


def encoder():
    root = tkinter.Tk()
    root.withdraw()
    file_type = [("file", "*")]
    idir = os.path.abspath(os.path.dirname(__file__))
    filename = tkinter.filedialog.askopenfilename(filetypes=file_type,
                                                  initialdir=idir)
    with open(filename, "r") as f:
        data = f.readlines()
        data = list("".join(data))
        data = [ord(i) for i in data]
        if len(data) % 3 == 2:
            tmp = data.pop(-1)
            tmp2 = data.pop(-1)
            last = [tmp, tmp2, 0]
        elif len(data) % 3 == 1:
            tmp = data.pop(-1)
            last = [tmp, 0, 0]
        else:
            last = [0, 0, 0]
        data_list = []
        for i in range(int(len(data) / 3)):
            tmp = []
            for j in range(3):
                tmp.append(data.pop(0))
            data_list.append(tmp)
        data_list.append(last)
        draw(data_list)


def draw(data):
    img = cv.imread("tmp.png")
    for i in range(100):
        for j in range(100):
            try:
                img[i][j] = data.pop(0)
            except IndexError:
                img[i][j] = [0, 0, 0]
    cv.imwrite("output.png", img)
