import tkinter as tk

# Create a function to handle button click events
def on_button_click():
    user_input = entry.get()
    label.config(text=f'Hello, {user_input}!')

# Create the main application window
root = tk.Tk()
root.title("Simple Tkinter GUI")

# Create and pack a label
label = tk.Label(root, text="Enter your name:")
label.pack()

# Create and pack an entry widget
entry = tk.Entry(root)
entry.pack()

# Create and pack a button
button = tk.Button(root, text="Submit", command=on_button_click)
button.pack()

# Start the Tkinter main loop
root.mainloop()
