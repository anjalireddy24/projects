import tkinter as tk
from tkinter import filedialog, messagebox
from analyzer import analyze_password
from wordlist_generator import generate_from_password, export_wordlist

def run_gui():
    def analyze_and_generate():
        password = entry_password.get()
        result = analyze_password(password)
        feedback = f"Score: {result['score']}/4\nFeedback: {result['feedback']}\nCrack Times: {result['crack_times']}"
        text_result.delete("1.0", tk.END)
        text_result.insert(tk.END, feedback)

        wordlist = generate_from_password(password)
        filename = filedialog.asksaveasfilename(defaultextension=".txt", title="Save Wordlist")
        if filename:
            export_wordlist(wordlist, filename)
            messagebox.showinfo("Success", f"Wordlist saved to {filename}")

    root = tk.Tk()
    root.title("Password Analyzer")

    tk.Label(root, text="Password:").grid(row=0, column=0)
    entry_password = tk.Entry(root, show="*")
    entry_password.grid(row=0, column=1)

    tk.Button(root, text="Analyze & Generate", command=analyze_and_generate).grid(row=1, column=0, columnspan=2)

    text_result = tk.Text(root, height=10, width=50)
    text_result.grid(row=2, column=0, columnspan=2)

    root.mainloop()