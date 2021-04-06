import subprocess
__version__ = subprocess.check_output(["git", "describe", '--abbrev=8', '--always', 'HEAD']).strip()
