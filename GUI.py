import tkinter as tk

def on_button_click():
    label.config(text="Hello, " + entry.get())

# Create the main window
window = tk.Tk()
window.title("Simple GUI")

# Create a label
label = tk.Label(window, text="Enter your name:")
label.pack(pady=10)

# Create an entry widget (for input)
entry = tk.Entry(window)
entry.pack(pady=10)

# Create a button
button = tk.Button(window, text="Say Hello", command=on_button_click)
button.pack(pady=10)

# Run the main loop
window.mainloop()
