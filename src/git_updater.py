# src/git_updater.py
from git import Repo
import datetime

def commit_and_push():
    repo = Repo.init(".")
    repo.git.add("--all")
    repo.index.commit(f"Auto update: {datetime.datetime.now()}")
    origin = repo.remote(name='origin')
    origin.push()
    print("Pushed to GitHub")
