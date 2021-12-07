#### 

# Documentation for Auto_Dumper

## 1. Sturcture

+ class ProcessManager:
  - Manage process, search process PID and kill process
  - Currently unused
+ class GDBManager:
  - Manage GDB, to insert and remove breakpoints

## 2. Using Auto_Dumper

### Dependencies:
It is confirmed that Auto_Dumper works on Windows with [msys2](https://www.msys2.org/). Of course, You also need to install `gdb` on msys2 by `pacman -S gdb`.

You also need to install the following python package(s) in your msys2 environment:
`pip install pygdbmi`

This script relies on [procdump](https://docs.microsoft.com/en-us/sysinternals/downloads/procdump) to take memory dump of running processes. You can find the executables in the `./procdump` folder. You can also download yourself if you wish. Please make sure the `write_dump()` function is invoking the version of procdump that matches your operating system.

### Usage:
`python auto_dumper.py [breakpoint instruction address] [malware exe name]`

After the script terminates, you should find a `.dmp` file in the root directory of the project. If the script reports `Exited with code: 1`, it's expected behavior and your dump file's integrity is not affected.