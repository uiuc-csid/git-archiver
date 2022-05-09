__version__ = '0.1.0'

from typing import cast
import click
from github import Github, Repository
from git import Repo


@click.command()
@click.option('--github-base-url', default="https://github-dev.cs.illinois.edu/api/v3", envvar='GITHUB_BASE_URL', help="The base url of the github site")
@click.option('--github-token', required=True, prompt=True, envvar='GITHUB_TOKEN', help="Access token with permissions for each repo. Falls back to the GITHUB_TOKEN environment variable")
@click.option('--github-org-name', required=True, prompt=True, envvar='GITHUB_ORG_NAME', help="The organization name. Falls back to GITHUB_ORG_NAME environment variable.")
def cli(github_base_url, github_token, github_org_name):
    gh = Github(base_url=github_base_url, login_or_token=github_token)
    organization = gh.get_organization(github_org_name)

    repos = organization.get_repos()
    with click.progressbar(repos, length=repos.totalCount) as bar:
        for repo in bar:
            Repo.clone_from(repo.ssh_url, to_path=f"{repo.name}.git", multi_options=['--bare'])


if __name__ == '__main__':
    cli()  #pylint: disable=no-value-for-parameter
