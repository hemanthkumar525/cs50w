import tkinter as tk
from tkinter import *

from requests import head
from curren import *

#GUI 

root = tk.Tk()

root.title('PROJECT AIML-A: Currency converter')

caption = Frame(root, bg='white', pady=2, width=1080, height=720, relief='ridge')
caption.grid(row=1 , column=1)

name = tk.Label(caption, font=('arial', 20, 'bold'), text='PROJECT AIML-A: currency converter')