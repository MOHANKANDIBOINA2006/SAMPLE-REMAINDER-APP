import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import threading
import time

def set_reminder():
    reminder_time = time_entry.get().strip().upper()
    reminder_msg = msg_entry.get().strip()

    if not reminder_time or not reminder_msg:
        messagebox.showwarning('Warning', 'Please enter both time and message!')
        return

    # Validate time format with seconds
    try:
        datetime.strptime(reminder_time, '%I:%M:%S %p')
    except ValueError:
        messagebox.showerror('Error', 'Please enter time in HH:MM:SS AM/PM format (e.g., 02:30:15 PM)')
        return

    def reminder_thread():
        while True:
            now = datetime.now().strftime('%I:%M:%S %p')
            if now == reminder_time:
                messagebox.showinfo('Reminder', f'Time to: {reminder_msg}')
                break
            time.sleep(1)

    threading.Thread(target=reminder_thread, daemon=True).start()
    messagebox.showinfo('Reminder Set', f'Your reminder is set for {reminder_time}')

root = tk.Tk()
root.title('Reminder App (With Seconds)')
root.geometry('320x240')
root.configure(bg='#f9f9f9')

tk.Label(root, text='Enter time (HH:MM:SS AM/PM):', bg='#f9f9f9', font=('Arial', 11, 'bold')).pack(pady=5)
time_entry = tk.Entry(root, font=('Arial', 11))
time_entry.pack(pady=5)

tk.Label(root, text='Enter message:', bg='#f9f9f9', font=('Arial', 11, 'bold')).pack(pady=5)
msg_entry = tk.Entry(root, font=('Arial', 11))
msg_entry.pack(pady=5)

# Stylish Set Reminder button
set_btn = tk.Button(
    root,
    text='Set Reminder',
    command=set_reminder,
    bg='#4CAF50',
    fg='white',
    font=('Helvetica', 12, 'bold'),
    activebackground='#45a049',
    relief='raised',
    borderwidth=3
)
set_btn.pack(pady=15)

root.mainloop()