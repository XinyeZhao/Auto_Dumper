from GDBManager import GDBManager
import sys
import subprocess
import os

def prompt():
    print("Usage: python auto_dumper.py [breakpoint address in hex] [path to malware executable]")

def write_dump(proc_name, dmp_file_name):
    subproc = subprocess.Popen(['./procdump/procdump.exe', '-ma', '-w', f'{proc_name}', f'{dmp_file_name}.dmp'])
    return subproc.wait()

def path_parser(path_name):
    '''
    Parse the path to get the execution file name
    e.g. path_parser(r'../folderA/folderB/folderC/folderD/aa.py') -> aa.py
    '''
    file_name = os.path.basename(os.path.normpath(path_name))
    return file_name

def main():
    if(len(sys.argv) != 3):
        prompt()
        return
    
    addr = sys.argv[1]
    try:
        int(addr, base=16)
    except:
        prompt()
        return
    path = sys.argv[2]
    
    print("Launching gdb subprocess...")
    gdb_manager = GDBManager()
    print("gdb launched successfully.")

    # read symbol tables
    print("Reading symbols...")
    output = gdb_manager.exec(f'file {path}')
    print(f"Response for reading symbols from {addr}:")
    print(output)

    # add breakpoint
    print("Adding break point...")
    output = gdb_manager.exec(f'break *{addr}')
    print(f"Response for adding breakpoint at {addr}:")
    print(output)

    # run
    print(f"Starting {path}...")
    output = gdb_manager.exec("run")
    print(f"Response for running {path}:")
    print(output)

    # remove breakpoint
    print("Removing break point...")
    output = gdb_manager.exec(f'del 1')
    print(f"Response for removing breakpoint at {addr}:")
    print(output)

    # wait for user to take memory dump
    print("\n")
    print(f"Writing memory dump for {path}...")
    file_name = path_parser(path)
    exit_code = write_dump(path, file_name)
    print(f"Finished writing memory dump. Exited with code: {exit_code}")

    gdb_manager.exit()

    

if __name__ == '__main__':
    main()
