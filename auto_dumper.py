from ProcessManager import ProcessManager
from GDBManager import GDBManager

def main():
    process_manager = ProcessManager()
    process_manager.showAllProcInfo()
    
    gdb_manager = GDBManager()
    

if __name__ == '__main__':
    main()
