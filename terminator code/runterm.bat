@ECHO OFF

TITLE terminator

ECHO starting terminator...

ECHO ===========================

CD %~dp0

PYTHON terminator.py

ECHO exiting...

TIMEOUT /t 1 /nobreak >nul