<<<<<<< HEAD
# 🎵 KeygenMusic 98

A simple GUI tool that captures and downloads tracker-style music from [keygenmusic.tk](https://keygenmusic.tk). Inspired by the nostalgic design of classic Windows 98 keygens.

---

## ✨ Features

- Automatically captures links to `.xm`, `.mod`, `.s3m`, and `.it` music files from keygenmusic.tk
- Copy music links to clipboard with one click
- Download music directly via GUI
- Animated logo and scrolling status bar
- Classic Windows 98-style interface
- Packaged into a single portable `.exe` file

---

## 📸 Preview
*(Insert screenshot here if available)*

---

## ⚙️ Requirements

- Python 3.9 to 3.11 (selenium-wire may not support Python 3.12+)
- Google Chrome browser installed
- ChromeDriver (included in project)

---

## 🧩 Installation

```bash
pip install -r requirements.txt
```

---

## 🚀 Run the App

```bash
python v6.py
```

---

## 📦 Build Executable (.exe)

Using PyInstaller:

```bash
pyinstaller --onefile --noconsole ^
--icon=keygen_icon.ico ^
--add-data "bg_classic.png;." ^
--add-data "chromedriver.exe;." ^
--name KeygenMusic98 v6.py
```

> 🔸 Use `;` instead of `:` in `--add-data` paths on Windows.

---

## 📋 Notes

The app opens Chrome in the background and captures tracker music file requests directly from keygenmusic.tk.

---

## 👨‍💻 Author

RuSh_SE7EN

---

## 🪪 License

MIT License – free to use, modify, and distribute.
=======
# KeygenMusic98
A GUI-based tool for grabbing and downloading music from keygenmusic.tk
>>>>>>> 4bfb8dd7e874d8a689c48d4b1478c1ade791ab2c
