@echo off
IF [%1] EQU [] GOTO v2
IF [%2] EQU [] GOTO v2
GOTO v2

:v1
echo no argument
Pause
Exit 0

:v2
echo Execute
REM pip install -r requirements.txt
py webClick.py
REM Pause
REM Exit 0