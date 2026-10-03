
TOKEN = "8939663107:AAHfpQd7P_T3V8Czx7HhQzAlK3MwCRimuRc" # Наприклад:

# //--------------------------------
import tkinter as tk
from tkinter import messagebox
import urllib.request
import json
import ssl
import os


# --- НАЛАШТУВАННЯ ---
# TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

CHAT_ID = "5770479157"
TOKEN = "8939663107:AAHfpQd7P_T3V8Czx7HhQzAlK3MwCRimuRc"
CABINET_NAME = "Кабінет інформатики №3"
# --------------------


def send_sos():
    """Функція, яка виконується при натисканні на кнопку SOS."""

    if not TOKEN:
        messagebox.showerror(
            "Помилка",
            "Не задано Telegram Bot Token."
        )
        return

    message = (
        f"🚨 УВАГА! ТРИВОГА! 🚨\n"
        f"Сигнал надійшов із приміщення: {CABINET_NAME}"
    )

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": message
    }

    try:
        # Контекст SSL
        context = ssl._create_unverified_context()

        # Перетворення даних у JSON
        data_encoded = json.dumps(
            data,
            ensure_ascii=False
        ).encode("utf-8")

        req = urllib.request.Request(
            url,
            data=data_encoded,
            headers={
                "Content-Type": "application/json; charset=utf-8"
            }
        )

        # Відправлення запиту
        with urllib.request.urlopen(
            req,
            context=context
        ) as response:

            if response.status == 200:
                messagebox.showinfo(
                    "Успіх",
                    "Сигнал тривоги успішно надіслано!"
                )
            else:
                messagebox.showerror(
                    "Помилка",
                    f"Не вдалося надіслати сигнал.\n"
                    f"Код відповіді: {response.status}"
                )

    except Exception as e:
        messagebox.showerror(
            "Помилка мережі",
            f"Сталася помилка:\n{e}"
        )


# --- Графічний інтерфейс ---

root = tk.Tk()

root.title("Система екстреного виклику")
root.geometry("400x300")
root.config(bg="#f0f0f0")


label = tk.Label(
    root,
    text="Панель екстреного зв'язку",
    font=("Arial", 14, "bold"),
    bg="#f0f0f0"
)

label.pack(pady=20)


sos_button = tk.Button(
    root,
    text="SOS",
    font=("Arial", 32, "bold"),
    bg="red",
    fg="white",
    activebackground="darkred",
    activeforeground="white",
    width=6,
    height=2,
    command=send_sos
)

sos_button.pack(pady=20)


sub_label = tk.Label(
    root,
    text=f"Об'єкт: {CABINET_NAME}",
    font=("Arial", 10),
    bg="#f0f0f0",
    fg="gray"
)

sub_label.pack(
    side="bottom",
    pady=10
)


root.mainloop()