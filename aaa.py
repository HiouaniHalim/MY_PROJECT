from Tkinter import *
import ttk
from Create_New_Folder import *
from DELETE__FILE import *
import time
import OPEN
from CHANGE_NAME import *
import Pmw

__all__ = ['the_definition', 'FUNCTION_RETURN', 'RESET']


class the_definition (object):
    """
    This breed is responsible for making file data storage
    """
    __slots__ = ['_name_', '_last_N_', '_AGE_', '__OS__', '_a_', '_i_', '_A_', '_NAME_']

    def __init__(self, _NAME, _LAST_, _age_):
        self._name_ = _NAME
        self._last_N_ = _LAST_
        self._AGE_ = _age_
        self.__OS__ = 'C:\\Users\\Hlim\\Desktop\\directory\\TEXT.rtf'
        self._a_ = os.path.expanduser ('~\Desktop')
        os.chdir (self._a_)
        self._i_ = ''
        self._A_ = ''
        self._NAME_ = ''

    def c(self):
        for x in os.listdir (self._a_):
            if os.path.isdir (x):
                for self._i_ in os.listdir (x):
                    if self._i_.rpartition ('.')[-1] == 'rtf':
                        _SPLIT_ = os.path.splitext (self._i_)
                        for a in os.listdir (self._a_):
                            A = a.__add__ ('\\' + self._i_)
                            if os.access (A, os.F_OK):
                                # print(A + '  100')
                                self._A_ = A
                                return self._A_
                            else:
                                pass
                        self._i_ = _SPLIT_[0]
                        # print(self._i_ + ' 1')
                        return self._i_

    def xx(self):
        __C__ = self._a_.__add__ ('\\' + self._A_)
        self.__OS__ = __C__
        return self.__OS__

    def __copy__(self):
        try:
            # print(the_definition.name_, the_definition.last_N_)
            w = '********'
            CREATE_FILE = open (self.__OS__, 'a+')
            CREATE_FILE.writelines (
                'INFO :\t\t\t' + '** TIME IS : %10s' % time.ctime () + ' ** \n\n' + 'MANE : \t\t\t' + '' + self.name_
                + '\n' + 'LAST NAME : \t\t' + self.last_N_ + '\n' + 'AGE : \t\t\t' + ''
                + self.AGE_ + '\n\n' + w * 8 + '**' + '\n\n')
            """
            while C < a.__len__():
                """"""
                CREATE_FILE.writelines(a[C]+'\n')
                C += 1
            """
            CREATE_FILE.close ()
        except KeyError:
            print('File does not exist')

    @property
    def name_(self):
        return self._name_

    @property
    def last_N_(self):
        return self._last_N_

    @property
    def AGE_(self):
        return self._AGE_


def _OPEN_():
    """"""
    RUN = OPEN.__OPEN__ ()
    RUN.CHANGE ()
    # RUN.R()
    RUN.__str__ ()


def NEW():
    """"""
    a = OPEN.GET ()
    a.c ()
    a.MOV ()
    a.INPUT_NAME ()
    a.Create_New_File ()


def STOKAGE_SAVE():
    """"""
    v1 = ENTRY_A.get ()
    v2 = ENTRY_b.get ()
    v3 = ENTRY_C.get ()
    z = the_definition (_NAME=v1, _LAST_=v2, _age_=v3)
    # z.CHANGE ()
    z.c ()
    z.xx ()
    z.__copy__ ()


def DELETE_DELETE():
    """"""
    D = DELETE ()
    D.CHANGE ()
    D.RUN ()


def CH():
    a = os.path.expanduser ('~\Desktop')
    os.chdir (a)
    for i in os.listdir (a):
        x = i.__add__ ('\TEXT.rtf')
        if os.path.exists (x):
            global BUTTON0
            BUTTON0.configure (state=DISABLED)
        else:
            pass


def ABOUT():
    roo = Tk ()
    roo.geometry ('200x200+500+150')
    roo.withdraw ()
    Pmw.initialise ()
    Pmw.aboutversion ('1.0.1')
    Pmw.aboutcopyright ('Copyright Company Name 1999\nAll rights reserved')
    Pmw.aboutcontact (
        'For information about this application contact:\n' +
        ' Programmer By Halim-Hiouani\n' +
        ' Phone: (+213) 669772530 \n' +
        ' email: Hiouani12345@gmail.com'
    )
    about = Pmw.AboutDialog (roo, applicationname='About Dialog')
    roo.mainloop ()


def H():
    r = Tk ()
    r.withdraw ()
    st = Pmw.ScrolledText (r, borderframe=1, labelpos=N,
                           label_text='Blackmail', usehullsize=1,
                           hull_width=400, hull_height=300,
                           text_padx=10, text_pady=10,
                           text_wrap='none')
    st.importfile ('blackmail.txt')
    st.pack (fill=BOTH, expand=1, padx=5, pady=5)
    r.mainloop ()


