# AutoFold
Python program that automatically pauses and unpauses FoldingAtHome when a specified program is launched.

This program works by checking for open programs using psutil. If the program is in the list it will pause FoldingAtHome. If all specified programs are closed the program will unpause FoldingAtHome.

This program makes use of --send-pause and --send-unpause in FAHClient.exe.

## Run using Python
1. Make sure you have "psutil" module installed.
2. Clone repository.
3. Open the "autofold-setup.py" file and follow instructions, which will set up configs.
4. Run "autofold-cli.py", which is the main program.
