# Minecraft Vietnamese Translator - Offline Version

🎮 **Ứng dụng dịch mô tả vật phẩm Minecraft sang tiếng Việt**

**✅ HOÀN TOÀN MIỄN PHÍ - OFFLINE MODE - KHÔNG CẦN API**

## 🚀 Bắt đầu nhanh

### 1. Cài đặt Tesseract OCR (Tùy chọn)

Chỉ cần nếu muốn dùng tính năng **chụp tooltip từ Minecraft**

**Windows:**
- Tải: https://github.com/UB-Mannheim/tesseract/wiki
- Chạy installer (cài mặc định)

**macOS:**
```bash
brew install tesseract
```

**Linux:**
```bash
sudo apt-get install tesseract-ocr
```

### 2. Cài đặt Python Dependencies

```bash
pip install -r requirements.txt
```

### 3. Chạy ứng dụng

```bash
python minecraft_translator.py
```

## ✨ Tính năng

✅ **Dịch Offline** - Không cần Internet, không cần API  
✅ **Từ điển Minecraft** - 200+ từ được dịch sẵn  
✅ **Cache dịch** - Lưu bản dịch để nhanh hơn lần sau  
✅ **Giao diện đẹp** - GUI dễ sử dụng  
✅ **Chụp Tooltip** - Tự động nhận dạng text từ Minecraft  
✅ **Thêm dịch tùy chỉnh** - Tuỳ chỉnh từ điển của riêng bạn  

## 📖 Cách sử dụng

### Cách 1: Dán text và dịch

```
1. Mở ứng dụng: python minecraft_translator.py
2. Dán text tiếng Anh vào ô "Nhập hoặc dán text"
3. Nhấp "Dịch ngay"
4. Kết quả hiển thị dưới "Kết quả dịch (Tiếng Việt)"
```

**Ví dụ:**
```
Input:  Diamond Sword - A legendary weapon
Output: Kiếm Kim Cương - A legendary vũ khí
```

### Cách 2: Chụp Tooltip từ Minecraft

```
1. Mở Minecraft, vào Inventory
2. Di chuột vào vật phẩm
3. Nhấp nút "Chụp tooltip" trong ứng dụng
4. Text được chụp tự động → dịch → hiển thị kết quả
```

> **Yêu cầu:** Tesseract OCR phải được cài đặt

## 📚 Từ điển tích hợp

Ứng dụng hỗ trợ dịch **200+ thuật ngữ Minecraft** như:

### Vũ khí & Giáp
- Sword → Kiếm
- Pickaxe → Rìu
- Chestplate → Áo giáp

### Phù thủy
- Sharpness → Sắc nhọn
- Unbreaking → Bất tử
- Silk Touch → Cảm ứng lụa

### Hiệu ứng
- Regeneration → Phục hồi
- Speed → Tốc độ
- Strength → Sức mạnh

### Vật phẩm
- Diamond → Kim cương
- Iron → Sắt
- Gold → Vàng
- Netherite → Netherite

### Quái vật
- Zombie → Zombie
- Creeper → Creeper
- Enderman → Enderman

**Và còn nhiều từ khác...**

## ⚙️ Cấu hình

Chỉnh sửa `config.json`:

```json
{
  "auto_translate": true,
  "cache_translations": true,
  "gui": {
    "window_width": 900,
    "window_height": 700
  }
}
```

## 📁 Cấu trúc dự án

```
minecraft/
├── minecraft_translator.py    # Ứng dụng chính
├── detection.py               # Chụp & phát hiện text
├── dictionary.py              # Từ điển
├── config.json                # Cấu hình
├── translation_cache.json     # Cache dịch (tự tạo)
├── requirements.txt           # Dependencies
├── README.md                  # Hướng dẫn
└── OFFLINE_MODE.md           # Thông tin offline
```

## 🔧 Mở rộng từ điển

Thêm dịch tùy chỉnh vào `dictionary.py`:

```python
from dictionary import MinecraftDictionary

translator = MinecraftDictionary()
translator.add_custom_translation("ancient_debris", "mảnh vỡ cổ đại")
```

Hoặc chỉnh sửa file `DICTIONARY` trong `minecraft_translator.py`

## ❓ Troubleshooting

### ❌ Lỗi: "pytesseract.TesseractNotFoundError"

**Giải pháp:** Cài đặt Tesseract OCR (xem phần "Cài đặt Tesseract OCR")

### ❌ Lỗi: "ModuleNotFoundError: No module named 'tkinter'"

**Giải pháp:**
```bash
# Linux
sudo apt-get install python3-tk

# macOS
brew install python-tk

# Windows: Chạy lại Python installer, chọn "tcl/tk and IDLE"
```

### ❌ OCR không nhận dạng được text

**Giải pháp:**
- Tăng độ sáng/tương phản Minecraft
- Sử dụng texture pack mặc định
- Kiểm tra font size (font nhỏ OCR khó nhận)

## 🎯 So sánh: Offline vs Online

| Tính năng | Offline | Online (Google API) |
|----------|---------|------------------|
| Chi phí | ✅ Miễn phí | ❌ Có phí |
| Cần API | ✅ Không | ❌ Có |
| Tài khoản | ✅ Không | ❌ Cần Google Cloud |
| Độ chính xác | 🟡 Tốt | 🟢 Rất tốt |
| Hoạt động Offline | ✅ Có | ❌ Không |

## 🤝 Đóng góp

Muốn cải thiện ứng dụng?

1. Fork repository
2. Tạo branch mới: `git checkout -b feature/your-feature`
3. Commit: `git commit -am 'Add feature'`
4. Push: `git push origin feature/your-feature`
5. Tạo Pull Request

## 📝 Giấy phép

MIT License - Tự do sử dụng, sửa đổi, phân phối

## 💬 Liên hệ & Hỗ trợ

Gặp vấn đề? Tạo Issue trên GitHub:
https://github.com/darkstarboypro-dotcom/minecraft/issues

## 📚 Hướng dẫn đầy đủ

- [Cài đặt chi tiết](docs/INSTALL.md)
- [Offline Mode](OFFLINE_MODE.md)
- [Google Translate API (Tùy chọn)](google_setup.py)

---

**Happy Translating! 🎮✨**

*Dịch vô tận, Minecraft không bao giờ sợ hãi!*
