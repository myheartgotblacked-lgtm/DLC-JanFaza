
import tkinter as tk
from tkinter import ttk
import subprocess
import json
import webbrowser

APP_NAME = "DLC جان‌فزا"
VERSION = "1.1"

BG = "#101820"
CARD = "#1b2935"
GREEN = "#65d6ad"
WHITE = "#ffffff"
MUTED = "#a9bdc2"

root = tk.Tk()
root.title(f"{APP_NAME} | v{VERSION}")
root.geometry("620x650")
root.minsize(560, 600)
root.configure(bg=BG)

style = ttk.Style()
style.theme_use("clam")
style.configure(
    "TButton",
    font=("Arial", 11, "bold"),
    padding=10
)

def get_powershell(command):
    return subprocess.check_output(
        ["powershell", "-NoProfile", "-Command", command],
        text=True,
        timeout=10,
        stderr=subprocess.DEVNULL
    ).strip()

def check_security():
    status_label.config(text="در حال بررسی امنیت...")
    root.update_idletasks()

    try:
        command = """
        Get-MpComputerStatus |
        Select AntivirusEnabled,
        RealTimeProtectionEnabled,
        AntispywareEnabled |
        ConvertTo-Json -Compress
        """

        data = json.loads(get_powershell(command))

        antivirus_value.config(
            text="فعال" if data["AntivirusEnabled"] else "غیرفعال"
        )

        realtime_value.config(
            text="فعال" if data["RealTimeProtectionEnabled"] else "غیرفعال"
        )

        antispyware_value.config(
            text="فعال" if data["AntispywareEnabled"] else "غیرفعال"
        )

        status_label.config(
            text="بررسی امنیت با موفقیت انجام شد."
        )

    except Exception:
        status_label.config(
            text="امکان دریافت اطلاعات Windows Defender وجود ندارد."
        )

        antivirus_value.config(text="نامشخص")
        realtime_value.config(text="نامشخص")
        antispyware_value.config(text="نامشخص")

def check_firewall():
    try:
        command = """
        Get-NetFirewallProfile |
        Select Name, Enabled |
        ConvertTo-Json -Compress
        """

        data = json.loads(get_powershell(command))

        if isinstance(data, dict):
            data = [data]

        firewall_info = "\n".join(
            f"{item['Name']}: {'فعال' if item['Enabled'] else 'غیرفعال'}"
            for item in data
        )

        status_label.config(text="وضعیت فایروال:\n" + firewall_info)

    except Exception:
        status_label.config(text="وضعیت فایروال قابل دریافت نیست.")

def open_security():
    webbrowser.open("windowsdefender:")

def open_firewall():
    subprocess.Popen(["control.exe", "firewall.cpl"])

def about():
    status_label.config(
        text=f"DLC JanFaza\nVersion: {VERSION}\n"
             "Windows Security Manager\n"
             "Built with Python and Tkinter"
    )

# Header
header = tk.Frame(root, bg=BG)
header.pack(fill="x", pady=20)

tk.Label(
    header,
    text="🛡 DLC جان‌فزا",
    font=("Arial", 26, "bold"),
    fg=GREEN,
    bg=BG
).pack()

tk.Label(
    header,
    text=f"SECURITY MANAGER  |  VERSION {VERSION}",
    font=("Arial", 10, "bold"),
    fg=MUTED,
    bg=BG
).pack(pady=5)

# Security card
card = tk.Frame(root, bg=CARD, padx=20, pady=20)
card.pack(fill="x", padx=25, pady=10)

tk.Label(
    card,
    text="وضعیت امنیت ویندوز",
    font=("Arial", 16, "bold"),
    fg=WHITE,
    bg=CARD
).pack(anchor="e", pady=(0, 15))

def create_status_row(parent, name):
    row = tk.Frame(parent, bg=CARD)
    row.pack(fill="x", pady=8)

    tk.Label(
        row,
        text=name,
        font=("Arial", 12),
        fg=WHITE,
        bg=CARD
    ).pack(side="right")

    value = tk.Label(
        row,
        text="بررسی نشده",
        font=("Arial", 12, "bold"),
        fg=GREEN,
        bg=CARD
    )
    value.pack(side="left")

    return value

antivirus_value = create_status_row(card, "آنتی‌ویروس")
realtime_value = create_status_row(card, "محافظت بلادرنگ")
antispyware_value = create_status_row(card, "ضدجاسوس‌افزار")

# Buttons
buttons = tk.Frame(root, bg=BG)
buttons.pack(fill="x", padx=35, pady=15)

def create_button(text, command):
    ttk.Button(
        buttons,
        text=text,
        command=command
    ).pack(fill="x", pady=5)

create_button("🔄 بررسی مجدد امنیت", check_security)
create_button("🔥 بررسی فایروال", check_firewall)
create_button("🛡 باز کردن Windows Security", open_security)
create_button("⚙ تنظیمات Firewall", open_firewall)
create_button("ℹ درباره برنامه", about)

# Footer
status_label = tk.Label(
    root,
    text="برای شروع، بررسی امنیت را انتخاب کنید.",
    font=("Arial", 10),
    fg=GREEN,
    bg=BG,
    wraplength=550,
    justify="center"
)
status_label.pack(pady=15)

tk.Label(
    root,
    text="DLC JanFaza © 2026",
    font=("Arial", 9),
    fg=MUTED,
    bg=BG
).pack(side="bottom", pady=12)

root.mainloop()
