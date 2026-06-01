"""
Minecraft Dictionary - Từ điển dịch tích hợp
"""

MINECRAFT_DICTIONARY = {
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
    
    # Cấu trúc
    "structure": "cấu trúc",
    "fortress": "pháo đài",
    "dungeon": "hầm ngục",
    "mansion": "lâu đài",
    "village": "làng",
    "stronghold": "thành trì",
    "end city": "thành phố đầu cuối",
    
    # Thực thể
    "entity": "thực thể",
    "mob": "quái vật",
    "animal": "động vật",
    "hostile": "thù địch",
    "passive": "không kích",
    "neutral": "trung lập",
    
    # Tương tác
    "right click": "nhấp chuột phải",
    "left click": "nhấp chuột trái",
    "attack": "tấn công",
    "interact": "tương tác",
    "use": "sử dụng",
    
    # Trạng thái
    "burning": "cháy",
    "drowning": "chết đuối",
    "suffocating": "ngạt thở",
    "falling": "rơi",
    "wither": "tàn rỗi",
    "void": "khoảng trống",
    "explosion": "nổ",
    
    # Chiều hướng
    "north": "bắc",
    "south": "nam",
    "east": "đông",
    "west": "tây",
    "up": "lên",
    "down": "xuống",
    
    # Thời gian
    "day": "ngày",
    "night": "đêm",
    "sunset": "lúc mặt trời lặn",
    "sunrise": "lúc mặt trời mọc",
    "morning": "sáng",
    "afternoon": "chiều",
    "evening": "tối",
    
    # Biến thể
    "variant": "biến thể",
    "color": "màu sắc",
    "texture": "kết cấu",
    "model": "mô hình",
    
    # Khác
    "level": "cấp độ",
    "experience": "kinh nghiệm",
    "requirement": "yêu cầu",
    "cooldown": "thời gian chờ",
    "charge": "sạc",
    "empty": "rỗng",
    "full": "đầy",
}

def get_translation(text: str) -> str:
    """Lấy dịch từ từ điển"""
    text_lower = text.lower()
    
    # Kiểm tra khớp chính xác
    if text_lower in MINECRAFT_DICTIONARY:
        return MINECRAFT_DICTIONARY[text_lower]
    
    # Kiểm tra khớp từng phần
    for key, value in MINECRAFT_DICTIONARY.items():
        if key in text_lower:
            return text.replace(key, value, flags=2)  # Case-insensitive
    
    return text

def add_custom_translation(english: str, vietnamese: str):
    """Thêm dịch tùy chỉnh"""
    MINECRAFT_DICTIONARY[english.lower()] = vietnamese

def load_dictionary_from_file(filepath: str):
    """Tải từ điển từ file JSON"""
    import json
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            custom_dict = json.load(f)
            MINECRAFT_DICTIONARY.update(custom_dict)
    except Exception as e:
        print(f"Lỗi tải từ điển: {e}")

def save_dictionary_to_file(filepath: str):
    """Lưu từ điển vào file JSON"""
    import json
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(MINECRAFT_DICTIONARY, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Lỗi lưu từ điển: {e}")
