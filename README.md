# Git Archiver

## Installation

The repo can be installed directly as a python package. We recommend installing it either using [pipx](https://github.com/pypa/pipx)(recommended) or using a bare [virtualenv](https://docs.python.org/3/library/venv.html) to avoid polluting your python installation.

### pipx Installation

Pipx is a useful tool that allows you to install command line tools into isolated virtual environments while automatically creating and managing them. It also places scripts onto the user's path so that they do not have to activate the venv by hand each time they want to use the command. Because of this, it is the recommended method for installing small scripts like this.

After installing pipx following the [instructions here](https://github.com/pypa/pipx#install-pipx) you can install the package in an isolated virtual environment with a single command

```bash
pipx install git+https://github.com/uiuc-csid/git-archiver.git
git-archiver <options>
```

### Pip Installation

Find a suitable place on your machine and create a virtual environment using `python -m venv $VENV-LOCATION`.

Then activate the virtual environment and install the package. Note: you will need to activate the virtual environment before each time you use the script in order to put it on your path.

```bash
source $VENV-LOCATION/bin/activate
pip install git+https://github.com/uiuc-csid/git-archiver.git
git-archiver <options>
```

### Required: Personal Access Token

You will need to generate a personal access token for github. For [github-dev the link is here](https://github-dev.cs.illinois.edu/settings/tokens). It should have `repo` level permissions.

## Archiving an organiztion

In order to archive an organization, you must first ensure that you are the owner of the organization. Then, create an empty folder and cd into it. We recommend that you name this folder after the organization that you are archiving. Now you can call `git-archiver` and it will clone every repo from the organization as a bare repo into the current folder. All options can be set either interactively, as cli flags, or as environment variables.

| Argument | Environment variable | Purpose |
|----------|----------------------|---------|
| --github-base-url | GITHUB_BASE_URL      | The api url you are using. Defaults to <https://github-dev.cs.illinois.edu/api/v3> |
| --github-token | GITHUB_TOKEN | Your personal access token |
| --github-org-name | GITHUB_ORG_NAME | The organization you are archiving |

```bash
mkdir test-org
export GITHUB_TOKEN=************
git-archiver --github-org-name test-org
```
