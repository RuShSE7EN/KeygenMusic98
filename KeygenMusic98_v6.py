import tkinter as tk
from tkinter import filedialog
from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import threading
import requests
import os
import time
import pyperclip
from PIL import Image, ImageTk

def resource_path(relative_path):
    import sys, os
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


CHROMEDRIVER_PATH = resource_path("chromedriver.exe")
SITE_URL = "https://keygenmusic.tk"
ALLOWED_EXTENSIONS = (".xm", ".mod", ".s3m", ".it")


class HorizontalMarquee(tk.Canvas):
    def __init__(self, parent, text, fg="#00FF00", bg="black", font=("Fixedsys", 9, "bold"), speed=50, pause_time=3000, **kwargs):
        super().__init__(parent, bg=bg, highlightthickness=0, **kwargs)
        self.fg = fg
        self.bg = bg
        self.font = font
        self.speed = speed
        self.pause_time = pause_time

        self.width = kwargs.get("width", 350)
        self.height = kwargs.get("height", 50)
        self.configure(width=self.width, height=self.height)

        self.text = text
        self.text_id = None

        self._paused = True
        self._after_id = None

        self.create_rectangle(0, 0, self.width, self.height, fill=self.bg, outline=self.bg)
        self.create_text_item(self.text)
        self.after(self.pause_time, self._start_marquee)

    def create_text_item(self, text):
        if self.text_id:
            self.delete(self.text_id)
        self.text_id = self.create_text(self.width // 2, self.height // 2, text=text, font=self.font, fill=self.fg, anchor="center")
        self.text_bbox = self.bbox(self.text_id)
        self.text_width = self.text_bbox[2] - self.text_bbox[0]

    def update_text(self, new_text):
        self.text = new_text
        self._paused = True
        if self._after_id:
            self.after_cancel(self._after_id)
        self.create_text_item(self.text)
        self.after(self.pause_time, self._start_marquee)

    def _start_marquee(self):
        self._paused = False
        self._scroll_text()

    def _scroll_text(self):
        if self._paused:
            return

        x1, y1, x2, y2 = self.bbox(self.text_id)
        if x2 < 0:
            self.moveto(self.text_id, self.width, (self.height - (y2 - y1)) // 2)
        else:
            self.move(self.text_id, -2, 0)
        self._after_id = self.after(self.speed, self._scroll_text)


class KeygenMusic98:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("KeygenMusic 98")
        self.root.geometry("360x360")
        self.root.resizable(False, False)
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        self.bg_image = Image.open(resource_path("bg_classic.png")).resize((360, 360))
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.canvas = tk.Canvas(self.root, width=360, height=360, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, anchor="nw", image=self.bg_photo)

        self.logo_text = self.canvas.create_text(180, 110, text="KeygenMusic 98", font=("Fixedsys", 20, "bold"), fill="#FFA500")
        self.canvas.create_text(180, 345, text="© RuSh_SE7EN", font=("MS Sans Serif", 12, "bold"), fill="#87CEEB")

        self.current_link = None
        self.found_links = set()
        self.message_timeout = None

        self.status_bar = HorizontalMarquee(self.root, text="Listening for music tracks...", fg="#00FF00", bg="black",
                                            font=("Fixedsys", 9, "bold"), height=40, width=350, speed=50, pause_time=3000)
        self.status_bar.place(x=5, y=5)

        self.copy_btn = tk.Button(self.root, text="Copy Link", command=self.copy_link,
                                  width=15, height=1, relief="raised", bg="#3CB371", fg="black",
                                  font=("MS Sans Serif", 10, "bold"), bd=2)
        self.copy_btn.place(x=50, y=200)

        self.download_btn = tk.Button(self.root, text="Download", command=self.download_track,
                                      width=15, height=1, relief="raised", bg="#E57373", fg="black",
                                      font=("MS Sans Serif", 10, "bold"), bd=2)
        self.download_btn.place(x=180, y=200)

        self.logo_anim_offset = 0
        self.logo_anim_direction = 1
        self.logo_anim_colors = ["#FFA500", "#FFFFFF"]
        self.logo_color_index = 0
        self.animate_logo()

    def animate_logo(self):
        self.logo_anim_offset += self.logo_anim_direction * 2
        if abs(self.logo_anim_offset) > 4:
            self.logo_anim_direction *= -1
        self.canvas.coords(self.logo_text, 180 + self.logo_anim_offset, 110)
        self.logo_color_index = (self.logo_color_index + 1) % len(self.logo_anim_colors)
        self.canvas.itemconfig(self.logo_text, fill=self.logo_anim_colors[self.logo_color_index])
        self.root.after(70, self.animate_logo)

    def update_link(self, url):
        self.current_link = url
        self.status_bar.update_text(url)

    def set_temp_message(self, message, delay=3000):
        self.status_bar.update_text(message)
        self.root.after(delay, lambda: self.status_bar.update_text(self.current_link or "Listening for music tracks..."))

    def copy_link(self):
        if self.current_link:
            pyperclip.copy(self.current_link)
            self.set_temp_message("✔ Link copied.")
        else:
            self.set_temp_message("⚠ No link available.")

    def download_track(self):
        if not self.current_link:
            self.set_temp_message("⚠ No link available.")
            return

        file_name = self.current_link.split("/")[-1]
        save_path = filedialog.asksaveasfilename(
            defaultextension=os.path.splitext(file_name)[-1],
            filetypes=[("Music files", "*.*")],
            initialfile=file_name
        )

        if save_path:
            try:
                response = requests.get(self.current_link)
                with open(save_path, "wb") as f:
                    f.write(response.content)
                self.set_temp_message("✔ Download complete.")
                self.current_link = None
            except Exception:
                self.set_temp_message(f"⚠ Download failed.")
        else:
            self.set_temp_message("✘ Download canceled.")

    def on_close(self):
        try:
            if hasattr(self, "driver"):
                self.driver.quit()
        except:
            pass
        self.root.destroy()

    def run(self):
        self.root.mainloop()


def start_browser(gui: KeygenMusic98):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", False)
    service = Service(CHROMEDRIVER_PATH)
    gui.driver = webdriver.Chrome(service=service, options=chrome_options)
    gui.driver.get(SITE_URL)

    while True:
        time.sleep(1)
        for req in gui.driver.requests:
            if req.response and any(req.url.endswith(ext) for ext in ALLOWED_EXTENSIONS):
                if req.url not in gui.found_links:
                    gui.found_links.add(req.url)
                    gui.update_link(req.url)


def main():
    gui = KeygenMusic98()
    threading.Thread(target=start_browser, args=(gui,), daemon=True).start()
    gui.run()


if __name__ == "__main__":
    main()
