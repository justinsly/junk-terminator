@ECHO OFF

TITLE terminator

ECHO starting terminator...

ECHO ===========================

:: this single command shall not be touched
:: in any condition since its required to run as admin
CD %~dp0

PYTHON terminator.py

ECHO exiting...

TIMEOUT /t 1 /nobreak >nul