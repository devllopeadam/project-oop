import tkinter as tk


class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Frame Switching Example")

        self.frame = tk.Frame(self)
        self.frame.pack(fill="both", expand=True)

        self.current_frame = None

        self.create_frame1()
        self.create_frame2()

        self.show_frame(self.frame1)

    def create_frame1(self):
        self.frame1 = tk.Frame(self.frame)

        label = tk.Label(self.frame1, text="Frame 1", font=("Helvetica", 18))
        label.pack(pady=20)

        button = tk.Button(self.frame1, text="Show Frame 2", command=self.show_frame2)
        button.pack()

    def create_frame2(self):
        self.frame2 = tk.Frame(self.frame)

        label = tk.Label(self.frame2, text="Frame 2", font=("Helvetica", 18))
        label.pack(pady=20)

        button = tk.Button(self.frame2, text="Show Frame 1", command=self.show_frame1)
        button.pack()

    def show_frame(self, frame):
        if self.current_frame:
            self.current_frame.pack_forget()  # Hide the current frame
        self.current_frame = frame
        self.current_frame.pack(fill="both", expand=True)

    def show_frame1(self):
        self.show_frame(self.frame1)

    def show_frame2(self):
        self.show_frame(self.frame2)


if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
