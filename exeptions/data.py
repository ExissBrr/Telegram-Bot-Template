class BadData(Exception):
    """Тип ошибки плохих данных"""
    pass

class FailedGetUserId(BadData):
    """Не удалось получить id"""

    def __init__(self, data):
        self.match = f"Failed git user id from data: {data}"