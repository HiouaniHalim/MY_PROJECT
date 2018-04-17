import os
import tkMessageBox
import shutil

__all__ = ['DELETE']


class DELETE(object):
    """  DELETE FILE ** TEXT.txt ** """
    def __init__(self):
        self._a_ = os.path.expanduser ('~\Desktop')
        os.chdir (self._a_)
        self.__OS__ = 'C:\\Users\\Hlim\\Desktop\\directory\\TEXT.rtf'
        self._i_ = ''
        self._A_ = ''
        self._NAME_ = ''
        self.__C__ = ''

    def CHANGE(self):
        if os.path.exists(self.__OS__):
            for i in os.listdir (self._a_):
                x = i.__add__ ('\TEXT.rtf')
                if os.path.exists (x):
                    self.__C__ = i
                    return self.__C__
                else:
                    pass
        else:
            for x in os.listdir (self._a_):
                if os.path.isdir (x):
                    for self._i_ in os.listdir (x):
                        if self._i_.rpartition ('.')[-1] == 'rtf':
                            for a in os.listdir (self._a_):
                                A = a.__add__ ('\\' + self._i_)
                                if os.access (A, os.F_OK):
                                    b = os.path.split(A)
                                    self.__C__ = b[0]
                                    # print(self.__C__)
                                    return self.__C__
                                else:
                                    pass

    def RUN(self):
        if os.path.isdir(self.__C__):
            # print(self.__BB__)
            # print(self.a.__add__('\\'+self.__BB__))
            # os.remove('directory')
            # os.system ("rm -rf %s" % self.__BB__)
            shutil.rmtree(self.__C__)
        else:
            tkMessageBox.showerror(title='REMOVE', message='There is no file with this name')
