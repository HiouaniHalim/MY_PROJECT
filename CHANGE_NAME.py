# C:\\Users\\Hlim\\Desktop\\directory\\TEXT.rtf
import os                                               # HALIM - HIOUANI


try:   # Python 2
    from Tkinter import Tk
    from tkSimpleDialog import askstring
except ImportError:   # Python 3

    from tkinter import Tk
    from tkinter.simpledialog import askstring


class PATH:
    def __init__(self):
        # self._NAME_ = NAME
        self._ORIGINAL_NAME_ = 'directory'
        self._a_ = os.path.expanduser ('~\Desktop')
        os.chdir (self._a_)
        self._i_ = ''
        self._A_ = ''
        self._NAME_ = ''
        self.__C__ = ''
        self.text = ''
        # This is the original name of the FOLDER

    def RETURN_FOLDER_NAME(self):
        """"""
        a = os.path.expanduser ('~\Desktop')
        os.chdir (a)

        for i in os.listdir (a):
            x = i.__add__ ('\TEXT')
            if os.path.exists (x):
                e = os.path.dirname (x)
                print(e)
                self._ORIGINAL_NAME_ = e
                print(self._ORIGINAL_NAME_)
                return self._ORIGINAL_NAME_

    def ROOT(self):
        root = Tk ()
        root.geometry ('50x30+500+200')
        root.withdraw ()  # hide main window
        text = askstring ("CHANGE_NAME_FOLDER", "Name :")
        self.text = text

    def c(self):
        for x in os.listdir(self._a_):
            if os.path.isdir (x):
                for self._i_ in os.listdir(x):
                    if self._i_.rpartition('.')[-1] == 'rtf':
                        _SPLIT_ = os.path.splitext(self._i_)
                        for a in os.listdir(self._a_):
                            A = a.__add__('\\' + self._i_)
                            if os.access(A, os.F_OK):
                                # print(A + '  100')
                                self._A_ = A
                                return self._A_

    def s(self):
        T = os.path.split (self._A_)
        print(T[0])
        self._ORIGINAL_NAME_ = T[0]
        return self._ORIGINAL_NAME_

    def CHANGE(self):

        os.rename(self._ORIGINAL_NAME_, self.text)    # self._NAME_ = ' NAME '
        # self.a.replace(self.a, self._NAME_)
