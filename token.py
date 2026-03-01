import requests
import re

def hunt_sctv_link():
    # Giả lập là trình duyệt để tvmienphi.org không chặn
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    url = "VTV https://tvmienphi.org/live-tv/xem-kenh-sctv5-truc-tuyen.html" # Trang chủ bạn tìm thấy
    
    try:
        r = requests.get(url, headers=headers)
        # Tìm link có cấu trúc cdn1...token...e=...
        match = re.search(r'https://[^\s"\']+\.m3u8\?token=[a-zA-Z0-9_-]+&e=\d+', r.text)
        if match:
            return match.group(0)
    except:
        return None

# Sau khi lấy được, ghi đè vào file m3u của bạn
link = hunt_sctv_link()
if link:
    with open("sctv.m3u", "w") as f:
        f.write(f"#EXTM3U\n#EXTINF:-1,SCTV 5 Auto\n{link}")
