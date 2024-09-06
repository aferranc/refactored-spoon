# Refactored Spoon

## Development

To start developing this project it is necessary to have the `poetry` package installed:
```
$ pip install poetry
```

The `poetry install` command reads the *poetry.lock* file from the current directory, processes it, and downloads and installs all the libraries and dependencies outlined in that file. If the file does not exist it will look for *pyproject.toml* and do the same.

### Automatically prepare message before commit

It can be desirable to use commitizen for all types of commits (i.e. regular, merge, squash) so that the complete git history adheres to the commit message convention without ever having to call `cz commit`.

To automatically prepare a commit message prior to committing, you can use a **prepare-commit-msg** Git hook:
```
wget -O .git/hooks/prepare-commit-msg https://raw.githubusercontent.com/commitizen-tools/commitizen/master/hooks/prepare-commit-msg.py
chmod +x .git/hooks/prepare-commit-msg
```

To automatically perform arbitrary cleanup steps after a successful commit you can use a **post-commit** Git hook:
```
wget -O .git/hooks/post-commit https://raw.githubusercontent.com/commitizen-tools/commitizen/master/hooks/post-commit.py
chmod +x .git/hooks/post-commit
```

A combination of these two hooks allows for enforcing the usage of commitizen so that whenever a commit is about to be created, commitizen is used for creating the commit message.

Running `git commit` or `git commit -m "..."` for example, would trigger commitizen and use the generated commit message for the commit.

**Features**

* Commits can be created using both `cz commit` and the regular `git commit`
* The hooks automatically create a backup of the commit message that can be reused if the commit failed
* The commit message backup can also be used via `cz commit --retry`
