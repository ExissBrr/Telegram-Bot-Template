from loguru import logger


logger.add(
    sink="logs/info.log",
    format="{time} {level} {message}",
    level="INFO",
    rotation="10 MB",
    compression="zip"
)

logger.add(
    sink="logs/error.log",
    format="{time} {level} {message}",
    level="ERROR",
    rotation="10 MB",
    compression="zip",
)

logger.add(
    sink="logs/debug.log",
    format="{time} {level} {message}",
    level="DEBUG",
    rotation="10 MB",
    compression="zip"
)

logger.add(
    sink="logs/success.log",
    format="{time} {level} {message}",
    level="SUCCESS",
    rotation="10 MB",
    compression="zip"
)
