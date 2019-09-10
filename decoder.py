import cv2 as cv
import tkinter.filedialog
import os


def decoder():
    main()


def main():
    root = tkinter.Tk()
    root.withdraw()
    file_type = [("file", "*")]
    idir = os.path.abspath(os.path.dirname(__file__))
    filename = tkinter.filedialog.askopenfilename(filetypes=file_type,
                                                  initialdir=idir)

    img = cv.imread(filename)
    img = img.tolist()
    img = sum(sum(img, []), [])
    with open("decode.txt", "w") as f:
        for i in img:
            if i == 0:
                exit(0)
            f.write(chr(i))
