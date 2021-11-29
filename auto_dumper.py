import pygdbmi
import psutil
import os

class ProcessManager:
    '''
    This class is designed to manage all process, which will be used to start and kill
    green-cat, and take dump files
    '''
    def __init__(self):
        self.procDict = self.__pidDictBuilder__()

    def __pidDictBuilder__(self):
        '''
        This is used to build the process dict of {'name' : pid}
        '''
        procDict = {}
        pids = psutil.pids()
        for pid in pids:
            p = psutil.Process(pid)
            if not p.name():
                procDict[None] = pid
            else:
                process_name = p.name()
                procDict[process_name] = pid
        return procDict

    def showAllProcInfo(self):
        '''
        Show all process info: name and pid
        '''
        for process_name, pid in self.procDict.items():
            print('PID: ',pid,', PROCESS NAME: ', process_name)

    def processKiller(self, name):
        '''
        Search and kill the process of givin name
        '''
        flag = False
        for process_name, pid in self.procDict.items():
            if name == process_name:
                flag = True
                p = psutil.Process(pid)
                p.kill()
                print("Sucessfull Killing!", pid)
                break

        if not flag:
            print('Process Not Found:', name)

class GDBManager:
    '''
    This class is designed to control the GDB, which will be used to insert breaker,
    remove breaker
    '''
    def __init__(self):
        pass

def main():
    process_manager = ProcessManager()
    process_manager.showAllProcInfo()
    process_manager.processKiller('wallpaper32.exe')

if __name__ == '__main__':
    main()
