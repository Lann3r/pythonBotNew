from typing import Callable, Awaitable, Dict, Any
from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery


class CheckSubscription(BaseMiddleware):

    async def __call__(
            self,
            handler: Callable[[CallbackQuery, Dict[str, Any]], Awaitable[Any]],
            event: CallbackQuery,
            data: Dict[str, Any]
    ) -> Any:
        chat_member = await event.bot.get_chat_member('@kotogramfun', event.from_user.id)

        if chat_member.status == 'left':
            await event.answer('Подпишись на канал!')
        else:
            return await handler(event, data)
