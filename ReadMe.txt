By Thomas O'Malley, for the US Geothermal Project

This script organizes geodatabases by state.

It first searches the given directory for all gdb files, and then using the python module shutil, it moves the files into folders by state name.

Requirements:
GDB file names must start with the state abbreviation, ie. ILWellLogs.gdb
Unique names - delete your old geodatabases, remove them from the directory being operated on, or rename them

Use:
Restructuring file systems at state surveys to match, improving interoperability of programs.

Ulterior goal:
Fix broken data links caused by moving map project files to a new computer or drive.  If mxd and gdb files share the same name and are organized under states, then any mxd can be pointed to it's source data by searching the service_gdb\\MapName.gdb in it's parent directory.