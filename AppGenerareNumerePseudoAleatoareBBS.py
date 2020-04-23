import wx
import sympy
import random
import sys
from datetime import datetime
import threading
import time


class AsyncBBSGenerator(threading.Thread):
    def __init__(self, mb):
        threading.Thread.__init__(self)
        self.mb = mb
        self.bbs = BBS()

    def run(self):
        self.bbs.generate(self.mb)

        time.sleep(2)
        print("Finished background file write.")


class BBS():
    def __init__(self):
        self.x = 3*10**10
        self.y = 4*10**10
        self.seed = random.randint(1, 1e10)

    def writeToBinaryFile(self, content):
        now = datetime.now()
        dt_string = now.strftime("%d%m%Y_%H%M%S")
        with open(dt_string + ".bin", "wb") as file:
            file.write(content.encode('ascii'))

    def nextUsablePrime(self, x):
        p = sympy.nextprime(x)
        while (p % 4 != 3):
            p = sympy.nextprime(p)
        return p

    def generate(self, mb):
        p = self.nextUsablePrime(self.x)
        q = self.nextUsablePrime(self.y)
        M = p*q

        # consideram ca un caracter in fisier ocupa 1 byte
        # astfel data marimea fisierului 'mb' -> mb * 1000000 caractere de scris in fisier
        N = int(float(mb) * 1000000)

        print("\np:\t", p)
        print("q:\t", q)
        print("M:\t", M)
        print("Seed:\t", self.seed)

        x = self.seed

        bit_output = ""
        for _ in range(N):
            x = x * x % M
            b = x % 2
            bit_output += str(b)

        self.writeToBinaryFile(bit_output)


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='AppGenerareNumerePseudoAleatoareBBS')
        self.panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)

        self.label = wx.StaticText(self.panel, label="Dimensiunea(MB) a fisierului obtinut in urma generarii datelor")
        my_sizer.Add(self.label, 0, wx.ALL | wx.CENTER, 5)

        self.text_ctrl = wx.TextCtrl(self.panel)
        my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)

        my_btn = wx.Button(self.panel, label='Genereaza fisier binar!')
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)

        self.info = wx.StaticText(self.panel, label="")
        my_sizer.Add(self.info, 0, wx.ALL | wx.CENTER, 5)

        self.panel.SetSizer(my_sizer)

        self.Show()

    def on_press(self, event):
        value = self.text_ctrl.GetValue()
        if not value:
            self.info.SetLabel("Nu ai introdus nicio valoare!")
        elif not (isInt(value) or isFloat(value)):
            self.info.SetLabel("Valoarea trebuie sa fie de tip int sau float!")
        else:
            self.info.SetLabel(f'Ai introdus {value}MB. Se genereaza fisierul!')
            background = AsyncBBSGenerator(value)
            background.start()
        
        self.panel.Layout()
        # background.join()

def isInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def isFloat(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
