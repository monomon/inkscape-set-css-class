import os
import sys

if sys.platform.startswith('linux'):
    dest_path = os.path.join(os.environ['HOME'], '.config', 'inkscape', 'extensions')
elif sys.platform.startswith('win'):
    dest_path = os.path.join(os.environ['APPDATA'], 'inkscape', 'extensions')

current_dir = sys.path[0]

if not os.path.isdir(dest_path):
    print("Target directory does not exist {}".format(dest_path))
    sys.exit()

import shutil
import glob

filenames = []
for ext in ["py", "inx"]:
    filenames.extend(glob.glob(os.path.join(current_dir, "*." + ext)))
# we don't want to copy setup.py
filenames.remove(os.path.join(current_dir, "setup.py"))

print("copying files\n{}\nto destination\n{}".format(filenames, dest_path))

for f in filenames:
    shutil.copy2(f, dest_path)

print("done")
