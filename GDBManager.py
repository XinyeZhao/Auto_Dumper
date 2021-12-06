import pygdbmi

class GDBManager:
    '''
    This class is designed to control GDB, which will be used to insert and/or remove breakpoint,
    '''
    def __init__(self):
        self.controller = pygdbmi.gdbcontroller