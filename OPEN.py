import os
import tkMessageBox
import shutil

try:   # Python 2
    from Tkinter import Tk
    from tkSimpleDialog import askstring
except ImportError:   # Python 3

    from tkinter import Tk
    from tkinter.simpledialog import askstring            # if you are use Python 3 run and remove '#'

__all__ = ['GET', '__OPEN__']


class GET(object):
    __slots__ = ['__get__path__', 'c', '_a_', '_A_', '__C__', '_i_', '_NAME_']

    def __init__(self):
        # super(_GET_, self).__init__()
        # self._GET_ = self.__get__path__                # 'C:\\Users\\Hlim\\Desktop\\directory\\TEXT.rtf'
        self._a_ = os.path.expanduser ('~\Desktop')
        os.chdir (self._a_)
        self._i_ = ''
        self._A_ = ''
        self._NAME_ = ''
        self.__C__ = ''

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
                            else:
                                pass
                        self._i_ = _SPLIT_[0]
                        # print(self._i_ + ' 1')
                        return self._i_

    def MOV(self):
        self.__C__ = self._a_.__add__ ('\\' + self._A_)
        c = self.__C__ .split('\\')
        # print(c[5])
        x = self.__C__ .replace(c[5], 'CONSTANT')
        # print(x)
        # print(__C__)
        shutil.move(self.__C__, x)
        return self.__C__

    def INPUT_NAME(self):
        root = Tk ()
        root.geometry ('50x30+500+200')
        root.withdraw ()  # hide main window
        text = askstring ("CHANGE_NAME_FOLDER", "Name :")
        self._NAME_ = text
        return self._NAME_

    def Create_New_File(self):
        __C__ = self._a_.__add__ ('\\' + self._A_)
        __PH__ = os.path.split(__C__)
        CREATE_FILE = open (__PH__[0] + '\\' + self._NAME_ + '.rtf', 'a+')


class __OPEN__ (object):
    """"""

    def __init__(self):
        # super(__OPEN__, self).__init__()
        # super(__OPEN__, self).c()
        # self.__c__ = self.__C__
        # print(self.__c__)
        self.__get__path__ = 'C:\\Users\\Hlim\\Desktop\\directory\\TEXT.rtf'
        self.c = ''
        self._a_ = os.path.expanduser ('~\Desktop')
        os.chdir (self._a_)
        self._i_ = ''
        self._A_ = ''
        self.__C__ = ''

    def CHANGE(self):                               # PROBLEM
        # print(self.__get__path__)
        if os.path.exists(self.__get__path__):
            # print(self.__get__path__, ' -> if')
            return self.__get__path__

        elif os.path.exists(self.__get__path__):
            a = os.path.expanduser ('~\Desktop')
            os.chdir (a)
            for i in os.listdir (a):
                if os.path.isdir(i):
                    x = i.__add__ ('\\TEXT.rtf')
                    if os.path.exists(x):
                        N = self._a_.__add__('\\' + x)
                        self.__get__path__ = N
                        # print(self.__get__path__, ' -> elif')
                        return self.__get__path__
        else:
            for x in os.listdir (self._a_):
                if os.path.isdir (x):
                    for self._i_ in os.listdir (x):
                        if self._i_.rpartition ('.')[-1] == 'rtf':
                            for a in os.listdir (self._a_):
                                A = a.__add__ ('\\' + self._i_)
                                if os.access (A, os.F_OK):
                                    self.__get__path__ = A
                                    # print(self.__get__path__, ' else')
                                    return self.__get__path__
                                else:
                                    pass

    def __str__(self):
        # print(self.__get__path__, 'x')
        if os.path.exists(self.__get__path__):
            os.system (self.__get__path__)
        else:
            tkMessageBox.showinfo(title='warning', message='This file does not exist')
