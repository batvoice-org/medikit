import git
repo = git.Repo(search_parent_directories=True)
__version__ = repo.git.describe('--abbrev=8', '--always', 'HEAD')