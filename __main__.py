"""entry point package for the bot"""
import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config_data.config import Config, load_config
from keyboards.bot_main_menu import set_main_menu

# routers import
# ...
# middlewares import
# ...
# other imports
# ...

logger = logging.getLogger(__name__) # logger initialization


async def main() -> None:
    """main function: configuration and starting the bot"""
    # logging configuration
    logging.basicConfig(
        level=logging.DEBUG,
        style='{',
        format='[{asctime}] {name} {levelname:<8s} {filename} {lineno} {message}',
    )
    # starting bot log
    logger.info('Starting bot')

    # config loading
    config: Config = load_config()
    # storage objects initialization
    #storage = ...

    # bot and dispatcher initialization
    bot = Bot(
        token=config.tg_bot.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
        )
    dp = Dispatcher()

    # Инициализируем другие объекты (пул соединений с БД, кеш и т.п.)
    # ...

    # Помещаем нужные объекты в workflow_data диспетчера
    #dp.workflow_data.update(...)

    # main menu activation
    await set_main_menu(bot)

    # routers registration
    logger.debug('registering routers')
    # ...

    # middlewares registration
    logger.debug('registering middlewares')
    # ...

    # Пропускаем (если нужно) накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())
