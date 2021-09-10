import logging


_logger = None
def create_logger(name, log_file=None):
    r"""Method to create logger"""
    global _logger
    # Create a custom logger
    _logger = logging.getLogger(name)
    _logger.setLevel(logging.INFO)

    # Create handlers
    c_handler = logging.StreamHandler()
    # c_handler.setLevel(logging.DEBUG)
    format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    c_handler.setFormatter(format)
    _logger.addHandler(c_handler)

    if log_file is not None:
        f_handler = logging.FileHandler(log_file)
        # f_handler.setLevel(logging.DEBUG)
        f_handler.setFormatter(format)
        _logger.addHandler(f_handler)

    _logger.info("Logger created")
    
    
def get_logger():
    global _logger
    return _logger