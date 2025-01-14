import tkinter as tk
from datetime import datetime

class Stopwatch:
    def __init__(self, parent, title):
        # Initialize stopwatch state
        self.counter = 21600
        self.running = False
        
        # Create frame for this stopwatch
        self.frame = tk.Frame(parent, bg="lightgray", padx=5, pady=5)
        self.frame.pack(side="top", fill="x", padx=10, pady=10)

        # Title label
        self.title_label = tk.Label(self.frame, text=title, font="Verdana 12 bold", bg="lightgray")
        self.title_label.pack()

        # Time display label
        self.label = tk.Label(self.frame, text="Welcome", fg="black", font="Verdana 20 bold", bg="lightgray")
        self.label.pack()

        # Control buttons
        self.buttons_frame = tk.Frame(self.frame, bg="lightgray")
        self.buttons_frame.pack()

        self.start_button = tk.Button(self.buttons_frame, text="Start", width=6, command=self.start)
        self.start_button.pack(side="left", padx=5)

        self.stop_button = tk.Button(self.buttons_frame, text="Stop", width=6, state="disabled", command=self.stop)
        self.stop_button.pack(side="left", padx=5)

        self.reset_button = tk.Button(self.buttons_frame, text="Reset", width=6, state="disabled", command=self.reset)
        self.reset_button.pack(side="left", padx=5)

    def update_display(self):
        if self.running:
            if self.counter == 21600:
                display = "starting..."
            else:
                tt = datetime.fromtimestamp(self.counter)
                display = tt.strftime("%H:%M:%S")
            self.label["text"] = display
            self.counter += 1
            self.label.after(1000, self.update_display)

    def start(self):
        self.running = True
        self.update_display()
        self.start_button["state"] = "disabled"
        self.stop_button["state"] = "normal"
        self.reset_button["state"] = "normal"

    def stop(self):
        self.running = False
        self.start_button["state"] = "normal"
        self.stop_button["state"] = "disabled"
        self.reset_button["state"] = "normal"

    def reset(self):
        self.counter = 21600
        if not self.running:
            self.reset_button["state"] = "disabled"
            self.label["text"] = "Welcome"
        else:
            self.label["text"] = "starting..."

# Main application
root = tk.Tk()
root.title("Multiple Stopwatches")
root.geometry("400x600")

# Create multiple stopwatches
stop_titles = ['courses', 'projects', 'mother', 'job-related']
for i in range(4):
    Stopwatch(root, title=stop_titles[i])

root.mainloop()
