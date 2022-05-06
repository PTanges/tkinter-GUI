import tkinter

class myGUI:
	def __init__(self):
		self._main_window = tkinter.Tk()

		self._main_window.title("My first GUI")

		self._label1 = tkinter.Label(self._main_window, text="This is my first GUI program!", relief = "solid")
		self._label1.pack(padx=15, pady=20, ipadx=10, ipady=10)
		tkinter.mainloop()