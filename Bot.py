from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
import asyncio
import yfinance as yf
from binance.client import Client
import requests
from dotenv import load_dotenv
import os

tok = None
load_dotenv()
# Токен (НИКОГДА не публикуй его в открытом доступе! Я заменил)
with open("Token.txt", 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        if line.strip():  # берем первую непустую строку
            tok = line.strip()
            break

bot = Bot(token = tok)
dp = Dispatcher()
binance_client = Client()

def get_yahoo_price(ticker):
    """Цена через Yahoo Finance"""
    try:
        stock = yf.Ticker(ticker)
        data = stock.info
        price = data.get('regularMarketPrice', data.get('currentPrice'))
        if price:
            return {
                'price': price,
                'currency': data.get('currency', 'USD'),
                'name': data.get('longName', ticker)
            }
    except:
        return None

def get_binance_price(symbol):
    """Цена через Binance"""
    try:
        ticker = binance_client.get_symbol_ticker(symbol=symbol.upper() + 'USDT')
        return {
            'price': float(ticker['price']),
            'currency': 'USDT',
            'name': f'{symbol.upper()}/USDT'
        }
    except:
        return None

@dp.message(Command('start', 'help'))
async def send_welcome(message: Message):
    await message.reply(
        "📊 Отправь мне название акции или крипты\n\n"
        "Примеры:\n"
        "• AAPL - Apple\n"
        "• BTC - Биткоин\n"
        "• SBER.ME - Сбер\n"
        "• EURUSD=X - Евро/Доллар"
    )

# Обработчик всех текстовых сообщений (не команд)
@dp.message()
async def handle_price(message: Message):
    query = message.text.strip().upper()
    
    # Пробуем Binance для крипты
    if len(query) <= 5: 
        crypto = get_binance_price(query)
        if crypto:
            await message.reply(
                f"*{crypto['name']}*\n"
                f"💰 Цена: `{crypto['price']:.2f}` {crypto['currency']}",
                parse_mode='Markdown'
            )
            return
    
    # Пробуем Yahoo для всего остального
    yahoo = get_yahoo_price(query)
    if yahoo:
        await message.reply(
            f"*{yahoo['name']}*\n"
            f"💰 Цена: `{yahoo['price']:.2f}` {yahoo['currency']}",
            parse_mode='Markdown'
        )
    else:
        await message.reply("❌ Ничего не найдено. Попробуй другой запрос.")

async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())