from aiogram import types
from aiogram.utils import exceptions
from loguru import logger

from loader import DP


@DP.errors_handler()
async def errors_logging(update: types.Update, exception):
    """
    Обработчик ошибок, вызванных самим ботом
    :param update: Апдейт, где произошла ошибка
    :param exception: Ошибка
    :return:
    """

    if isinstance(exception, exceptions.NetworkError):
        logger.error("Network error")
        return True
    if isinstance(exception, exceptions.BadRequest):
        logger.error("Bad request")
        return True

    if isinstance(exception, exceptions.BadWebhook):
        logger.error("Bad webhook")
        return True

    if isinstance(exception, exceptions.BadWebhookAddrInfo):
        logger.error("Bad webhook addr info")
        return True

    if isinstance(exception, exceptions.BadWebhookNoAddressAssociatedWithHostname):
        logger.error("Bad webhook no address associated with hostname")
        return True

    if isinstance(exception, exceptions.BadWebhookPort):
        logger.error("Bad webhook port")
        return True

    if isinstance(exception, exceptions.BotBlocked):
        logger.error("Bot blocked")
        return True

    if isinstance(exception, exceptions.BotDomainInvalid):
        logger.error("Bot domain invalid")
        return True

    if isinstance(exception, exceptions.BotKicked):
        logger.error("Bot kicked")
        return True

    if isinstance(exception, exceptions.ButtonDataInvalid):
        logger.error("Button data invalid")
        return True

    if isinstance(exception, exceptions.ButtonURLInvalid):
        logger.error("Button URL invalid")
        return True

    if isinstance(exception, exceptions.CantDemoteChatCreator):
        logger.error("Cant demote chat creator")
        return True

    if isinstance(exception, exceptions.CantGetUpdates):
        logger.error("Cant get updates")
        return True

    if isinstance(exception, exceptions.CantInitiateConversation):
        logger.error("Cant initiate conversation")
        return True

    if isinstance(exception, exceptions.CantParseEntities):
        logger.error("Cant parse entities")
        return True

    if isinstance(exception, exceptions.CantParseUrl):
        logger.error("Cant parse url")
        return True

    if isinstance(exception, exceptions.CantRestrictChatOwner):
        logger.error("Cant restrict chat owner")
        return True

    if isinstance(exception, exceptions.CantRestrictSelf):
        logger.error("Cant restrict self")
        return True

    if isinstance(exception, exceptions.CantTalkWithBots):
        logger.error("Cant talk with bots")
        return True

    if isinstance(exception, exceptions.ChatAdminRequired):
        logger.error("Chat admin required")
        return True

    if isinstance(exception, exceptions.ChatDescriptionIsNotModified):
        logger.error("Chat description is not modified")
        return True

    if isinstance(exception, exceptions.ChatIdIsEmpty):
        logger.error("Chat id is empty")
        return True

    if isinstance(exception, exceptions.ChatNotFound):
        logger.error("Chat not found")
        return True

    if isinstance(exception, exceptions.MessageCantBeDeleted):
        logger.error("Message cant be deleted")
        return True

    if isinstance(exception, exceptions.MessageCantBeEdited):
        logger.error("Message cant be edited")
        return True

    if isinstance(exception, exceptions.MessageCantBeForwarded):
        logger.error("Message cant be forwarded")
        return True

    if isinstance(exception, exceptions.MessageError):
        logger.error("Message error")
        return True

    if isinstance(exception, exceptions.MessageIdentifierNotSpecified):
        logger.error("Message identifier not specified")
        return True

    if isinstance(exception, exceptions.MessageIdInvalid):
        logger.error("Message id invalid")
        return True

    if isinstance(exception, exceptions.MessageIsNotAPoll):
        logger.error("Message is not a poll")
        return True

    if isinstance(exception, exceptions.MessageNotModified):
        logger.error("Message not modified")
        return True

    if isinstance(exception, exceptions.MessageTextIsEmpty):
        logger.error("Message text is empty")
        return True

    if isinstance(exception, exceptions.MessageToDeleteNotFound):
        logger.error("Message to delete not found")
        return True

    if isinstance(exception, exceptions.MessageToEditNotFound):
        logger.error("Message to edit not found")
        return True

    if isinstance(exception, exceptions.MessageToForwardNotFound):
        logger.error("Message to forward not found")
        return True

    if isinstance(exception, exceptions.MessageToPinNotFound):
        logger.error("Message to pin not found")
        return True

    if isinstance(exception, exceptions.MessageToReplyNotFound):
        logger.error("Message to reply not found")
        return True

    if isinstance(exception, exceptions.MessageWithPollNotFound):
        logger.error("Message with poll not found")
        return True


