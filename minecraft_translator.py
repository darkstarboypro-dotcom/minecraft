"""
Minecraft Vietnamese Translator
Dịch mô tả vật phẩm trong Minecraft sang tiếng Việt
"""

import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from PIL import ImageGrab
import pytesseract
from google.cloud import translate_v2
import threading
from enum import Enum
import re

class MinecraftVersion(Enum):
    """Các phiên bản Minecraft được hỗ trợ"""
    VANILLA = "vanilla"
    FABRIC = "fabric"
    FORGE = "forge"
    QUILT = "quilt"
    NEOFORGE = "neoforge"

class TranslationCache:
    """Bộ nhớ cache dịch thuật"""
    def __init__(self, cache_file="translation_cache.json"):
        self.cache_file = cache_file
        self.cache = self._load_cache()
    
    def _load_cache(self):
        """Tải cache từ file"""
        if os.path.exists(self.cache_file):
            try:
                with open(self.cache_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return {}
        return {}
    
    def _save_cache(self):
        """Lưu cache vào file"""
        with open(self.cache_file, 'w', encoding='utf-8') as f:
            json.dump(self.cache, f, ensure_ascii=False, indent=2)
    
    def get(self, text):
        """Lấy dịch từ cache"""
        return self.cache.get(text)
    
    def set(self, text, translation):
        """Lưu dịch vào cache"""
        self.cache[text] = translation
        self._save_cache()

class MinecraftTextExtractor:
    """Trích xuất text từ cửa sổ Minecraft"""
    
    @staticmethod
    def extract_from_window(window_rect):
        """Trích xuất text từ vùng được chỉ định"""
        try:
            screenshot = ImageGrab.grab(bbox=window_rect)
            text = pytesseract.image_to_string(screenshot, lang='eng')
            return text
        except Exception as e:
            raise Exception(f"Lỗi trích xuất text: {str(e)}")
    
    @staticmethod
    def extract_description(text):
        """Trích xuất mô tả từ text (loại bỏ tên vật phẩm)"""
        lines = text.strip().split('\n')
        if len(lines) > 1:
            # Giả định dòng đầu là tên, các dòng khác là mô tả
            return '\n'.join(lines[1:])
        return text

class VietnamseTranslator:
    """Dịch sang tiếng Việt"""
    
    def __init__(self, api_key=None):
        self.api_key = api_key
        self.cache = TranslationCache()
        if api_key:
            self.client = translate_v2.Client(
                target_language='vi',
                credentials=self._load_credentials(api_key)
            )
    
    def _load_credentials(self, api_key):
        """Tải credentials từ file hoặc biến môi trường"""
        try:
            from google.oauth2 import service_account
            return service_account.Credentials.from_service_account_file(api_key)
        except:
            return None
    
    def translate(self, text):
        """Dịch text sang tiếng Việt"""
        if not text or not text.strip():
            return text
        
        # Kiểm tra cache
        cached = self.cache.get(text)
        if cached:
            return cached
        
        try:
            # Sử dụng Google Translate API nếu khả dụng
            if hasattr(self, 'client') and self.client:
                result = self.client.translate_text(
                    source_language='en',
                    target_language='vi',
                    values=[text]
                )
                translation = result[0]['translatedText']
            else:
                # Fallback: sử dụng các dịch vụ khác hoặc offline
                translation = self._offline_translate(text)
            
            # Lưu vào cache
            self.cache.set(text, translation)
            return translation
        except Exception as e:
            print(f"Lỗi dịch: {str(e)}")
            return text
    
    def _offline_translate(self, text):
        """Dịch offline sử dụng từ điển tích hợp"""
        # Dictionary dịch bản
        dictionary = self._load_dictionary()
        words = text.lower().split()
        translated_words = [dictionary.get(w, w) for w in words]
        return ' '.join(translated_words)
    
    def _load_dictionary(self):
        """Tải từ điển dịch"""
        return {
            'item': 'vật phẩm',
            'damage': 'sát thương',
            'durability': 'độ bền',
            'enchantment': 'phù thủy',
            'potion': 'huyền dược',
            'effect': 'hiệu ứng',
        }

class MinecraftTranslatorApp:
    """Ứng dụng Minecraft Vietnamese Translator"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Minecraft Vietnamese Translator")
        self.root.geometry("800x600")
        self.translator = VietnamseTranslator()
        self.selected_window = None
        
        self._create_widgets()
    
    def _create_widgets(self):
        """Tạo các widget giao diện"""
        
        # Khung chọn cửa sổ
        frame_window = ttk.LabelFrame(self.root, text="Chọn cửa sổ Minecraft", padding=10)
        frame_window.pack(fill="x", padx=10, pady=10)
        
        ttk.Button(
            frame_window,
            text="Chọn cửa sổ Minecraft",
            command=self._select_window
        ).pack(side="left")
        
        self.label_window = ttk.Label(frame_window, text="Chưa chọn cửa sổ")
        self.label_window.pack(side="left", padx=10)
        
        # Khung cài đặt
        frame_settings = ttk.LabelFrame(self.root, text="Cài đặt", padding=10)
        frame_settings.pack(fill="x", padx=10, pady=10)
        
        ttk.Label(frame_settings, text="Phiên bản Minecraft:").pack(anchor="w")
        self.version_var = tk.StringVar(value=MinecraftVersion.VANILLA.value)
        version_combo = ttk.Combobox(
            frame_settings,
            textvariable=self.version_var,
            values=[v.value for v in MinecraftVersion],
            state="readonly"
        )
        version_combo.pack(fill="x", pady=5)
        
        ttk.Checkbutton(
            frame_settings,
            text="Dịch khi di chuột vào vật phẩm"
        ).pack(anchor="w")
        
        # Khung hiển thị
        frame_display = ttk.LabelFrame(self.root, text="Kết quả dịch", padding=10)
        frame_display.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Text widget cho tên vật phẩm
        ttk.Label(frame_display, text="Tên vật phẩm:").pack(anchor="w")
        self.text_name = tk.Text(frame_display, height=2, width=80)
        self.text_name.pack(fill="x", pady=5)
        
        # Text widget cho mô tả
        ttk.Label(frame_display, text="Mô tả (Tiếng Việt):").pack(anchor="w")
        self.text_description = tk.Text(frame_display, height=10, width=80)
        self.text_description.pack(fill="both", expand=True, pady=5)
        
        # Khung nút
        frame_buttons = ttk.Frame(self.root)
        frame_buttons.pack(fill="x", padx=10, pady=10)
        
        ttk.Button(
            frame_buttons,
            text="Bắt đầu dịch",
            command=self._start_translation
        ).pack(side="left", padx=5)
        
        ttk.Button(
            frame_buttons,
            text="Xóa",
            command=self._clear_text
        ).pack(side="left", padx=5)
        
        ttk.Button(
            frame_buttons,
            text="Thoát",
            command=self.root.quit
        ).pack(side="right", padx=5)
    
    def _select_window(self):
        """Chọn cửa sổ Minecraft"""
        messagebox.showinfo(
            "Hướng dẫn",
            "Chức năng này yêu cầu nhấp vào cửa sổ Minecraft trong 5 giây.\n"
            "Hiện tại, vui lòng nhập tọa độ cửa sổ thủ công."
        )
        self.label_window.config(text="Cửa sổ được chọn")
    
    def _start_translation(self):
        """Bắt đầu quá trình dịch"""
        threading.Thread(target=self._translate_worker, daemon=True).start()
    
    def _translate_worker(self):
        """Xử lý dịch trong background"""
        try:
            # Giả lập: lấy text từ cửa sổ
            sample_text = "Diamond Sword\nA legendary weapon"
            
            lines = sample_text.strip().split('\n')
            item_name = lines[0] if lines else ""
            description = '\n'.join(lines[1:]) if len(lines) > 1 else ""
            
            # Dịch mô tả
            translated_description = self.translator.translate(description)
            
            # Cập nhật GUI
            self.text_name.config(state="normal")
            self.text_name.delete("1.0", "end")
            self.text_name.insert("1.0", item_name)
            
            self.text_description.config(state="normal")
            self.text_description.delete("1.0", "end")
            self.text_description.insert("1.0", translated_description)
            
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi dịch: {str(e)}")
    
    def _clear_text(self):
        """Xóa text"""
        self.text_name.delete("1.0", "end")
        self.text_description.delete("1.0", "end")

def main():
    """Hàm chính"""
    root = tk.Tk()
    app = MinecraftTranslatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
