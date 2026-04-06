"""
file-compressor - Compress files and directories efficiently

Part of Viprasol Utilities: https://viprasol.com
"""

__version__ = "0.1.0"
__author__ = "Viprasol"
__email__ = "hello@viprasol.com"

from .core import FileCompressor, compress, process, main

__all__ = ["FileCompressor", "compress", "process", "main"]
