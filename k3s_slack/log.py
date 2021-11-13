import logging

import k3s_slack.config as CFG


def init_logging():
    logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s", level=logging.INFO)


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, CFG.LOGGING_LEVEL, logging.INFO))
    return logger
