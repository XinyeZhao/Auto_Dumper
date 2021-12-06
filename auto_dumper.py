from GDBManager import GDBManager
import sys

def prompt():
    print("Usage: python auto_dumper.py [breakpoint address in hex]")

def main():
    if(len(sys.argv) != 2):
        prompt()
        return
    
    addr = sys.argv[1]
    try:
        int(addr, base=16)
    except:
        prompt()
        return
    
    print("Launching gdb subprocess...")
    gdb_manager = GDBManager()
    print("gdb launched successfully.")

    # add breakpoint
    print("Adding break point...")
    output = gdb_manager.exec(f'break {addr}')
    print(f"Response for adding breakpoint at {addr}:")
    print(output)

    # remove breakpoint
    print("Removing break point...")
    output = gdb_manager.exec(f'del 1')
    print(f"Response for adding breakpoint at {addr}:")
    print(output)

    gdb_manager.exit()

    

if __name__ == '__main__':
    main()
