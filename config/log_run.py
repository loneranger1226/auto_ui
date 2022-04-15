import logging.config


def get_log(path):
    logging.config.fileConfig(path)
    return logging.getLogger()