from quill import Window
import tkinter as tk
from tkinter import ttk


class Widgets(Window):
    def startup(self):
        menu = tk.Menu(self)

        frame = ttk.Frame()
        ttk.Button(frame).pack()
        frame2 = ttk.Frame()
        ttk.Entry(frame2).pack()

        # TK

        self.insert_tk_button(text="TK Button")

        self.insert_tk_checkbutton(text="TK Checkbutton")

        self.insert_tk_entry()

        self.insert_tk_frame()

        self.insert_tk_label(text="TK Label")

        tk_labelframe = self.insert_tk_labelframe(text="TK LabelFrame")
        tk.Button(tk_labelframe).pack()

        self.insert_tk_menubutton(text="TK Menubutton", menu=menu)

        tk_panedwindow = self.insert_tk_panedwindow()
        tk_panedwindow.add(frame)
        tk_panedwindow.add(frame2)

        self.insert_tk_radiobutton(text="TK Radiobutton")

        self.insert_tk_scale()

        self.insert_tk_scrollbar()

        # TTK

        self.insert_ttk_button(text="TTK Button")

        self.insert_ttk_checkbutton(text="TTK Checkbutton")

        self.insert_ttk_entry()

        self.insert_ttk_frame()

        self.insert_ttk_label(text="TTK Label")

        ttk_labelframe = self.insert_ttk_labelframe(text="TTK LabelFrame")
        tk.Button(ttk_labelframe).pack()

        self.insert_ttk_menubutton(text="Menu Button", menu=menu)

        ttk_panedwindow = self.insert_ttk_panedwindow()
        ttk_panedwindow.add(frame)
        ttk_panedwindow.add(frame2)

        self.insert_ttk_radiobutton(text="TTK Radiobutton")

        self.insert_ttk_scale()

        self.insert_ttk_scrollbar()

        self.insert_ttk_combobox(values=["red", "blue", "yellow"])

        notebook = self.insert_ttk_notebook()
        notebook.add(frame, text="Button")
        notebook.add(frame2, text="Entry")

        self.insert_ttk_progressbar()

        self.insert_ttk_separator()

        self.insert_ttk_treeview()


def main():
    app = Widgets(title="Maze Game")
    app.mainloop()


if __name__ == "__main__":
    main()
