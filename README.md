# 🛡️ DLC JanFaza

### Windows Security Manager & Monitoring Tool

**DLC JanFaza** is a lightweight Windows desktop application developed with Python and Tkinter. It provides a simple and modern graphical interface for monitoring Windows security features and accessing important security settings.

The application helps users check Windows Defender, real-time protection, antispyware protection, and Windows Firewall status from one convenient dashboard.

---

## ✨ Features

- 🛡️ Windows Defender status monitoring
- 🔍 Real-Time Protection status checking
- 🔐 Antivirus protection monitoring
- 👁️ Antispyware protection monitoring
- 🔥 Windows Firewall status checking
- 📊 Security status dashboard
- 🔄 Refresh security information
- ⚙️ Quick access to Windows Security settings
- 🔥 Quick access to Firewall settings
- ℹ️ Built-in About section
- 🖥️ Modern dark-themed graphical interface
- 📦 Standalone Windows EXE support

---

## 🆕 What's New in v1.1

The latest version introduces several improvements:

- Improved graphical interface
- Added Windows Firewall status monitoring
- Added separate security status sections
- Added a refresh security button
- Added an About section
- Improved application layout
- Updated application version information

---

## 🖥️ Requirements

- Windows 10 or Windows 11
- Python 3.10 or newer
- Tkinter
- PowerShell
- PyInstaller (for building EXE files)

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/myheartgotblacked-lgtm/DLC-JanFaza.git
```

### 2. Open the project folder

```bash
cd DLC-JanFaza
```

### 3. Run the application

```bash
py DLC_JanFaza.py
```

---

## 📦 Build EXE

Install PyInstaller:

```bash
py -m pip install pyinstaller
```

Build the executable:

```bash
py -m PyInstaller --onefile --windowed --clean --name DLC-JanFaza DLC_JanFaza.py
```

The executable will be available in:

```text
dist/DLC-JanFaza.exe
```

---

## 📁 Project Structure

```text
DLC-JanFaza/
│
├── DLC_JanFaza.py
├── DLC-JanFaza.spec
├── README.md
├── LICENSE
└── .gitignore
```

---

## 🔒 Security Notice

DLC JanFaza is designed for Windows security monitoring and convenience.

- It reads available Windows Defender status information.
- It checks Windows Firewall profile status.
- It does not intentionally disable antivirus protection.
- It does not bypass Windows security mechanisms.
- It does not modify Windows security policies.
- It provides quick access to official Windows security settings.

**Note:** Some security information may be unavailable depending on Windows configuration, permissions, or installed antivirus software.

---

## 🛠️ Technologies

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Tkinter | Graphical user interface |
| PowerShell | Windows security information |
| PyInstaller | EXE packaging |

---

## 📌 Project Information

| Item | Details |
|---|---|
| Project | DLC JanFaza |
| Version | 1.1 |
| Platform | Windows 10 / Windows 11 |
| Language | Python |
| Interface | Tkinter |
| License | MIT |

---

## 🤝 Contributing

Contributions, suggestions, feature requests, and bug reports are welcome!

You can fork this repository, improve the project, and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

See the `LICENSE` file for more information.

---

## ⭐ Support

If you find DLC JanFaza useful, consider giving this repository a star on GitHub!

---

**DLC JanFaza — Simple, Lightweight, and Convenient Windows Security Monitoring.**

Developed as an independent community project. Not affiliated with Microsoft.
