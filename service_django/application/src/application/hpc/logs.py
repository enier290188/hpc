import logging


def config_logger():
    logger = logging.getLogger()
    # hdlr = logging.StreamHandler()
    hdlr = logging.FileHandler('/service_django/error.log')
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.DEBUG)


def get_logs(e):
    logging.info("#### Aqui se produjo un error. ####", e)