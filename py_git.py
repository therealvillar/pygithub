import subprocess
import os


def clone_repository(repo_url, destination_folder):
    """
    Clones a repository from the given URL to the given destination folder using the Git command line tool.
    Returns True if the repository was successfully cloned.
    """
    command = f"git clone {repo_url} {destination_folder}"
    result = subprocess.run(command, shell=True)
    return result.returncode == 0

def add_files(files):
    """
    Adds the given files to the Git staging area using the Git command line tool.
    Returns True if the files were successfully added.
    """
    command = f"git add {files}"
    result = subprocess.run(command, shell=True)
    return result.returncode == 0

def commit_changes(message):
    """
    Commits the changes in the Git staging area with the given message using the Git command line tool.
    Returns True if the changes were successfully committed.
    """
    command = f'git commit -m "{message}"'
    result = subprocess.run(command, shell=True)
    return result.returncode == 0

def push_changes(remote, branch):
    """
    Pushes the changes to the given remote and branch using the Git command line tool.
    Returns True if the changes were successfully pushed.
    """
    command = f"git push {remote} {branch}"
    result = subprocess.run(command, shell=True)
    return result.returncode == 0

def pull_changes(remote, branch):
    """
    Pulls the changes from the given remote and branch using the Git command line tool.
    Returns True if the changes were successfully pulled.
    """
    command = f"git pull {remote} {branch}"
    result = subprocess.run(command, shell=True)
    return result.returncode == 0

def create_branch(branch_name):
    """
    Creates a new branch with the given name using the Git command line tool.
    Returns True if the branch was successfully created.
    """
    command = f"git branch {branch_name}"
    result = subprocess.run(command, shell=True)
    return result.returncode == 0

def switch_branch(branch_name):
    """
    Switches to the branch with the given name using the Git command line tool.
    Returns True if the branch was successfully switched to.
    """
    command = f"git checkout {branch_name}"
    result = subprocess.run(command, shell=True)
    return result.returncode == 0



def create_requirements_file(requirements_file_path):
    """
    Generates a requirements.txt file containing the list of installed packages using pip freeze.
    Returns True if the requirements.txt file was successfully generated.
    """
    command = f"pip freeze > {requirements_file_path}"
    result = subprocess.run(command, shell=True)
    return result.returncode == 0


def generate_gitignore_file(gitignore_file_path, files_to_ignore=None, dirs_to_ignore=None):
    """
    Generates a .gitignore file containing the list of files and directories to ignore in Git.
    Returns True if the .gitignore file was successfully generated.
    """
    with open(gitignore_file_path, "w") as f:
        if files_to_ignore:
            for file in files_to_ignore:
                f.write(file + "\n")
        if dirs_to_ignore:
            for directory in dirs_to_ignore:
                f.write(directory + "/\n")
    return True


