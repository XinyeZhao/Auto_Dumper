import pygdbmi
import psutil
import os

class ProcessManager:
    def __init__(self):
        self.procDict = self.pidDictBuilder()

    def pidDictBuilder(self):
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
        for i in self.procDict.items():
            print('PID: ',i[1],', PROCESS NAME:', i[0])

    def processKiller(self, name):
        flag = False
        for i in self.procDict.items():
            process_name = i[0]
            pid = i[1]
            if name == process_name:
                flag = True
                p = psutil.Process(pid)
                p.kill()
                print("Sucessfull Killing!", pid)
                break

        if not flag:
            print('Process Not Found:', name)

class GDBManager:
    def __init__(self):
        pass

def main():
    process_manager = ProcessManager()
    process_manager.showAllProcInfo()
    process_manager.processKiller('wallpaper32.exe')

if __name__ == '__main__':
    main()