from tkinter import *
from tkinter import messagebox

# ----------------------Variables--------------------

color_1 = '#141414'
color_2 = 'orange'
color_3 = 'white'
width_button = 4
font_button = 'Georgia 15'
size_padding = 3

# ---------------------Settings---------------------

root = Tk()
root.geometry("250x300")
root.title("Calculator")
root.resizable(width=False, height=False)

# ---------------------Frames-----------------------

top_first = Frame(root)
top_first.pack(side=TOP)

top_second = Frame(root)
top_second.pack(side=TOP)

top_third = Frame(root)
top_third.pack(side=TOP)

top_fourth = Frame(root)
top_fourth.pack(side=TOP)

top_fifth = Frame(root)
top_fifth.pack(side=TOP)

top_sixth = Frame(root)
top_sixth.pack(side=TOP)

# ---------------------Buttons----------------------

Button(top_second, text="+", width=width_button, highlightbackground=color_1, bg=color_1, fg=color_3,
       font=font_button,
       command=lambda: add_text_to_entry("+")).pack(side=LEFT, padx=size_padding, pady=size_padding)
Button(top_second, text="-", width=width_button, highlightbackground=color_1, bg=color_1, fg=color_3, font=font_button,
       command=lambda: add_text_to_entry("-")).pack(side=LEFT, padx=size_padding, pady=size_padding)
Button(top_second, text="*", width=width_button, highlightbackground=color_1, bg=color_1, fg=color_3, font=font_button,
       command=lambda: add_text_to_entry("*")).pack(side=LEFT, padx=size_padding, pady=size_padding)
Button(top_second, text="/", width=width_button, highlightbackground=color_1, bg=color_1, fg=color_3, font=font_button,
       command=lambda: add_text_to_entry("/")).pack(side=LEFT, padx=size_padding, pady=size_padding)

#

Button(top_third, text="7", width=width_button, highlightbackground=color_1, bg=color_1, fg=color_3, font=font_button,
       command=lambda: add_text_to_entry("7")).pack(side=LEFT, padx=size_padding, pady=size_padding)
Button(top_third, text="8", width=width_button, highlightbackground=color_1, bg=color_1, fg=color_3, font=font_button,
       command=lambda: add_text_to_entry("8")).pack(side=LEFT, padx=size_padding, pady=size_padding)
Button(top_third, text="9", width=width_button, highlightbackground=color_1, bg=color_1, fg=color_3, font=font_button,
       command=lambda: add_text_to_entry("9")).pack(side=LEFT, padx=size_padding, pady=size_padding)
Button(top_third, text="%", width=width_button, highlightbackground=color_1, bg=color_1, fg=color_3, font=font_button,
       command=lambda: add_text_to_entry("%")).pack(side=LEFT, padx=size_padding, pady=size_padding)

#

Button(top_fourth, text="4", width=width_button, highlightbackground=color_1, bg=color_1, fg=color_3, font=font_button,
       command=lambda: add_text_to_entry("4")).pack(side=LEFT, padx=size_padding, pady=size_padding)
Button(top_fourth, text="5", width=width_button, highlightbackground=color_1, bg=color_1, fg=color_3, font=font_button,
       command=lambda: add_text_to_entry("5")).pack(side=LEFT, padx=size_padding, pady=size_padding)
Button(top_fourth, text="6", width=width_button, highlightbackground=color_1, bg=color_1, fg=color_3, font=font_button,
       command=lambda: add_text_to_entry("6")).pack(side=LEFT, padx=size_padding, pady=size_padding)
Button(top_fourth, text="x", width=width_button, highlightbackground=color_1, bg=color_1, fg=color_3, font=font_button,
       command=lambda: clear_one_character()).pack(side=LEFT, padx=size_padding, pady=size_padding)

#

Button(top_fifth, text="1", width=width_button, highlightbackground=color_1, bg=color_1, fg=color_3, font=font_button,
       command=lambda: add_text_to_entry("1")).pack(side=LEFT, padx=size_padding, pady=size_padding)
Button(top_fifth, text="2", width=width_button, highlightbackground=color_1, bg=color_1, fg=color_3, font=font_button,
       command=lambda: add_text_to_entry("2")).pack(side=LEFT, padx=size_padding, pady=size_padding)
Button(top_fifth, text="3", width=width_button, highlightbackground=color_1, bg=color_1, fg=color_3, font=font_button,
       command=lambda: add_text_to_entry("3")).pack(side=LEFT, padx=size_padding, pady=size_padding)
Button(top_fifth, text="C", width=width_button, highlightbackground=color_1, bg=color_1, fg=color_3, font=font_button,
       command=lambda: clear()).pack(side=LEFT, padx=size_padding, pady=size_padding)

#

Button(top_sixth, text=".", width=width_button, highlightbackground=color_1, bg=color_1, fg=color_3, font=font_button,
       command=lambda: add_text_to_entry(".")).pack(side=LEFT, padx=size_padding, pady=size_padding)
Button(top_sixth, text="0", width=width_button, highlightbackground=color_1, bg=color_1, fg=color_3, font=font_button,
       command=lambda: add_text_to_entry("0")).pack(side=LEFT, padx=size_padding, pady=size_padding)
Button(top_sixth, text="=", width=12, highlightbackground=color_1, bg=color_2, font=font_button,
       command=lambda: elevate()).pack(side=LEFT, padx=size_padding, pady=size_padding)

# ---------------------Entry-----------------------

entry = Entry(top_first, font=('Georgia 40'))
entry.pack(side=LEFT)


# ----------------------functions------------------

def elevate():
    try:
        result = str(eval(entry.get()))
        clear()
        entry.insert(END, result)
    except:
        messagebox.showinfo('Error', "An error occured!")
        clear()


def add_text_to_entry(text):
    entry.insert(END, text)


def clear_one_character():
    entry.delete(0)


def clear():
    entry.delete(0, END)


# -----------------------------------------------

root.mainloop()
