# 📈 TRACKER BOT CURRENCY

[![Python](https://img.shields.io/badge/python-3.14-blue?logo=python)](https://www.python.org/)
[![Aiogram](https://img.shields.io/badge/aiogram-3.x-blue?logo=telegram)](https://docs.aiogram.dev/)

Telegram-бот для мгновенного получения актуальных цен на акции, криптовалюты и валютные пары. Просто отправьте название или тикер — и бот покажет текущую стоимость.

## ✨ Возможности

*   🔍 **Поиск по тикеру или названию** — понимает как `AAPL`, так и `Apple`
*   💰 **Поддержка множества активов:**
    *   Акции (Apple, Google, Сбер и др.)
    *   Криптовалюты (BTC, ETH, SOL и др.)
    *   Валютные пары (EUR/USD, USD/RUB)
*   ⚡ **Мгновенный ответ** — данные подгружаются через Yahoo Finance и Binance API
*   📊 **Красивое форматирование** — цена выделена, виден тип актива
*   🔒 **Безопасность** — токен бота хранится локально и не попадает в репозиторий

## 🛠️ Используемые технологии

*   **Python 3.14** — основной язык
*   **Aiogram 3.x** — асинхронная работа с Telegram Bot API
*   **yFinance** — получение данных об акциях и валютах
*   **python-binance** — получение данных о криптовалютах
*   **python-dotenv** — безопасное хранение токена

## 🚀 Установка и запуск

### Предварительные требования
*   Установленный Python 3.14 или выше
*   Установленный Git
*   Токен вашего Telegram-бота (получить у [@BotFather](https://t.me/BotFather))

### Пошаговая инструкция

1.  **Клонируйте репозиторий:**
    ```bash
    git clone https://github.com/flenk41/TRACKER_BOT_CURRENCY-.git
    cd TRACKER_BOT_CURRENCY-
