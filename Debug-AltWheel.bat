@echo off
rem Starts Alt Wheel with a visible log window, to find out why something doesn't work.
cd /d "%~dp0"
where py >nul 2>nul && (py -m altwheel --debug) || (python -m altwheel --debug)
pause
