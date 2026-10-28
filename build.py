"""Build AltWheel.exe with PyInstaller:  python build.py   (run it from this folder)"""
import os
import shutil
import subprocess
import sys

here = os.path.dirname(os.path.abspath(__file__))
web = os.path.join(here, "web")
repo = os.path.abspath(os.path.join(here, ".."))

# Preserve local website assets if already bundled. Never delete a user's
# working web folder during an EXE build.
if not os.path.isfile(os.path.join(web, 'index.html')):
    os.makedirs(web, exist_ok=True)
    for item in ('index.html', 'css', 'js', 'assets'):
        src = os.path.join(repo, item)
        dest = os.path.join(web, item)
        if os.path.isdir(src) and not os.path.exists(dest):
            shutil.copytree(src, dest)
        elif os.path.isfile(src):
            shutil.copy2(src, dest)
if not os.path.isfile(os.path.join(web, 'index.html')):
    raise SystemExit('Missing web/index.html: restore the web folder before building.')

sep = ";" if os.name == "nt" else ":"
cmd = [
    sys.executable, "-m", "PyInstaller", "--noconfirm", "--onefile", "--windowed",
    "--name", "AltWheel",
    "--add-data", "web%sweb" % sep,
    "--collect-all", "uiautomation", "--collect-all", "comtypes",
    "--collect-all", "imageio_ffmpeg", "--collect-data", "docx", "--collect-data", "pptx", "--collect-data", "openpyxl",
    "--hidden-import", "pystray._win32",
    "--exclude-module", "numpy", "--exclude-module", "matplotlib",
    "--exclude-module", "scipy", "--exclude-module", "pandas",
    "altwheel.pyw",
]
print("Building... this takes a few minutes.")
subprocess.check_call(cmd, cwd=here)
print("\nDone. Your app is dist" + os.sep + "AltWheel.exe")
