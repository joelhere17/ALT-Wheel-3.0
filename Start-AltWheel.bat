@echo off
rem Double-click this file to start Alt Wheel. It installs what it needs the first time.
cd /d "%~dp0"
set PY=
where py >nul 2>nul && set PY=py
if not defined PY where python >nul 2>nul && set PY=python
if not defined PY (
  echo Python is not installed yet.
  echo 1. Go to https://www.python.org/downloads/ and install Python.
  echo 2. On the first installer screen, tick "Add python.exe to PATH".
  echo 3. Then double-click this file again.
  start https://www.python.org/downloads/
  pause
  exit /b 1
)
%PY% -c "import PIL, uiautomation, pystray, fitz, docx, pillow_heif, imageio_ffmpeg, openpyxl, pptx" >nul 2>nul
if errorlevel 1 (
  echo Setting up Alt Wheel for the first time. This takes a minute...
  for %%p in (pillow uiautomation pystray pymupdf python-docx pillow-heif imageio-ffmpeg openpyxl python-pptx) do %PY% -m pip install --disable-pip-version-check -q %%p
)
%PY% -c "import PIL, uiautomation, pystray" >nul 2>nul
if errorlevel 1 (
  echo Setup did not finish. Check your internet connection and try again.
  pause
  exit /b 1
)
if "%PY%"=="py" (start "" pyw altwheel.pyw) else (start "" pythonw altwheel.pyw)
echo Alt Wheel is running. Look for its icon by the clock. You can close this window.
timeout /t 4 >nul