def FUNCTION_RETURN():
    # _VAR_ = 'C:\\Users\\Hlim\\Desktop\\directory\\TEXT.txt'
    aw = "C:\Users\Hlim\Desktop\directory\CONSTANT/"
    APP = NEW_FOLDER ( CHACK_NAME_OF_FOLDER_NEW=aw)

    # if os.chdir(os.path.expanduser('~\Desktop')):
    a = os.path.expanduser ('~\Desktop')
    os.chdir (a)
    for i in os.listdir (a):
        x = i.__add__ ('\TEXT.rtf')
        if os.path.exists (x):

            BUTTON0.configure (stat=DISABLED)
        else:
            APP.__set__ ()
            APP.x()
            APP.__enter__ ()

    v1 = ENTRY_A.get ()
    v2 = ENTRY_b.get ()
    v3 = ENTRY_C.get ()
    z = the_definition (_NAME=v1, _LAST_=v2, _age_=v3)
    z.__copy__ ()
    # z.CHANGE ()
    z.c ()
    z.xx ()


class OS_CHECK (NEW_FOLDER):
    def l(self):
        super (NEW_FOLDER.__init__ (), self)


def Switch_Name():
    """"""
    APP = PATH ()
    APP.RETURN_FOLDER_NAME ()
    APP.ROOT ()
    APP.c ()
    APP.s ()
    APP.CHANGE ()


def RESET():
    """"""
    ENTRY_A.delete (0, END)
    ENTRY_b.delete (0, END)
    ENTRY_C.delete (0, END)


root = Tk ()
root.title ('Login')
root.resizable (0, 0)
root.geometry ('500x370+400+70')
root.wm_iconbitmap ('LOGIN/images.ico')
# root.attributes ("-transparent color", "black")
root.configure (bg='#3D3D3D')

# <-- STYLE -->

s = ttk.Style ()
s.configure ('c.TFrame', background='#3D3D3D')
s.configure ('c.TLabel', background='#3D3D3D', foreground='white')
s.configure ('C.TLabel', background='#6C6C6C', foreground='black')

# <-- MENU -->

menu = Menu (root)
root.config (menu=menu)
file_menu = Menu (menu, tearoff=0)
menu.add_cascade (label="File", menu=file_menu)
file_menu.add_command (label="New", command=lambda: NEW ())
file_menu.add_command (label="Open_File", command=lambda: _OPEN_ ())
file_menu.add_separator ()
file_menu.add_command (label="Exit", command=root.quit)

help_menu = Menu (menu, tearoff=0)
menu.add_cascade (label="Help", menu=help_menu)
help_menu.add_command (label="About...", command=lambda: ABOUT ())
help_menu.add_command (label="Help...", command=lambda: H())

# <-- FRAMES -->

FRAME = ttk.Frame (root, width=400, height=350, style='c.TFrame')
xf = ttk.Frame (FRAME, relief=GROOVE, borderwidth=2, style='c.TFrame')

ENTRY_A = ttk.Entry (xf, width=20, style='C.TLabel')
ENTRY_A.focus_force ()
ENTRY_A.bind ('<Return>', FUNCTION_RETURN)  # RETURN TO FUNCTION_RETURN
ENTRY_A.place (x=130, y=80)

ENTRY_b = ttk.Entry (xf, width=20, style='C.TLabel')
ENTRY_b.bind ('<Return>', FUNCTION_RETURN)  # RETURN TO FUNCTION_RETURN
ENTRY_b.pack (padx=130, pady=110)

ENTRY_C = ttk.Entry (xf, width=20, style='C.TLabel', )
ENTRY_C.bind ('<Return>', FUNCTION_RETURN)  # RETURN TO FUNCTION_RETURN3
ENTRY_C.place (x=130, y=140)

LABEL_A = ttk.Label (xf, text='NAME :', style='c.TLabel').place (x=60, y=80)
LABEL_B = ttk.Label (xf, text='L_NAME :', style='c.TLabel').place (x=60, y=110)
LABEL_C = ttk.Label (xf, text='AGE :', style='c.TLabel').place (x=60, y=140)

BUTTON0 = ttk.Button (xf, text='New_Folder', command=lambda: FUNCTION_RETURN (), width=12)
CH ()
BUTTON0.place (x=295, y=210)

BUTTON1 = ttk.Button (xf, text='SAVE-DATA', command=lambda: STOKAGE_SAVE (), width=11).place (x=215, y=210)

BUTTON_A = ttk.Button (xf, text='DELETE-F', command=lambda: DELETE_DELETE (), width=10).place (x=141, y=210)

BUTTON_B = ttk.Button (xf, text='RE-DIR', command=lambda: Switch_Name (), width=8).place (x=78, y=210)

BUTTON_C = ttk.Button (xf, text='Reset', command=lambda: RESET (), width=6).place (x=27, y=210)

xf.place (relx=0.01, rely=0.125, anchor=NW)

ttk.Label (FRAME, text='THE INFORMATION', style='c.TLabel').place (relx=.06, rely=0.125, anchor=W)

FRAME.pack ()

ttk.Button (root, text='Quit', command=root.destroy, width=5).place (x=450, y=315)

root.mainloop ()
