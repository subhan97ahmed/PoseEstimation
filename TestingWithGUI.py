import tkinter as tk
from tkinter import ttk
import withMethods


class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)

        # Make the app responsive
        for index in [0, 1, 2]:
            self.columnconfigure(index=index, weight=1)
            self.rowconfigure(index=index, weight=1)

        # Create value lists
        self.option_menu_list = ["", "OptionMenu", "Option 1", "Option 2"]
        self.combo_list = ["Combobox", "Editable item 1", "Editable item 2"]
        self.readonly_combo_list = ["Readonly combobox", "Item 1", "Item 2"]

        # Create control variables
        self.var_0 = tk.BooleanVar()
        self.var_1 = tk.BooleanVar(value=True)
        self.var_2 = tk.BooleanVar()
        self.var_3 = tk.IntVar(value=2)
        self.var_4 = tk.StringVar(value=self.option_menu_list[1])
        self.var_5 = tk.DoubleVar(value=75.0)

        # Create widgets
        self.setup_widgets()

    def setup_widgets(self):
        # # Create a Frame for the Checkbuttons
        # self.check_frame = ttk.LabelFrame(self, text="Checkbuttons", padding=(20, 10))
        # self.check_frame.grid(
        #     row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew"
        # )
        #
        # # Checkbuttons
        # self.check_1 = ttk.Checkbutton(
        #     self.check_frame, text="Unchecked", variable=self.var_0
        # )
        # self.check_1.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")
        #
        # self.check_2 = ttk.Checkbutton(
        #     self.check_frame, text="Checked", variable=self.var_1
        # )
        # self.check_2.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")
        #
        # self.check_3 = ttk.Checkbutton(
        #     self.check_frame, text="Third state", variable=self.var_2
        # )
        # self.check_3.state(["alternate"])
        # self.check_3.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")
        #
        # self.check_4 = ttk.Checkbutton(
        #     self.check_frame, text="Disabled", state="disabled"
        # )
        # self.check_4.state(["disabled !alternate"])
        # self.check_4.grid(row=3, column=0, padx=5, pady=10, sticky="nsew")
        #
        # # Separator
        # self.separator = ttk.Separator(self)
        # self.separator.grid(row=1, column=0, padx=(20, 10), pady=10, sticky="ew")
        #
        # # Create a Frame for the Radiobuttons
        # self.radio_frame = ttk.LabelFrame(self, text="Radiobuttons", padding=(20, 10))
        # self.radio_frame.grid(row=2, column=0, padx=(20, 10), pady=10, sticky="nsew")
        #
        # # Radiobuttons
        # self.radio_1 = ttk.Radiobutton(
        #     self.radio_frame, text="Unselected", variable=self.var_3, value=1
        # )
        # self.radio_1.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")
        # self.radio_2 = ttk.Radiobutton(
        #     self.radio_frame, text="Selected", variable=self.var_3, value=2
        # )
        # self.radio_2.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")
        # self.radio_4 = ttk.Radiobutton(
        #     self.radio_frame, text="Disabled", state="disabled"
        # )
        # self.radio_4.grid(row=3, column=0, padx=5, pady=10, sticky="nsew")
        #
        # Create a Frame for input widgets
        self.widgets_frame = ttk.Frame(self, padding=(0, 0, 0, 10))
        self.widgets_frame.grid(
            row=0, column=1, padx=10, pady=(30, 10), sticky="nsew", rowspan=3
        )
        self.widgets_frame.columnconfigure(index=0, weight=1)

        # # Entry
        # self.entry = ttk.Entry(self.widgets_frame)
        # self.entry.insert(0, "Entry")
        # self.entry.grid(row=0, column=0, padx=5, pady=(0, 10), sticky="ew")
        #
        # # Spinbox
        # self.spinbox = ttk.Spinbox(self.widgets_frame, from_=0, to=100, increment=0.1)
        # self.spinbox.insert(0, "Spinbox")
        # self.spinbox.grid(row=1, column=0, padx=5, pady=10, sticky="ew")
        #
        # # Combobox
        # self.combobox = ttk.Combobox(self.widgets_frame, values=self.combo_list)
        # self.combobox.current(0)
        # self.combobox.grid(row=2, column=0, padx=5, pady=10, sticky="ew")
        #
        # # Read-only combobox
        # self.readonly_combo = ttk.Combobox(
        #     self.widgets_frame, state="readonly", values=self.readonly_combo_list
        # )
        # self.readonly_combo.current(0)
        # self.readonly_combo.grid(row=3, column=0, padx=5, pady=10, sticky="ew")
        #
        # # Menu for the Menubutton
        # self.menu = tk.Menu(self)
        # self.menu.add_command(label="Menu item 1")
        # self.menu.add_command(label="Menu item 2")
        # self.menu.add_separator()
        # self.menu.add_command(label="Menu item 3")
        # self.menu.add_command(label="Menu item 4")
        #
        # # Menubutton
        # self.menubutton = ttk.Menubutton(
        #     self.widgets_frame, text="Menubutton", menu=self.menu, direction="below"
        # )
        # self.menubutton.grid(row=4, column=0, padx=5, pady=10, sticky="nsew")
        #
        # # OptionMenu
        # self.optionmenu = ttk.OptionMenu(
        #     self.widgets_frame, self.var_4, *self.option_menu_list
        # )
        # self.optionmenu.grid(row=5, column=0, padx=5, pady=10, sticky="nsew")

        # Button
        self.button = ttk.Button(self.widgets_frame, text="Start Test",
                                 command=lambda: withMethods.scoreExercise("wrist curl"))
        self.button.grid(row=6, column=0, padx=5, pady=10, sticky="nsew")

        # Sizegrip
        self.sizegrip = ttk.Sizegrip(self)
        self.sizegrip.grid(row=100, column=100, padx=(0, 5), pady=(0, 5))


if __name__ == "__main__":
    root = tk.Tk()
    root.title("")
    import os

    print(os.path.exists("./themes/azure.tcl"))
    # Simply set the theme
    root.tk.call("source", "./themes/azure.tcl")
    root.tk.call("set_theme", "dark")

    app = App(root)
    app.pack(fill="both", expand=True)

    # Set a minsize for the window, and place it in the middle
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate - 20))

    root.mainloop()
