import os
import sys

def clone_repo(repo_url, destination):
    try:
        os.system(f'git clone {repo_url} {destination}')
        print(f'Repository cloned to {destination}')
    except Exception as e:
        print(f'Error cloning repository: {e}')

def main():
    if len(sys.argv) != 3:
        print("Usage: python clone_github_repo.py <repo_url> <destination>")
        sys.exit(1)

    repo_url = sys.argv[1]
    destination = sys.argv[2]

    clone_repo(repo_url, destination)

if __name__ == "__main__":
    main()
