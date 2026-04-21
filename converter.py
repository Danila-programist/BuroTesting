"""
Файл, содержащий функции для конвертации данных из 
float в bytes и bytes в строку. 
"""

import struct

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

    result: bytes = struct.pack('d', value)
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

    result: str = value.hex() 
    return result

