#### 

# Documentation for Auto_Dumper

Auto_dumpter is a supplementary tool for Forecast([GitHub - CyFI-Lab-Public/Forecast: Forecasting Malware Capabilities From Cyber Attack Memory Images](https://github.com/CyFI-Lab-Public/Forecast)), which is for automatically taking memoy dump file of a given windows malware execution file at a given address.

### 1. Dependencies:

It is confirmed that Auto_Dumper works on Windows with [msys2](https://www.msys2.org/). After installing msys2 on your machine, you also need to install `gdb` on msys2 with command

```
pacman -S gdb
```

You also need to install the following python package(s) in your msys2 environment: `

```
pip install pygdbmi
```

This script relies on [procdump](https://docs.microsoft.com/en-us/sysinternals/downloads/procdump) to take memory dump of running processes. You can find the executables in the `./procdump` folder. You can also download yourself if you wish. Please make sure the `write_dump()` function is invoking the version of procdump that matches your operating system.

## 2. Sturcture

+ class ProcessManager:
  - Manage process, search process PID and kill process
  - Currently unused
+ class GDBManager:
  - Manage GDB, to insert and remove breakpoints

## 3. Using Auto_Dumper

To start generating a dump file of a given malware execution file, using command:

```
python auto_dumper.py [breakpoint instruction address] [path to malware.exe ]`
```

For example, the following command will generate a dump file for the `webc2-greencat-2.exe` will generate a dump file： `webc2-greencat-2.exe.dmp` ,in the same root directory of the project.

```
python auto_dumper.py 0x123456 ../path/to/webc2-greencat-2.exe
```

And if the script reports `Exited with code: 1`, it's expected behavior and your dump file's integrity is not affected.
