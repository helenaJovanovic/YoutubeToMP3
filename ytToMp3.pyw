import youtube_dl
import threading
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askdirectory


class MAIN:
    def __init__(self):
        self.root = Tk()
        self.root.iconbitmap("file.ico")
        
        self.URL = StringVar()
        self.PATH = StringVar()

        self.root.geometry("640x310")
        self.root.resizable(False, False)
        self.root.title("Youtube To MP3")
    
        self.AddWidgets()
        
        self.root.mainloop()


    def AddWidgets(self):
        self.BLANK_1 = Label(self.root).pack()
        self.BLANK_2 = Label(self.root).pack()
        self.enterURL = Label(self.root, text="Youtube URL:", font= ('Georgia', '14', 'italic')).pack()
        self.entryURL = Entry(textvariable=self.URL, width=40, font=('Georgia', 12)).pack()


        self.BLANK_3 = Label(self.root).pack()
        self.BLANK_4 = Label(self.root).pack()
        self.enterPATH = Label(self.root, text="Choose Download Folder:", font= ('Georgia', '14', 'italic')).pack()
        self.entryPATH = Entry(textvariable=self.PATH, width=40, font=('Georgia', 12))
        self.entryPATH.bind("<Button-1>", self.PathChooser)
        self.entryPATH.pack()

    
        self.BLANK_5 = Label(self.root).pack()
        self.BLANK_6 = Label(self.root).pack()
        self.submit = Button(self.root, text = "Download", command=self.initiateDownload)
        self.submit.pack(ipady=15, ipadx=50)

        
    def PathChooser(self, args):
        self.directory = askdirectory()
        self.entryPATH.delete(0, END)
        self.entryPATH.insert(0, self.directory)

    def Progress(self, d):
        if d['status'] == 'finished':
            Label(self.new_window).pack()
            converting = Label(self.new_window, text="Unpacking and converting", font= ('Georgia', '14', 'italic')).pack()
        elif d['status'] == 'downloading':
            #turn the logging on, and then parse logging.log file for download percentage
            
            self.progress_bar["value"] +=5
            if (self.progress_bar["value"]>=100):
                self.progress_bar["value"] = 0
            if d['total_bytes'] == None:
                byt = "Unknown"
            else:
                byt = str(int(d['total_bytes']/1024/1024))

            
            self.info.config(
                text = "Elapsed:  " + str(int(d['elapsed'])) +"s,  ETA:  " + str(int(d['eta'])) + "s,  Speed:  " + str(int(d['speed']/1024))+
                "MBps,  Size:  " + byt +" MB"
            )
        
    
    def initiateDownload(self):
        new_thread = threading.Thread(target=self.Download)
        new_thread.start()
        
    def Download(self):
        
        URL = self.URL.get()
        
        
        self.new_window = Toplevel()
        self.new_window.geometry("400x250")
        self.new_window.iconbitmap("file.ico")
        self.new_window.title("Download Progress")
        self.new_window.attributes('-topmost', 'true')

        Label(self.new_window).pack()
        Label(self.new_window).pack()
        Label(self.new_window, text="Progress: ", font=('Georgia', '14', 'italic')).pack()
        
        self.progress_bar = Progressbar(self.new_window, orient="horizontal", length = 300, mode="determinate")
        self.progress_bar.pack()
        self.progress_bar["maximum"] = 100
        self.progress_bar["value"] = 0
        self.info = Label(self.new_window)
        self.info.pack()

        self.settings = {
            'outtmpl':self.directory + '/%(title)s.%(ext)s',
            'progress_hooks': [self.Progress],
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '256',}]
        }
        
        with youtube_dl.YoutubeDL(self.settings) as ydl:
            ydl.download([URL])

        self.new_window.destroy()


Start = MAIN()
