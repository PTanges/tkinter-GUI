import tkinter
import tkinter.messagebox

class scoreAveragerGUI:
    def __init__(self):
        self._mainWindow = tkinter.Tk()
        self._mainWindow.title("Scores")

        self._frame1 = tkinter.Frame(self._mainWindow)
        self._frame2 = tkinter.Frame(self._mainWindow)
        self._frame3 = tkinter.Frame(self._mainWindow)
        self._frame4 = tkinter.Frame(self._mainWindow)
        self._frame5 = tkinter.Frame(self._mainWindow)

        self._label1 = tkinter.Label(self._frame1, text="Score for Test 1:", relief="solid")
        self._label2 = tkinter.Label(self._frame2, text="Score for Test 2:", relief="solid")
        self._label3 = tkinter.Label(self._frame3, text="Score for Test 3:", relief="solid")
        self._label4 = tkinter.Label(self._frame4, text="Average:")
        self._avgLbl = tkinter.StringVar()
        self._label5 = tkinter.Label(self._frame4, textvariable=self._avgLbl)

        self._label1.pack(ipadx=15, ipady=5, side="left")
        self._label2.pack(ipadx=15, ipady=5, side="left")
        self._label3.pack(ipadx=15, ipady=5, side="left")
        self._label4.pack(ipadx=5, ipady=5, side="left")
        self._label5.pack(ipadx=5, ipady=5, )

        self._entry1 = tkinter.Entry(self._frame1)
        self._entry2 = tkinter.Entry(self._frame2)
        self._entry3 = tkinter.Entry(self._frame3)
        self._entry1.pack(padx=15, pady=15, side="left")
        self._entry2.pack(padx=15, pady=15, side="left")
        self._entry3.pack(padx=15, pady=15, side="left")

        self._avgButton = tkinter.Button(self._frame5, text="Calculate Average", command=self.averageScore)
        self._avgButton.pack(padx=15, pady=15, side="left")

        self._frame1.pack(padx=15, pady=5)
        self._frame2.pack(padx=15, pady=5)
        self._frame3.pack(padx=15, pady=5)
        self._frame4.pack(padx=15, pady=5)
        self._frame5.pack(padx=15, pady=5)

        tkinter.mainloop()
    '''
    @property
    def avg(self):
        return self._avg

    @avg.setter
    def avg(self, avg):
        self._avg = avg
    '''

    def averageScore(self):
        self._avgLbl.set("")
        score1 = self._entry1.get()
        score2 = self._entry2.get()
        score3 = self._entry3.get()

        try:
            score1 = float(score1)
            score2 = float(score2)
            score3 = float(score3)

            avg = (score1 + score2 + score3)/3.0

            # Truncate to 1 or 2 decimal places without rounding
            sAvg = ""
            tempString = str(avg)
            for index in range(len(tempString)):
                if tempString[index] == ".":
                    sAvg += tempString[index]
                    sAvg += tempString[index + 1]
                    if (index+2) < len(tempString):
                      sAvg += tempString[index+2]
                    break
                else:
                    sAvg += tempString[index]


            avg = float(sAvg)
            self._avgLbl.set(avg)
            # self._label5.set(self._avg)
            # self._stringAvg = tkinter.StringVar()
            # tkinter.messagebox.showinfo('Title', "Text")
        except:
            tkinter.messagebox.showerror('Error', "Please enter a number")


'''
5 Frames
3 Labels + 3 Entry
2 Labels + StringVar & textVariable
1 Button
'''