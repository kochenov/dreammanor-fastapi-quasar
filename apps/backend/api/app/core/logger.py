import logging
from datetime import datetime, timezone

from pythonjsonlogger import jsonlogger

from .config import settings

logger = logging.getLogger()

logHandler = logging.StreamHandler()


class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
        if not log_record.get("timestamp"):
            now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
            log_record["timestamp"] = now
        if log_record.get("level"):
            log_record["level"] = log_record["level"].upper()
        else:
            log_record["level"] = record.levelname


formatter = CustomJsonFormatter(
    "%(timestamp)s %(level)s %(message)s %(module)s %(funcName)s"
)

# Добавление кодировки UTF-8
formatter.encoding = "utf-8"

logHandler.setFormatter(formatter)
logger.addHandler(logHandler)
# logger.setLevel(settings.LOG_LEVEL)
