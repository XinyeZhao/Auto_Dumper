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

When you see the message: `Waiting for you to take a memory dump...`, you can take a memory dump of the running malware process via various means, e.g. task manager.

After you have taken the memory dump, enter any input, and Auto_Dumper will kill the subordinate malware process, exit gdb, and terminate itself.