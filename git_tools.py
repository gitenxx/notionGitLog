from git import Repo
import os

def git_init(path, name):
    bare_repo = Repo.init(os.path.join(path, f'{name}'), bare=True)
    assert bare_repo.bare

def git_add(path, file):
    repo = Repo(path)
    repo.index.add(file)
    repo.index.commit("Adding " + file + " to repo")
    # TODO hmmm it's just a sketch

# TODO add OOP ok :----------DDDD