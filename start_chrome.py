import sys
import subprocess

port = 8989
browser = "chrome"

if sys.platform == 'linux':
    browser="chromium"

subprocess.run(
    [browser, f"--remote-debugging-port={port}"], 
    shell=False,
    capture_output=False,
)
