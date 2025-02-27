import tkinter as tk
from tkinter import ttk
from Encode import encode
from Decode import decode
import ttkbootstrap as tb



root = tb.Window(themename="cyborg")  # Choose a theme (e.g., 'solar', 'darkly', 'minty', "cosmo", "flatly", "journal","morph","litera","superhero","cyborg","vapor" etc.)


root.title("Secret Word Generator")

width, height = 450, 650

display_width = root.winfo_screenwidth()
display_height = root.winfo_screenheight()

left = int(display_width/2-width/2)
top = int(display_height/2-height/2)

root.geometry(f"{width}x{height}+{left}+{top}")


def copy_to_clipboard(text):
    root.clipboard_clear()  # Clear previous clipboard content
    root.clipboard_append(text.get("1.0", tk.END).strip())  # Copy the text
    root.update()  # Keep clipboard content even after closing the app

def paste(entry_widget):
    clipboard_content = root.clipboard_get()
    cursor_position = entry_widget.index(tk.INSERT)
    try:
        entry_widget.insert(cursor_position, clipboard_content)

    except tk.TclError:
        entry_widget.insert(cursor_position, "")


notebook = tb.Notebook(root)

frame1 = tb.Frame(notebook, width=700, height=600, relief=tk.FLAT)
frame1.pack_propagate()
frame1.pack()

def encoding(event):
    entered_word = Entry1.get()
    Entry1.delete(0, tk.END)
    try:
        shift_no = int(shift_num.get())
    except ValueError:
        shift_no = 0

    result = encode(entered_word, shift_no)
    result_text.config(state="normal")  # Enable editing
    result_text.delete(1.0, tk.END)  # Clear previous result
    result_text.insert(tk.END, result)  # Insert new result
    result_text.config(state="disabled")  # Disable editing



heading = tb.Label(frame1, text="Enter your text:", font=("Perpetua", 17),)
heading.pack(pady=7)

entry_frame = tb.Frame(frame1)
entry_frame.pack(pady=10)

Entry1 = ttk.Entry(entry_frame, font="Perpetua 13", width=37)
Entry1.pack(pady = 10, side="left", padx=(0.5))
Entry1.bind("<Return>", encoding)

paste_btn = tb.Button(entry_frame, text="📋", bootstyle="secondary-link", command= lambda :paste(Entry1))
paste_btn.place(relx=1, rely=0.5, anchor="e")

label3 = ttk.Label(frame1, text="Shift the letters by: ", bootstyle="info")
label3.pack()

shift_num = ttk.Spinbox(frame1, from_=1, to=26)
shift_num.set(0)
shift_num.pack()
shift_num.bind("<Return>", encoding)

label1 = ttk.Label(frame1, text="Secret Text:", font="Perpetua 14")
label1.pack(pady=20)

result_text = tk.Text(frame1, font="Perpetua 17", width=27, height=8, wrap="word")
result_text.pack(pady= 5)
result_text.configure(state="disabled")

copy_button = tb.Button(frame1, text="Copy", bootstyle="primary", command=lambda: copy_to_clipboard(result_text))
copy_button.pack(pady=5)






frame2 = tb.Frame(notebook, width=700, height=600, relief=tk.FLAT)
frame2.pack()


def Decode(event):

    entered_word2 = Entry2.get()
    Entry2.delete(0, tk.END)
    try:
        shifted_no = int(shifted_num.get())

    except ValueError:
        shifted_no = 0

    result2 = decode(entered_word2,shifted_no)
    result_text2.config(state="normal")  # Enable editing
    result_text2.delete(1.0, tk.END)  # Clear previous result
    result_text2.insert(tk.END, result2)  # Insert new result
    result_text2.config(state="disabled")  # Disable editing



heading2 = ttk.Label(frame2, text="Enter your secret text:", font="Perpetua 17")
heading2.pack(pady = 7)

entry_frame2 = tb.Frame(frame2)
entry_frame2.pack(pady=10)

Entry2 = ttk.Entry(entry_frame2, font="Perpetua 13", width=37)
Entry2.pack(pady = 10, side="left", padx=(0.5))
Entry2.bind("<Return>", Decode)

paste_btn2 = tb.Button(entry_frame2, text="📋", bootstyle="secondary-link", command=lambda :paste(Entry2))
paste_btn2.place(relx=1, rely=0.5, anchor="e")

label4 = tb.Label(frame2, text = "Letters are shifted by:", bootstyle="info")
label4.pack()

shifted_num = ttk.Spinbox(frame2, from_=1, to=26)
shifted_num.set(0)
shifted_num.pack()
shifted_num.bind("<Return>", Decode)

label2 = ttk.Label(frame2, text="Decoded Text:", font="Perpetua 14")
label2.pack(pady=20)

result_text2 = tk.Text(frame2, font="Perpetua 17", width=27, height=8, wrap="word")
result_text2.pack(pady= 5)
result_text2.configure(state="disabled")

copy_button2 = tb.Button(frame2, text="Copy", bootstyle="primary", command=lambda: copy_to_clipboard(result_text2))
copy_button2.pack(pady=5)

notebook.add(frame1, text="Text ➡ Code")
notebook.add(frame2, text="Code ➡ Text")
notebook.pack()




root.mainloop()

