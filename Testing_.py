#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# PROGRAMMER BU HALIM__HIOUANI  FROM ALGERIA

from Tkinter import *
import ttk


def CHACK():
    """ RUN FILE.PY 'aaa.py' """
    ARRAY = ['a', 'a']
    if ENTRY_A.get () == ARRAY[0] and ENTRY_B.get () == ARRAY[1]:
        # print('yes')
        root.destroy()
        import aaa
    else:
        """ If the secret slavery is wrong this text will appear """

        LABEL_C.config (text='USERNAME OR PASSWORD IS INCORRECT')


root = Tk ()
root.title ('Login')
root.geometry ('500x400+400+70')
root.wm_iconbitmap ('LOGIN/images.ico')
# root.attributes ("-transparent color", "black")  # جعل الشاشة شفافة
root.configure (bg='#3D3D3D')

s = ttk.Style ()
s.configure ('c.TFrame', background='#3D3D3D')
s.configure ('c.TLabel', background='#3D3D3D', foreground='white')
s.configure ('C.TLabel', background='#6C6C6C', foreground='black')
s.configure ('N.TLabel', background='#3D3D3D', foreground='red')

FRAME = ttk.Frame (root, width=400, height=350, style='c.TFrame')
xf = ttk.Frame (FRAME, relief=GROOVE, borderwidth=2, style='c.TFrame')

ENTRY_A = ttk.Entry (xf, width=20, style='C.TLabel')
ENTRY_A.focus_force ()
ENTRY_A.bind ('<Return>', CHACK)
ENTRY_A.place (x=130, y=80)

ENTRY_B = ttk.Entry (xf, width=20, show='*', style='C.TLabel')
ENTRY_B.bind ('<Return>', CHACK
              )
ENTRY_B.pack (padx=130, pady=120)

LABEL_A = ttk.Label (xf, text='NAME :', style='c.TLabel').place (x=60, y=80)
LABEL_B = ttk.Label (xf, text='PASS :', style='c.TLabel').place (x=60, y=120)
LABEL_C = ttk.Label (xf, text='', style='N.TLabel')
LABEL_C.place (x=50, y=190)

BUTTON0 = ttk.Button (xf, text='Check', command=lambda: CHACK(), width=7)
BUTTON0.place (x=320, y=225)
xf.place (relx=0.01, rely=0.125, anchor=NW)

ttk.Label (FRAME, text='PAGE LOGIN', style='c.TLabel').place (relx=.06, rely=0.125, anchor=W)

FRAME.pack ()

ttk.Button (root, text='Quit', command=root.destroy, width=4).place (x=445, y=365)

root.mainloop ()

# root.configure (bg='black')
# root.attributes ('-topmost', 1)
# root.attributes ("-alpha", 1)
