from loguru import logger


logger.add(
    "info.log",
    format="{time} {level} {message}",
    level="INFO",
    rotation="10 MB",
    compression="zip"
)

logger.add(
    "error.log",
    format="{time} {level} {message}",
    level="ERROR",
    rotation="10 MB",
    compression="zip",
)

logger.add(
    "debug.log",
    format="{time} {level} {message}",
    level="DEBUG",
    rotation="10 MB",
    compression="zip"
)

logger.add(
    "success.log",
    format="{time} {level} {message}",
    level="SUCCESS",
    rotation="10 MB",
    compression="zip"
)
