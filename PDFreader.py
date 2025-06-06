import tkinter as tk
from tkinter import filedialog, messagebox
import fitz
root = tk.Tk()
root.title("Hmmza's PDF READER")
root.geometry("800x600")
pdf_file = None
current_page = 0
def open_pdf():
    global pdf_file, current_page
    filepath = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if filepath:
        try:
            pdf_file = fitz.open(filepath)
            current_page = 0
            show_page(current_page)
        except Exception as e:
            messagebox.showerror("Error!",f"Failed to load PDF:\n{e}")
def show_page(page_num):
    if pdf_file:
        try:
            page = pdf_file[page_num]
            text = page.get_text()
            text_box.delete("1.0", tk.END)
            text_box.insert(tk.END, text)
            page_label.config(text=f"page {page_num + 1} of {len(pdf_file)}")
        except IndexError:
            messagebox.showerror("Error", "Invalid page number")
def next_page():
    global current_page
    if pdf_file and current_page < len(pdf_file) - 1:
        current_page += 1
        show_page(current_page)
def prev_page():
    global current_page
    if pdf_file and current_page > 0:
        current_page -= 1
        show_page(current_page)

open_button = tk.Button(root, text="Open PDF", command=open_pdf)
open_button.pack(pady=10)
page_label = tk.Label(root, text="page: N/A")
page_label.pack()
text_box = tk.Text(root, wrap=tk.WORD, font=("Helvetica", 12))
text_box.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)


nav_frame = tk.Frame(root)
nav_frame.pack(pady=5)
prev_button = tk.Button(nav_frame, text="<< Previous", command=prev_page)
prev_button.pack(side=tk.LEFT, padx=10)
next_button = tk.Button(nav_frame, text="Next >>", command=next_page)
next_button.pack(side=tk.RIGHT, padx=10)
root.mainloop()
