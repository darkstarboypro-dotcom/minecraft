"""
Google Cloud Translation Setup Guide (Optional)
Hướng dẫn thiết lập Google Cloud Translate API (tùy chọn)

⚠️ CHỈ CẦN NẾU BẠN MUỐN DỊCH ONLINE

Ứng dụng Minecraft Translator đã hỗ trợ:
✅ OFFLINE MODE - Dịch offline với từ điển tích hợp (KHÔNG CẦN API)
❌ KHÔNG CẦN tài khoản Google Cloud
❌ KHÔNG CẦN thanh toán
✅ HOÀN TOÀN MIỄN PHÍ

Chỉ làm theo hướng dẫn dưới đây nếu bạn muốn:
- Dịch online với độ chính xác cao hơn
- Hỗ trợ nhiều ngôn ngữ hơn
"""

# Nếu bạn muốn sử dụng Google Translate (tùy chọn):

# Bước 1: Tạo Google Cloud Project
# 1. Truy cập: https://console.cloud.google.com
# 2. Nhấp "Select a Project" → "New Project"
# 3. Đặt tên project: "Minecraft Translator"
# 4. Nhấp "Create"

# Bước 2: Bật Translation API
# 1. Tìm kiếm "Translation" trong search bar
# 2. Nhấp "Cloud Translation API"
# 3. Nhấp "Enable"

# Bước 3: Tạo Service Account
# 1. Vào "APIs & Services" → "Credentials"
# 2. Nhấp "Create Credentials" → "Service Account"
# 3. Điền thông tin:
#    - Service account name: "minecraft-translator"
#    - Nhấp "Create and Continue"
# 4. Grant roles:
#    - Role: "Editor" hoặc "Cloud Translation API Editor"
#    - Nhấp "Continue"
# 5. Nhấp "Done"

# Bước 4: Tạo JSON Key
# 1. Vào "APIs & Services" → "Service Accounts"
# 2. Nhấp vào service account vừa tạo
# 3. Tab "Keys" → "Add Key" → "Create new key"
# 4. Chọn "JSON" → "Create"
# 5. File JSON sẽ download tự động
# 6. Đặt file vào thư mục dự án với tên: google-creds.json

# Bước 5: Cài đặt library
# pip install google-cloud-translate

# Bước 6: Sử dụng
# from google.cloud import translate_v2
# import os
#
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'google-creds.json'
# client = translate_v2.Client()
# result = client.translate_text(
#     source_language='en',
#     target_language='vi',
#     values=['Diamond Sword']
# )
# print(result[0]['translatedText'])

print("""
═══════════════════════════════════════════════════════════════
🎮 MINECRAFT VIETNAMESE TRANSLATOR - OFFLINE (MIỄN PHÍ)
═══════════════════════════════════════════════════════════════

✅ Ứng dụng đã sẵn sàng sử dụng OFFLINE

Không cần:
❌ Tài khoản Google Cloud
❌ Thanh toán
❌ API Key
❌ Kết nối Internet (có thể dùng offline)

Chỉ cần:
✅ Python 3.8+
✅ Tesseract OCR (tùy chọn, để chụp tooltip)

Cài đặt:
    pip install -r requirements.txt

Chạy:
    python minecraft_translator.py

═══════════════════════════════════════════════════════════════
""")
