from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

def get_mini_app_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="✨ Открыть открытку для Анюты",
                web_app=WebAppInfo(url="ТВОЯ_ССЫЛКА_НА_GITHUB_PAGES_ИЛИ_VERCEL")
            )
        ]
    ])
    return keyboard