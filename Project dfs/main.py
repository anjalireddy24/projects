import tkinter as tk
from tkinter import filedialog, messagebox
from stego_utils import embed_text, extract_text

def select_image():
    path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.bmp")])
    if path:
        image_path.set(path)

def hide_message():
    if not image_path.get() or not message_entry.get():
        messagebox.showerror("Error", "Select image and enter message.")
        return
    output = filedialog.asksaveasfilename(defaultextension=".png")
    if output:
        success = embed_text(image_path.get(), output, message_entry.get())
        if success:
            messagebox.showinfo("Success", "Message embedded successfully.")
        else:
            messagebox.showerror("Error", "Image too small.")

def reveal_message():
    if not image_path.get():
        messagebox.showerror("Error", "Select image first.")
        return
    msg = extract_text(image_path.get())
    messagebox.showinfo("Hidden Message", msg)

root = tk.Tk()
root.title("Steganography Tool")

image_path = tk.StringVar()

tk.Label(root, text="Image Path:").pack()
tk.Entry(root, textvariable=image_path, width=50).pack()
tk.Button(root, text="Browse", command=select_image).pack()

tk.Label(root, text="Message to Hide:").pack()
message_entry = tk.Entry(root, width=50)
message_entry.pack()

tk.Button(root, text="Hide Message", command=hide_message).pack(pady=5)
tk.Button(root, text="Reveal Message", command=reveal_message).pack(pady=5)

root.mainloop()