import subprocess

def func_clone_repo(repo, directory):
    output = subprocess.call(['/usr/bin/git', 'clone', repo, directory])
    return output