"""
Minecraft Vietnamese Translator - OFFLINE VERSION
Dịch mô tả vật phẩm trong Minecraft sang tiếng Việt (HOÀN TOÀN MIỄN PHÍ)
Không cần tài khoản Google Cloud, không cần thanh toán
"""

import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from PIL import ImageGrab
import pytesseract
import threading
from enum import Enum
import re
from typing import Dict

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
        return self.cache.get(text.lower())
    
    def set(self, text, translation):
        """Lưu dịch vào cache"""
        self.cache[text.lower()] = translation
        self._save_cache()

class MinecraftDictionary:
    """Từ điển Minecraft tiếng Việt - Hoàn toàn offline"""
    
    # Từ điển Minecraft tiếng Anh → Tiếng Việt
    DICTIONARY = {
        # Vật phẩm cơ bản
        "item": "vật phẩm",
        "block": "khối",
        "tool": "dụng cụ",
        "weapon": "vũ khí",
        "armor": "giáp",
        "food": "thức ăn",
        "material": "vật liệu",
        
        # Thuộc tính
        "damage": "sát thương",
        "durability": "độ bền",
        "enchantment": "phù thủy",
        "effect": "hiệu ứng",
        "rarity": "độ hiếm",
        "stackable": "có thể xếp chồng",
        
        # Phù thủy
        "sharpness": "sắc nhọn",
        "efficiency": "hiệu suất",
        "unbreaking": "bất tử",
        "fortune": "may mắn",
        "silk touch": "cảm ứng lụa",
        "flame": "lửa",
        "knockback": "hất lùi",
        "power": "sức mạnh",
        "mending": "sửa chữa",
        "protection": "bảo vệ",
        "fire protection": "bảo vệ lửa",
        "blast protection": "bảo vệ nổ",
        "projectile protection": "bảo vệ phát xạ",
        "respiration": "hô hấp",
        "aqua affinity": "mối quan hệ nước",
        "frost walker": "người đi bộ sương giá",
        "depth strider": "bước sâu",
        
        # Hiệu ứng
        "potion": "huyền dược",
        "instant health": "sức khỏe tức thì",
        "regeneration": "phục hồi",
        "weakness": "yếu đuối",
        "poison": "chất độc",
        "slowness": "chậm chạp",
        "speed": "tốc độ",
        "haste": "vội vàng",
        "fatigue": "mệt mỏi",
        "strength": "sức mạnh",
        "night vision": "nhìn ban đêm",
        "invisibility": "vô hình",
        "blindness": "mù lòa",
        "nausea": "buồn nôn",
        "resistance": "kháng cự",
        "fire resistance": "kháng lửa",
        "water breathing": "hô hấp dưới nước",
        "absorption": "hấp thụ",
        "saturation": "bão hòa",
        "glowing": "phát sáng",
        "levitation": "bay lơ lửng",
        "luck": "may mắn",
        "unluck": "xui xẻo",
        "mining fatigue": "mệt mỏi khai thác",
        "conduit power": "sức mạnh ống dẫn",
        
        # Vật phẩm đặc biệt
        "diamond": "kim cương",
        "emerald": "ngọc lục bảo",
        "gold": "vàng",
        "iron": "sắt",
        "coal": "than",
        "copper": "đồng",
        "amethyst": "tím",
        "netherite": "netherite",
        "obsidian": "obsidian",
        "stone": "đá",
        "dirt": "đất",
        "grass": "cỏ",
        "wood": "gỗ",
        "oak": "sồi",
        "birch": "bạch dương",
        "spruce": "vân sam",
        "jungle": "rừng",
        "acacia": "acacia",
        "dark oak": "sồi tối",
        
        # Cấu trúc
        "structure": "cấu trúc",
        "fortress": "pháo đài",
        "dungeon": "hầm ngục",
        "mansion": "lâu đài",
        "village": "làng",
        "stronghold": "thành trì",
        "end city": "thành phố đầu cuối",
        "nether fortress": "pháo đài nether",
        "temple": "đền thờ",
        "igloo": "igloo",
        "desert": "sa mạc",
        
        # Thực thể
        "entity": "thực thể",
        "mob": "quái vật",
        "animal": "động vật",
        "hostile": "thù địch",
        "passive": "không kích",
        "neutral": "trung lập",
        "zombie": "zombie",
        "creeper": "creeper",
        "skeleton": "bộ xương",
        "spider": "nhện",
        "enderman": "enderman",
        "pig": "lợn",
        "cow": "bò",
        "sheep": "cừu",
        "chicken": "gà",
        "horse": "ngựa",
        "villager": "dân làng",
        "iron golem": "golem sắt",
        "snow golem": "golem tuyết",
        "wither": "wither",
        "ender dragon": "rồng ender",
        
        # Tương tác
        "right click": "nhấp chuột phải",
        "left click": "nhấp chuột trái",
        "attack": "tấn công",
        "interact": "tương tác",
        "use": "sử dụng",
        "place": "đặt",
        "break": "phá",
        
        # Trạng thái
        "burning": "cháy",
        "drowning": "chết đuối",
        "suffocating": "ngạt thở",
        "falling": "rơi",
        "tint": "tàn rỗi",
        "void": "khoảng trống",
        "explosion": "nổ",
        "wet": "ướt",
        "on fire": "đang cháy",
        
        # Chiều hướng
        "north": "bắc",
        "south": "nam",
        "east": "đông",
        "west": "tây",
        "up": "lên",
        "down": "xuống",
        "above": "phía trên",
        "below": "phía dưới",
        
        # Thời gian
        "day": "ngày",
        "night": "đêm",
        "sunset": "lúc mặt trời lặn",
        "sunrise": "lúc mặt trời mọc",
        "morning": "sáng",
        "afternoon": "chiều",
        "evening": "tối",
        "tick": "tick",
        
        # Khác
        "level": "cấp độ",
        "experience": "kinh nghiệm",
        "requirement": "yêu cầu",
        "cooldown": "thời gian chờ",
        "charge": "sạc",
        "empty": "rỗng",
        "full": "đầy",
        "infinite": "vô hạn",
        "max": "tối đa",
        "min": "tối thiểu",
    }
    
    def __init__(self):
        self.cache = TranslationCache()
    
    def translate(self, text: str) -> str:
        """Dịch text sang tiếng Việt (offline)"""
        if not text or not text.strip():
            return text
        
        # Kiểm tra cache
        cached = self.cache.get(text)
        if cached:
            return cached
        
        # Dịch từng từ
        words = text.lower().split()
        translated_words = []
        
        for word in words:
            # Xóa dấu câu
            clean_word = word.strip('.,;:!?')
            punctuation = word[len(clean_word):]
            
            # Tìm dịch
            if clean_word in self.DICTIONARY:
                translated = self.DICTIONARY[clean_word] + punctuation
            else:
                translated = word
            
            translated_words.append(translated)
        
        result = ' '.join(translated_words)
        self.cache.set(text, result)
        return result
    
    def add_custom_translation(self, english: str, vietnamese: str):
        """Thêm dịch tùy chỉnh"""
        self.DICTIONARY[english.lower()] = vietnamese

