# Minecraft Vietnamese Translator - Hướng dẫn cài đặt

## 1. Yêu cầu hệ thống
- Python 3.8+
- Windows, macOS hoặc Linux
- Tesseract OCR (để nhận dạng text từ ảnh)
- Google Cloud API Key (tùy chọn, để dịch chính xác hơn)

## 2. Cài đặt

### Bước 1: Clone repository
```bash
git clone https://github.com/darkstarboypro-dotcom/minecraft
cd minecraft
```

### Bước 2: Cài đặt Tesseract OCR

**Windows:**
- Tải từ: https://github.com/UB-Mannheim/tesseract/wiki
- Cài đặt với đường dẫn mặc định

**macOS:**
```bash
brew install tesseract
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install tesseract-ocr
```

### Bước 3: Cài đặt Python dependencies
```bash
pip install -r requirements.txt
```

### Bước 4 (Tùy chọn): Cài đặt Google Cloud Translate

1. Tạo tài khoản Google Cloud
2. Bật API Translate
3. Tạo service account và tải JSON key
4. Đặt biến môi trường:
```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/key.json"
```

## 3. Sử dụng

### Chạy ứng dụng
```bash
python minecraft_translator.py
```

### Hướng dẫn sử dụng

1. **Chọn cửa sổ Minecraft**: Nhấp "Chọn cửa sổ Minecraft" và chọn cửa sổ Minecraft đang chạy
2. **Chọn phiên bản**: Chọn loại Minecraft (Vanilla, Fabric, Forge, v.v.)
3. **Bắt đầu dịch**: 
   - Di chuột vào vật phẩm trong Minecraft
   - Nhấp "Bắt đầu dịch"
   - Ứng dụng sẽ hiển thị mô tả dịch sang tiếng Việt

## 4. Tính năng

✅ Dịch mô tả vật phẩm (ItemStack tooltips)
✅ Hỗ trợ Vanilla, Fabric, Forge, Quilt, NeoForge
✅ Bộ nhớ cache dịch để dịch nhanh hơn
✅ Giao diện dễ sử dụng
✅ Hỗ trợ OCR để nhận dạng text từ ảnh
✅ Dịch trực tuyến hoặc offline

## 5. Cấu hình

Tạo file `config.json` để tùy chỉnh:

```json
{
  "minecraft_window_title": "Minecraft",
  "auto_translate": true,
  "translation_language": "vi",
  "use_google_api": true,
  "cache_translations": true,
  "cache_file": "translation_cache.json"
}
```

## 6. Khắc phục sự cố

### Tesseract không tìm thấy
Windows: Thêm vào `minecraft_translator.py`:
```python
import pytesseract
pytesseract.pytesseract.pytesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

### Google API không hoạt động
- Kiểm tra Google Cloud credentials
- Đảm bảo API Translate được bật
- Đảm bảo có đủ quota

### OCR không chính xác
- Điều chỉnh độ sáng/tương phản của Minecraft
- Sử dụng font nhỏ hơn trong cài đặt

## 7. Phát triển

Muốn đóng góp? Tạo pull request hoặc issue!

## 8. Giấy phép

MIT License

## 9. Hỗ trợ

Nếu gặp vấn đề, vui lòng tạo issue trên GitHub.
