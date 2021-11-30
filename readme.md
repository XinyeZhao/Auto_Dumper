#### 

# Documentation for Auto_Dumper

## 1. Sturcture

+ class ProcessManager:
  - Manage process, search process PID and kill process
+ class GDBManager:
  - Manage GDB, to insert and remove breakpoints
  - Unfinished...

## 2. Using Auto_Dumper

### 1. For Windows:

In main function, showAllProcInfo method will list all current process with PID

```
process_manager.showAllProcInfo()
```

For killing a process, simply using 

```
process_manager.processKiller('the process name')### 3. For Linux:
```

### 2. For Linux:
