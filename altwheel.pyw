"""Double-click this file (or press Run in Wing) to start Alt Wheel 3."""
import os
import sys

sys.coinit_flags = 2  # COM in apartment mode, as Tk and pywin32 expect

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from altwheel.app import main

main()
