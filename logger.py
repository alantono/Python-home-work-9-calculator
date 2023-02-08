import logging
from tkinter import *

def log(a):
    logging.basicConfig(level = logging.INFO, filename = "Calculator.log",  format = '%(asctime)s %(levelname)s %(message)s',
                        datefmt = '%m/%d/%Y %I:%M:%S %p', encoding = "utf-8")
    logging.debug(a)
    logging.info(a)
    logging.warning(a)
    logging.error(a)
    logging.critical(a)

def print():
    window_text = Tk()
    window_text.title("История событий")
    window_text.geometry("400x600+1400+400")
    t = Text(window_text)
    t.pack()
    with open("Calculator.log", encoding="utf-8") as f_data:
        t.insert(1.0, f_data.read())
    window_text.mainloop()

