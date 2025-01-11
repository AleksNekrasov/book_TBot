import asyncio
import logging
from logging import getLogger

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

#-------------мои файлы---------------------------
from config_data.config import Config, load_config
from handlers import user_handlers, other_handlers
from keyboards.main_menu import set_main_menu

#логгер
logger = getLogger(__name__)

# Функция конфигурирования и запуска бота
async def main():
    logging.basicConfig(
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s',
        level=logging.INFO
    )

    logger.info('Starting bot')

    config: Config = load_config()

    bot = Bot(
        token=config.tg_bot_configurations.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )

    dp = Dispatcher()

    # Настраиваем главное меню бота
    await set_main_menu(bot)

    #роутеры
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    # Пропускаем накопившиеся апдейты
    await bot.delete_webhook(drop_pending_updates=True)
    # Запускаем поллинг
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

