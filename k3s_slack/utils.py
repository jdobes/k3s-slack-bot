import os
import logging
import subprocess

import k3s_slack.config as CFG


def init_logging():
    logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s", level=logging.INFO)


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, CFG.LOGGING_LEVEL, logging.INFO))
    return logger


def run_command(args, cwd=None, env=None):
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=cwd, env=env, text=True)
    return result.stdout, result.stderr


def ensure_latest_git_repo(url, repo_name):
    if os.path.isdir(f"/tmp/{repo_name}/"):
        run_command(["git", "pull"], cwd=f"/tmp/{repo_name}/")
    else:
        run_command(["git", "clone", url], cwd="/tmp")
