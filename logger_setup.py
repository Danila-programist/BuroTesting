"""
Файл, содержащий настройку логгера для вывода в консоль.
"""

import logging

def setup_console_logger(name: str = "console") -> logging.Logger:
    """Настройка логгера для вывода в консоль"""
    logger: logging.Logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    if not logger.handlers:
        ch: logging.StreamHandler = logging.StreamHandler()
        ch.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        logger.addHandler(ch)
    
    return logger

