import ProcessManager
import GDBManager

def main():
    process_manager = ProcessManager()
    process_manager.showAllProcInfo()
    process_manager.processKiller('wallpaper32.exe')

if __name__ == '__main__':
    main()
