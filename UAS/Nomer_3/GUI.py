import tkinter as tk

class App:
    def _init_(self, master):
        frame = tk.Frame(master)
        frame.pack()
        self.hi_there = tk.Button(frame, text="Biodata Mahasiswa", command=self.say_hi)
        self.hi_there.pack(side=tk.LEFT)

    def say_hi(self):
        print ("Nama : Anton Nurfendi")
        print ("NIM : 20210801242")
        print ("Fakultas : Ilmu Komputer")
        print ("Prodi : Teknik Informatika")

root = tk.Tk()

root.title("Bahasa Pemograman")
root.geometry("300x50")
app = App(root)
root.mainloop()