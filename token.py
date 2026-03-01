import requests
import re

url_nguon = "https://tvmienphi.org/live-tv/xem-kenh-sctv5-truc-tuyen.html" 

def hunt_link():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Referer': 'https://tvmienphi.org/'
    }
    try:
        response = requests.get(url_nguon, headers=headers, timeout=20)
        print(f"Trạng thái web: {response.status_code}") # In ra mã trạng thái
        
        # Tìm mọi link có đuôi m3u8 và có token
        pattern = r'(https?://[^\s"\']+\.m3u8\?[^\s"\']+token=[a-zA-Z0-9_-]+[^\s"\']*)'
        match = re.search(pattern, response.text)
        
        if match:
            return match.group(0)
    except Exception as e:
        print(f"Lỗi kết nối: {e}")
    return None

new_link = hunt_link()

if new_link:
    with open("sctv_auto.m3u", "w", encoding="utf-8") as f:
        f.write("#EXTM3U\n#EXTINF:-1, SCTV 5 Auto\n" + new_link)
    print("Đã tìm thấy và lưu link!")
else:
    print("Không tìm thấy link trong mã nguồn trang web.")
    # In ra một đoạn nhỏ mã nguồn để kiểm tra (tùy chọn)
    # print(response.text[:500]) 
