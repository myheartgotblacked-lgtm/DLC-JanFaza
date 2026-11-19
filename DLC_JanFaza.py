
import tkinter as tk
from tkinter import ttk
import subprocess
import json
import webbrowser

root = tk.Tk()
root.title("DLC جان‌فزا")
root.geometry("500x450")
root.configure(bg="#101820")

title = tk.Label(
    root,
    text="DLC جان‌فزا",
    font=("Arial", 25, "bold"),
    fg="#65d6ad",
    bg="#101820"
)
title.pack(pady=20)

status = tk.Label(
    root,
    text="وضعیت امنیت ویندوز",
    font=("Arial", 15),
    fg="white",
    bg="#101820"
)
status.pack(pady=15)

result = tk.Label(
    root,
    text="برای بررسی کلیک کن",
    font=("Arial", 12),
    fg="#65d6ad",
    bg="#101820"
)
result.pack(pady=15)

def check_security():
    try:
        command = (
            "Get-MpComputerStatus | "
            "Select AntivirusEnabled,RealTimeProtectionEnabled | "
            "ConvertTo-Json -Compress"
        )
        output = subprocess.check_output(
            ["powershell", "-NoProfile", "-Command", command],
            text=True,
            timeout=10
        )
        data = json.loads(output)

        result.config(
            text="آنتی‌ویروس: " +
            ("فعال" if data["AntivirusEnabled"] else "غیرفعال") +
            "\nمحافظت بلادرنگ: " +
            ("فعال" if data["RealTimeProtectionEnabled"] else "غیرفعال")
        )
    except Exception:
        result.config(text="وضعیت قابل بررسی نیست")

def open_security():
    webbrowser.open("windowsdefender:")

tk.Button(
    root,
    text="بررسی امنیت",
    command=check_security,
    font=("Arial", 12),
    width=25
).pack(pady=10)

tk.Button(
    root,
    text="تنظیمات Windows Security",
    command=open_security,
    font=("Arial", 12),
    width=25
).pack(pady=10)

root.mainloop()
