"""It is possible too to store the main menu settings in config_data package"""
from aiogram import Bot
from aiogram.types import BotCommand
from lexicon.lexicon_ru import LEXICON_MAIN_MENU_RU


async def set_main_menu(bot: Bot) -> None:
    """set main menu commands for the bot"""
    main_menu_commands = [
        BotCommand(
            command=command,
            description=description
        )
        for command, description in LEXICON_MAIN_MENU_RU.items()
    ]
    await bot.set_my_commands(main_menu_commands)

async def delete_main_menu(bot: Bot) -> None:
    """delete main menu commands for the bot"""
    await bot.delete_my_commands()
