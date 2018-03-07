import tkinter as tk
class Demo2:
    
    def __init__(self, master, prevGen):
        self.gen = prevGen + 1
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text = 'New Child', width = 25, command = self.new_window)
        self.button1.pack()
        self.quitButton = tk.Button(self.frame, text = 'Kill Self and Children', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.genLabel = tk.Label(self.frame, text = self.gen, width = 25)
        self.genLabel.pack()
        self.frame.pack()

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow, self.gen)

    def close_windows(self):
        self.master.destroy()

def main(): 
    root = tk.Tk()
    app = Demo2(root, 0)
    root.mainloop()

if __name__ == '__main__':
    main()
