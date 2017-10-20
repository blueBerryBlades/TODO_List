import tkinter
import tkinter.messagebox
import os

class TDL_Entry_Screen_GUI:
    def __init__(self):
        self.main = tkinter.Tk()
        self.main.title('TODO List :)')
        self.main.geometry("250x600")
        self.main.resizable(width=True, height=True)

        self.theList = []
        self.n = tkinter.IntVar()
        self.d = 0

        self.top = tkinter.Frame(self.main)
        self.mid = tkinter.Frame(self.main)
        self.bot = tkinter.Frame(self.main)
        self.listFrame = tkinter.Frame(self.main)

        self.mainLabel = tkinter.Label(self.top, text="What's on the list for today?", font="bold")
        self.entryLabel = tkinter.Label(self.mid, text="Enter task for today")
        self.entry = tkinter.Entry(self.mid)
        self.listLabel = tkinter.Label(self.listFrame)
        self.addBut = tkinter.Button(self.bot, text="Add to list", command=self.add)
        self.startBut = tkinter.Button(self.bot, text="Start", command=self.start)
        self.quitBut = tkinter.Button(self.bot, text="Quit", command=self.quit)

        self.mainLabel.pack(pady=15)
        self.entryLabel.pack(pady=10)
        self.entry.pack(side='left')
        self.addBut.pack(pady=10)
        self.startBut.pack(side='left', pady=10)
        self.quitBut.pack(side='left', pady=10)
        self.listLabel.pack(pady=10)

        self.top.pack()
        self.mid.pack()
        self.bot.pack()
        self.listFrame.pack()

        tkinter.mainloop()

    def add(self):
        text = self.entry.get()
        self.theList.append(text)
        self.entry.delete(0,'end')
        listText = ''
        for item in self.theList:
            listText =listText + item + '\n'
        self.listLabel.configure(text=listText)

    def start(self):
        self.n = len(self.theList)
        self.mainLabel.destroy()
        self.entryLabel.destroy()
        self.entry.destroy()
        self.addBut.destroy()
        self.startBut.destroy()
        self.quitBut.destroy()
        self.listLabel.destroy()

        self.label = tkinter.Label(self.top, text="Let's do this!", font='bold')
        self.statsLabel = tkinter.Label(self.top, text = '0/'+str(self.n))
        self.label.pack(pady=30)
        self.statsLabel.pack()
        
        for item in self.theList:
            self.btn = tkinter.Button(self.mid, text=item)
            self.btn['command'] = lambda button = self.btn: self.complete(button)
            self.btn.pack()

        self.quitBut = tkinter.Button(self.bot, text="Quit", font='bold',command=self.quit)
        self.quitBut.pack(pady=20)

    def complete(self, button):
        button.configure(state='disabled')
        self.d = self.d + 1
        self.statsLabel.configure(text=str(self.d)+'/'+str(self.n))
        if self.d == self.n:
            tkinter.messagebox.showinfo("All done!", "Yay! You finished all your tasks today! \n Now go and relax :)")
        
    def quit(self):
        if tkinter.messagebox.askyesno("Quit", "Are you sure you want to quit?"):
            self.main.destroy()

gui = TDL_Entry_Screen_GUI()



#class class TDL_List_Screen_GUI:
#    def __init__(self):
#        self.main = tkinter.Tk()
#        self.main.title('TODO List :)')
#        self.main.geometry("250x600")
#        self.main.resizable(width=True, height=True)
#
#        self.top = tkinter.Frame(self.main)
#        self.mid = tkinter.Frame(self.main)
#        self.bot = tkinter.Frame(self.main)
#
#        self.label = tkinter.Label(self.top, text="TODO List", font='bold')
#        self.stats = tkinter.Label(self.top)
#        
#        self.btn = ##
#
#        self.start = tkinter.Button
#        self.add
#        self.quit
#
#        self.start.pack()
#        self.add.pack()
#        self.quit.pack()
#
#        self.label.pack()
#        self.stats.pack()
#
#        self.top.pack()
#        self.mid.pack()
#        self.bot.pack()
