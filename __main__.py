import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config_data.config import Config, load_config

# Импортируем роутеры
# ...
# Импортируем миддлвари
# ...
# Импортируем вспомогательные функции для создания нужных объектов
# ...

logger = logging.getLogger(__name__) # инициализация логгера

# Функция конфигурирования и запуска бота
async def main() -> None:
    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.DEBUG,
        style='{',
        format='[{asctime}] {name} {levelname:<8s} {filename} {lineno} {message}',
    )
    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')

    # Загружаем конфиг в переменную config
    config: Config = load_config()
    # Инициализируем объект хранилища
    #storage = ...

    # Инициализируем бот и диспетчер
    bot = Bot(
        token=config.tg_bot.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
        )
    dp = Dispatcher()

    # Инициализируем другие объекты (пул соединений с БД, кеш и т.п.)
    # ...

    # Помещаем нужные объекты в workflow_data диспетчера
    #dp.workflow_data.update(...)

    # Настраиваем главное меню бота
    #await set_main_menu(bot)

    # Регистрируем роутеры
    logger.debug('Подключаем роутеры')
    # ...

    # Регистрируем миддлвари
    logger.debug('Подключаем миддлвари')
    # ...

    # Пропускаем (если нужно) накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())
