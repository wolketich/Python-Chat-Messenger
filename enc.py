import tkinter as tk
from tkinter import ttk

frndmessages = []
mymsg = []

def main():
    root = tk. Tk()
    root.title("Preparing...")
    root.geometry("400x350")
    image = tk.PhotoImage(file="logos.png")
    label = tk.Label(root, image=image)
    label.pack()
    # Create progress bar widget
    progress = ttk.Progressbar(root, orient=tk.HORIZONTAL,
                               length=250, mode='indeterminate')
    progress.pack (pady=10)

    # Start progress bar
    progress.start(10)

    #Destroy window after 5 seconds
    root.after(5000, root.destroy)

    root.mainloop()