class MinecraftTextExtractor:
    """Trích xuất text từ cửa sổ Minecraft"""
    
    @staticmethod
    def extract_from_region(x: int, y: int, width: int, height: int):
        """Trích xuất text từ vùng được chỉ định"""
        try:
            screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))
            text = pytesseract.image_to_string(screenshot, lang='eng')
            return text.strip()
        except Exception as e:
            raise Exception(f"Lỗi trích xuất text: {str(e)}")

class MinecraftTranslatorApp:
    """Ứng dụng Minecraft Vietnamese Translator - OFFLINE"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Minecraft Vietnamese Translator (Offline)")
        self.root.geometry("900x700")
        self.root.resizable(True, True)
        
        self.translator = MinecraftDictionary()
        self.extractor = MinecraftTextExtractor()
        self.is_monitoring = False
        
        # Style
        style = ttk.Style()
        style.theme_use('clam')
        
        self._create_widgets()
    
    def _create_widgets(self):
        """Tạo các widget giao diện"""
        
        # Header
        header_frame = ttk.Frame(self.root, relief="sunken", height=60)
        header_frame.pack(fill="x", padx=0, pady=0)
        
        ttk.Label(
            header_frame,
            text="🎮 Minecraft Vietnamese Translator (OFFLINE)",
            font=("Arial", 14, "bold")
        ).pack(anchor="w", padx=15, pady=10)
        
        # Khung nhập text
        frame_input = ttk.LabelFrame(self.root, text="📝 Nhập hoặc dán text", padding=15)
        frame_input.pack(fill="x", padx=15, pady=10)
        
        ttk.Label(frame_input, text="Text tiếng Anh:", font=("Arial", 10)).pack(anchor="w", pady=(0, 5))
        
        self.text_input = tk.Text(frame_input, height=4, width=100, font=("Arial", 10))
        self.text_input.pack(fill="both", expand=True, pady=5)
        
        # Khung nút
        button_frame = ttk.Frame(self.root)
        button_frame.pack(fill="x", padx=15, pady=10)
        
        ttk.Button(
            button_frame,
            text="🔄 Dịch ngay",
            command=self._translate_now
        ).pack(side="left", padx=5)
        
        ttk.Button(
            button_frame,
            text="🖱️ Chụp tooltip",
            command=self._capture_tooltip
        ).pack(side="left", padx=5)
        
        ttk.Button(
            button_frame,
            text="🗑️ Xóa",
            command=self._clear_all
        ).pack(side="left", padx=5)
        
        # Khung hiển thị kết quả
        frame_output = ttk.LabelFrame(self.root, text="✅ Kết quả dịch (Tiếng Việt)", padding=15)
        frame_output.pack(fill="both", expand=True, padx=15, pady=10)
        
        self.text_output = tk.Text(frame_output, height=8, width=100, font=("Arial", 11, "bold"), bg="#e8f5e9")
        self.text_output.pack(fill="both", expand=True)
        
        # Khung info
        info_frame = ttk.Frame(self.root, relief="sunken")
        info_frame.pack(fill="x", padx=0, pady=0)
        
        self.label_info = ttk.Label(
            info_frame,
            text="✅ Sẵn sàng - Offline mode (hoàn toàn miễn phí, không cần API)",
            font=("Arial", 9),
            foreground="green"
        )
        self.label_info.pack(anchor="w", padx=15, pady=8)
    
    def _translate_now(self):
        """Dịch text ngay lập tức"""
        text = self.text_input.get("1.0", "end").strip()
        
        if not text:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập text để dịch")
            return
        
        try:
            translated = self.translator.translate(text)
            
            self.text_output.config(state="normal")
            self.text_output.delete("1.0", "end")
            self.text_output.insert("1.0", translated)
            
            self.label_info.config(text=f"✅ Dịch xong - {len(text)} ký tự", foreground="green")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi dịch: {str(e)}")
    
    def _capture_tooltip(self):
        """Chụp tooltip từ Minecraft"""
        messagebox.showinfo(
            "📸 Chụp Tooltip",
            "1. Đảm bảo Minecraft đang mở\n"
            "2. Di chuột vào vật phẩm\n"
            "3. Cửa sổ này sẽ ghi lại text\n\n"
            "Tính năng này yêu cầu Tesseract OCR.\n"
            "Nếu chưa cài, vui lòng cài đặt trước."
        )
        
        try:
            # Chụp vùng tooltip (200x100 pixels ở vị trí chuột)
            import pyautogui
            x, y = pyautogui.position()
            
            text = self.extractor.extract_from_region(x + 10, y + 10, 250, 150)
            
            if text:
                self.text_input.delete("1.0", "end")
                self.text_input.insert("1.0", text)
                self._translate_now()
                self.label_info.config(text="✅ Chụp và dịch thành công", foreground="green")
            else:
                self.label_info.config(text="⚠️ Không tìm thấy text", foreground="orange")
        except Exception as e:
            self.label_info.config(text=f"❌ Lỗi: {str(e)}", foreground="red")
            messagebox.showerror("Lỗi", f"Lỗi chụp tooltip: {str(e)}")
    
    def _clear_all(self):
        """Xóa tất cả"""
        self.text_input.delete("1.0", "end")
        self.text_output.delete("1.0", "end")
        self.label_info.config(text="✅ Sẵn sàng", foreground="green")

def main():
    """Hàm chính"""
    root = tk.Tk()
    app = MinecraftTranslatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
