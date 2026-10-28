# Alt Wheel 3

**A Windows desktop radial menu for converting files and opening editing tools without leaving the desktop.**

Alt Wheel runs in the system tray. Hold **Ctrl + Shift**, left-click a supported file on your Windows desktop, move toward a conversion option, and release. For supported image and document files, press **Space** to switch between the **Convert** and **Tools** wheels.

> **Development disclosure:** Alt Wheel was developed with assistance from **Anthropic Claude** and **OpenAI ChatGPT** for coding, debugging, interface iteration, testing, and documentation. The project maintainer directed the work and tested desktop behavior on Windows. AI assistance is acknowledged rather than represented as independently authored work.

## Features

- Frosted-glass radial menu, hover and pop animations, and Windows tray controls.
- Image conversion and image tools including crop, compression, editing, annotation, metadata, background editing, and redaction.
- PDF conversions and document-specific tools (for example preview, split, merge, rotate, and extraction).
- Word, Excel, PowerPoint, CSV, and TXT support for applicable conversions and document operations.
- Video-to-MP3 extraction for supported video formats; video and MP3 do not use the document Tools wheel.
- Larger, dark, Windows Photos-inspired tool workspace for image editing.
- Converted outputs are written alongside the source file; work on copies when testing.

**Important:** Not every conversion or tool applies to every file format. The menu varies by file type. Office-to-PDF and Office-to-image export require an external **LibreOffice** installation. The desktop shortcut currently operates on the **Windows desktop**, not every File Explorer window. The browser-based image tools may launch in Microsoft Edge or Chrome.

## Project structure

```text
AltWheel3/
├── altwheel/                 Windows hooks, wheel UI, conversion engine and tool windows
│   ├── app.py               Event loop and app coordination
│   ├── shellfile.py         Desktop file lookup (including Windows UI Automation)
│   ├── engine.py            File conversions
│   ├── document_tools.py    Document operations
│   ├── toolbridge.py        Image editor bridge
│   └── ...                  Drawing, overlay, tray and Windows APIs
├── web/
│   ├── index.html           Browser-based editing UI
│   ├── css/                 Editor styles
│   └── js/                  Conversion and image tool logic
├── tests/                   Automated tests
├── .github/workflows/       Windows build and Python checks
├── docs/                    Installation and architecture notes
├── altwheel.pyw             GUI entry point
├── Start-AltWheel.bat       Double-click launcher
├── Debug-AltWheel.bat       Console diagnostics
├── Build-EXE.bat            Local Windows packaging
├── build.py                 PyInstaller configuration
├── requirements.txt         Runtime dependencies
└── requirements-dev.txt     Test and packaging dependencies
```

## Run on Windows

1. Download or clone this repository and open its root folder.
2. Install Python and ensure the `py` launcher is available.
3. Double-click **`Start-AltWheel.bat`**. On first run, it attempts to install required Python packages.
4. Find Alt Wheel in the notification area (possibly behind the **^** button).
5. Hold **Ctrl + Shift**, left-click a supported desktop file and keep the button held; move to a wheel option and release. Press **Space** to show the alternate wheel when available.

To install dependencies manually, use:

```powershell
py -m pip install -r requirements.txt
```

To run diagnostics, double-click `Debug-AltWheel.bat`. Logs are written to `%LOCALAPPDATA%\AltWheel\altwheel.log`.

For setup and troubleshooting, see [docs/INSTALLATION.md](docs/INSTALLATION.md).

## Build a Windows executable

**On a Windows machine:** double-click `Build-EXE.bat`. This installs PyInstaller and builds `dist/AltWheel.exe`.

**On GitHub:** go to **Actions → Build Windows EXE → Run workflow**, then download the build artifact after the run succeeds. The executable is **not code-signed**. Do not bypass Windows security warnings without verifying the source and release.

> The executable has not been verified in this environment on a real Windows desktop. Test the downloadable build yourself before distributing it.

## Testing

```powershell
py -m pip install -r requirements-dev.txt
py -m pytest tests/test_engine.py tests/test_app_flow.py tests/test_documents.py
```

The browser tool integration test may need Playwright and a browser installation; see `tests/test_toolbridge.py` before running it. Automated tests cannot fully verify global desktop hooks and graphical interaction on a physical Windows machine.

## Security and privacy

Most conversion tasks are performed locally. The editor bridge uses a local browser window, and certain optional format support may load a web dependency. Review dependencies and source code before running this application; it is an independently developed project, not a Microsoft product. Never test destructive operations on your only copy of a file.

## Attribution

- **Claude (Anthropic)** and **ChatGPT (OpenAI)** contributed implementation ideas, code, debugging assistance, and design/documentation iterations.
- **Project maintainer:** product requirements, review, integration decisions, and hands-on Windows testing.

No screenshots or image assets are included in this source distribution. The UI generates its graphics at runtime, and the GitHub repository is intentionally text/code-focused.

## License

No open-source license is included yet. **All rights are reserved by default.** If you intend others to copy, modify or redistribute this repository, choose and add an appropriate license after confirming you have the rights to license all included code and dependencies.
