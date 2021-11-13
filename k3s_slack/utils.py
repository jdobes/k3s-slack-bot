import os
import subprocess

import k3s_slack.config as CFG
from k3s_slack.log import get_logger

LOGGER = get_logger(__name__)


def run_command(args, cwd=None, env=None):
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=cwd, env=env, text=True)
    LOGGER.debug("STDOUT: %s", result.stdout)
    LOGGER.debug("STDERR: %s", result.stderr)


def ensure_latest_git_repo(url, repo_name):
    if os.path.isdir(f"/tmp/{repo_name}/"):
        run_command(["git", "pull", "--rebase=false"], cwd=f"/tmp/{repo_name}/")
    else:
        run_command(["git", "clone", url], cwd="/tmp")


def is_k3s_installed():
    return os.path.isfile(CFG.K3S_BINARY_PATH)
