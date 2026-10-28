@echo off
rem Makes dist\AltWheel.exe (one file you can copy anywhere). Needs Python installed on this PC.
cd /d "%~dp0"
where py >nul 2>nul && (set PY=py) || (set PY=python)
%PY% -m pip install -r requirements.txt pyinstaller
%PY% build.py
pause
