import tkinter as tk

class MainWindow():
	def __init__(self):
		self.r = tk.Tk()
		self.width = 1024
		self.height = 512
		self.color = '#FFFFFF'
		self.r.geometry(str(self.width) + 'x' + str(self.height))
		self.r.title('TO DO List for CKH only by Tony Liang & ...')
	def mainloop(self):
		self.r.mainloop()

main = MainWindow()
main.mainloop()
