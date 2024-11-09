"""config data for the bot"""
from dataclasses import dataclass
from environs import Env


@dataclass
class BotDataBase:
    """database config"""
    db_host: str
    db_port: int
    db_name: str
    db_user: str
    db_password: str

@dataclass
class TGBot:
    """telegram bot config"""
    token: str
    admin_ids: list[int]

@dataclass
class Config:
    """main config"""
    bot_db: BotDataBase
    tg_bot: TGBot

def load_config(path: str | None = None) -> Config:
    """load config from .env file"""
    env = Env()
    env.read_env(path)
    return Config(
        bot_db=BotDataBase(
            db_host=env("DB_HOST"),
            db_port=env.int("DB_PORT"),
            db_name=env("DB_NAME"),
            db_user=env("DB_USER"),
            db_password=env("DB_PASSWORD")
        ),
        tg_bot=TGBot(
            token=env("BOT_TOKEN"),
            admin_ids=env.list("ADMIN_IDS")
        )
    )

# test and debug case:
if __name__ == '__main__':
    env: Env = Env()
    env.read_env('../.env') # .env in main directory
    config = Config(
        bot_db=BotDataBase(
            db_host=env('DB_HOST'),
            db_port=env.int('DB_PORT'),
            db_name=env('DB_NAME'),
            db_user=env('DB_USER'),
            db_password=env('DB_PASSWORD')
        ),
        tg_bot=TGBot(
            token=env('BOT_TOKEN'),
            admin_ids=list(map(int, env.list('ADMIN_IDS'))) #env.list('ADMIN_IDS')
        )
    )
    print('BOT_TOKEN:', config.tg_bot.token)
    print('ADMIN_IDS:', config.tg_bot.admin_ids)
    print()
    print('DB_HOST:', config.bot_db.db_host)
    print('DB_PORT:', config.bot_db.db_port)
    print('DB_NAME:', config.bot_db.db_name)
    print('DB_USER:', config.bot_db.db_user)
    print('DB_PASSWORD:', config.bot_db.db_password)
