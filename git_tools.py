import os
from time import gmtime, strftime

from git import Repo
from git.exc import InvalidGitRepositoryError

def git_init(path, name):
    if InvalidGitRepositoryError:
        Repo.init(os.path.join(path))

def git_add(path, file):
    repo = Repo(str(path))
    repo.index.add(file)
    repo.index.commit('')

    # root_commit = repo.commit(repo.head)
    # commits = list(root_commit.traverse())
    