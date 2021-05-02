from data.config import DEFAULT_RATE_LIMIT


def rate_limit(limit: float = DEFAULT_RATE_LIMIT, key: str = "None"):
    """
    Декоратор для конфигурации ограничителя лимита и ключа функции
    :param limit: Лимит времени, который должен пройти,
     прежде чем можно будет повторно обработать функцию с указанным ключом
    :param key: Ключ функции
    :return:
    """
    def decorator(func):
        setattr(func, "throttling_rate_limit", limit)
        setattr(func, "throttling_key", key)
        return func
    return decorator
