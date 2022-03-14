import config
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, hunderline, hcode, hlink
from main import get_first_news


bot = Bot(token=config.TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Получить последнюю новость")
    await message.answer("Последняя новость", reply_markup=keyboard)


@dp.message_handler(Text(equals="Получить последнюю новость"))
async def last_news(msg: types.Message):
    last_news = get_first_news()
    await msg.answer(
        f"{hbold(last_news['news_date'])}\n" 
        f"{hlink(last_news['news_title'], last_news['news_url'])}"
        )


if __name__ == "__main__":
    executor.start_polling(dp)   