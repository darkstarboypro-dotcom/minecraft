"""
Minecraft Text Detector - Phát hiện text trong cửa sổ Minecraft
"""

import pyautogui
import time
from typing import Optional, Tuple, List
import threading

class MouseHoverDetector:
    """Phát hiện khi di chuột vào vật phẩm"""
    
    def __init__(self, callback=None):
        self.callback = callback
        self.is_running = False
        self.last_position = None
        self.hover_threshold = 0.5  # Thời gian hover tối thiểu (giây)
        self.hover_start_time = None
    
    def start(self):
        """Bắt đầu phát hiện"""
        self.is_running = True
        self.detector_thread = threading.Thread(
            target=self._detect_loop,
            daemon=True
        )
        self.detector_thread.start()
    
    def stop(self):
        """Dừng phát hiện"""
        self.is_running = False
    
    def _detect_loop(self):
        """Vòng lặp phát hiện"""
        while self.is_running:
            try:
                current_pos = pyautogui.position()
                
                # Kiểm tra nếu chuột di chuyển
                if current_pos != self.last_position:
                    self.hover_start_time = time.time()
                    self.last_position = current_pos
                else:
                    # Chuột đứng yên
                    if self.hover_start_time:
                        elapsed = time.time() - self.hover_start_time
                        if elapsed >= self.hover_threshold:
                            if self.callback:
                                self.callback(current_pos)
                            self.hover_start_time = None
                
                time.sleep(0.1)
            except Exception as e:
                print(f"Lỗi phát hiện hover: {e}")

class WindowDetector:
    """Phát hiện cửa sổ Minecraft"""
    
    @staticmethod
    def get_minecraft_windows() -> List[str]:
        """Lấy danh sách cửa sổ Minecraft"""
        try:
            import pygetwindow
            windows = pygetwindow.getWindowsWithTitle("Minecraft")
            return [w.title for w in windows]
        except:
            return []
    
    @staticmethod
    def get_window_bounds(window_title: str) -> Optional[Tuple[int, int, int, int]]:
        """Lấy tọa độ cửa sổ"""
        try:
            import pygetwindow
            windows = pygetwindow.getWindowsWithTitle(window_title)
            if windows:
                w = windows[0]
                return (w.left, w.top, w.width, w.height)
        except:
            pass
        return None

class ItemDetector:
    """Phát hiện vật phẩm dựa trên vị trí chuột"""
    
    # Vùng tooltip thông thường trong Minecraft
    TOOLTIP_WIDTH = 200
    TOOLTIP_HEIGHT = 100
    
    @staticmethod
    def get_tooltip_region(mouse_x: int, mouse_y: int) -> Tuple[int, int, int, int]:
        """Lấy vùng tooltip dựa trên vị trí chuột"""
        x = mouse_x + 10  # Offset từ con trỏ
        y = mouse_y + 10
        
        return (x, y, ItemDetector.TOOLTIP_WIDTH, ItemDetector.TOOLTIP_HEIGHT)
    
    @staticmethod
    def is_inventory_open(screenshot) -> bool:
        """Kiểm tra nếu inventory đang mở"""
        # Phát hiện các yếu tố điển hình của inventory
        # (Cần điều chỉnh dựa trên texture pack)
        return True  # Placeholder

class ScreenCapture:
    """Chụp ảnh màn hình"""
    
    @staticmethod
    def capture_region(x: int, y: int, width: int, height: int):
        """Chụp vùng cụ thể"""
        try:
            from PIL import ImageGrab
            bbox = (x, y, x + width, y + height)
            screenshot = ImageGrab.grab(bbox=bbox)
            return screenshot
        except Exception as e:
            print(f"Lỗi chụp ảnh: {e}")
            return None
    
    @staticmethod
    def capture_minecraft_window(window_bounds: Tuple[int, int, int, int]):
        """Chụp toàn bộ cửa sổ Minecraft"""
        x, y, width, height = window_bounds
        return ScreenCapture.capture_region(x, y, width, height)
