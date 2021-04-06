import subprocess
__version__ = str(subprocess.check_output(["git", "describe", '--abbrev=8', '--always', 'HEAD']).strip())
