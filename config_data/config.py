from dataclasses import dataclass

from environs import Env

@dataclass
class TgBot:
    token: str
    admin_ids: list[int]

@dataclass
class Config:
    tg_bot_configurations: TgBot

def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path=path)
    return Config(
        tg_bot_configurations=TgBot(
            token=env('BOT_TOKEN'),
            admin_ids=list(map(int,env.list('ADMIN_IDS')))
        )
    )