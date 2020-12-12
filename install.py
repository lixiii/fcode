import os 
import shutil 
import json 
import argparse
from glob import glob

# initial check
bpath = os.path.expanduser("~/.vscode/extensions")
if not os.path.isdir(os.path.join(bpath)):
    raise RuntimeError(f"Visual Studio Code extensions folder ({bpath}) not found. ")

with open('./package.json', 'r') as f: 
    packageJSON = json.load(f)

print(f"Installing fabrica.ai fcode extension version {packageJSON['version']}")

ipath = os.path.join(bpath, f"fabrica.ai-fcode-{packageJSON['version']}")

print(f"Installing extension to {ipath}")

if os.path.isdir(ipath): 
    input(f"[WARNING] The path {ipath} already exists. Press Enter to overide contents in the path or Ctrl+C to exit. ")
    if not os.path.isdir(os.path.join(ipath,"syntaxes")):
        os.mkdir(os.path.join(ipath,"syntaxes")) 
else: 
    os.mkdir(ipath) 
    os.mkdir(os.path.join(ipath,"syntaxes")) 

shutil.copy("./syntaxes/fcode.tmLanguage.json",os.path.join(ipath,"syntaxes"))
shutil.copy("./language-configuration.json",ipath)
shutil.copy("./package.json",ipath)
shutil.copy("./README.md",ipath)
shutil.copy("./CHANGELOG.md",ipath)

print("Installation complete. Please restart visual studio code to load extension. ")