## Запуск для разработки
1. Развернуть вирутальное окружение: `python -m venv venv`
2. Активировать **venv**:
    - Windows: `.\venv\Scripts\activate`
    - Unix/MacOS: `source venv/bin/activate`
3. Установить зависимости: `pip install -r requirements.txt`
4. Создать файл `.env` и вставить строку `BOT_TOKEN=your_token` со значением токена своего своего бота для разработки
5. Запустить главный скрипт: `python main.py`
6. Если всё прошло успешно, то бот запущен