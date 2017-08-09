import os
import sys
import argparse

def install():
    if sys.platform.startswith('linux'):
        dest_path = os.path.join(os.environ['HOME'], '.config', 'inkscape', 'extensions')
    elif sys.platform.startswith('win'):
        dest_path = os.path.join(os.environ['APPDATA'], 'inkscape', 'extensions')

    current_dir = sys.path[0]

    if not os.path.isdir(dest_path):
        print("Target directory does not exist {}. Stopping".format(dest_path))
        return

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

def package():
    if not sys.platform.startswith('linux'):
        print("Packaging only supported in Linux. Stopping")
        return

    import subprocess
    cmd = ["tar", "--create", "--gzip",
           "--exclude-vcs", "--exclude", "*.swp", "--exclude", "*.pyc",
           "--directory", "../", "--verbose",
           "--file", "../inkscape_set_css_class.tar.gz",
           os.path.basename(sys.path[0])
          ]
    print(cmd)
    subprocess.call(cmd)

parser = argparse.ArgumentParser()
parser.add_argument("command", help="command to execute")
args = parser.parse_args()

if args.command == "install":
    install()
elif args.command == "package":
    package()
