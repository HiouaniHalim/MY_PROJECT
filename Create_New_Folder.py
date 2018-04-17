import os

__all__ = ['NEW_FOLDER']


class NEW_FOLDER (object):
    """
    This Category Contains A Lot Of Diagrams Where :
        __set__ = You change the current path to the parent path with an increase by ' \directory/ '
        __enter__ = Check for file presence '' self.__CHECK__ ''
    """

    __slots__ = {'__CHECK__', '__OS__', '__CHECK__2'}

    def __init__(self, CHACK_NAME_OF_FOLDER_NEW):
        self.__CHECK__ = "C:\Users\Hlim\Desktop\directory/"
        self.__CHECK__2 = CHACK_NAME_OF_FOLDER_NEW

    def __set__(self, __RETURN__=os.path.expanduser ('~\Desktop').__add__ ('\directory/')):   # FINISH THIS IS FUNCTION
        self.__CHECK__ = __RETURN__
        # print('NEW PATH' + self.__CHECK__)
        return self.__CHECK__

    def x(self, _RETURN_=os.path.expanduser ('~\Desktop').__add__ ('\directory\CONSTANT/')):
        """"""
        self.__CHECK__2 = _RETURN_
        return self.__CHECK__2

    def __enter__(self):                 # FINISH THIS IS FUNCTION
        # var = super, the_definition
        if not os.path.exists (self.__CHECK__ and self.__CHECK__2):                  # PROGRAMMER BY HALIM__HIOUANI
            os.makedirs (self.__CHECK__)                # C:\\Users\\Hlim\\Desktop\\directory
            os.makedirs (self.__CHECK__2)                # C:\\Users\\Hlim\\Desktop\\directory\\COSTANT
        else:
            pass
