"""
Файл, содержащий функции для конвертации данных из 
float в bytes и bytes в строку, а также функцию для сохранения результата в файл от второй функции.
"""

import struct
import logging
from pathlib import Path
from datetime import datetime
from logger_setup import setup_console_logger

logger: logging.Logger = setup_console_logger("converter_logger")

def float_to_bytes(value: float) -> bytes:
    """
    Преобразование переменной типа float (8 байт) в последовательность сырых байтов 

    Args:
        value (float): Число с плавающей запятой, которое нужно преобразовать

    Returns:
        bytes: Последовательность байтов, представляющая число с плавающей запятой

    Raises:
        TypeError: Если value не является типом float.
    """
    if not isinstance(value, float):
        raise TypeError("Значение value должно быть типа float")

    logger.info(f"float_to_bytes вызвана с аргументом: {value}")
    result: bytes = struct.pack('d', value)
    logger.info(f"float_to_bytes вернула: {result}")
    return result


def bytes_to_string(value: bytes) -> str:
    """
    Преобразует последовательность байтов в шестнадцатеричную строку.

    Args:
        value (bytes): Последовательность байтов, которую нужно преобразовать

    Returns:
        str: Строка, полученная из последовательности байтов

    Raises:
        TypeError: Если value не является типом bytes.
    """
    if not isinstance(value, bytes):
        raise TypeError("Значение value должно быть типа bytes")

    logger.info(f"bytes_to_string вызвана с аргументом: {value}")
    result: str = value.hex() 
    logger.info(f"bytes_to_string вернула: {result}")
    return result


def save_float_conversion(value: float) -> None:
    """
    Преобразует число float в hex-строку и сохраняет результат в файл.

    Args:
        value (float): Число с плавающей запятой для преобразования


    Raises:
        TypeError: Если value не является типом float.
        IOError: Если возникает ошибка при записи в файл.
    """
    try:        
        bytes_data: bytes = float_to_bytes(value)  
        hex_string: str = bytes_to_string(bytes_data) 
        output_dir: Path = Path("logs")
        output_dir.mkdir(exist_ok=True)

        filename: str = str(output_dir / f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")

        with open(filename, "w", encoding="utf-8") as f:
            f.write(hex_string)
        
        logger.info(f"Результат сохранён в {filename}")
    except TypeError as e:
        logger.error(f"Ошибка типа: {e}")
    except IOError as e:
        logger.error(f"Ошибка записи в файл {filename}: {e}")
    except Exception as e:
        logger.error(f"Неожиданная ошибка: {e}")


