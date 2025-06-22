from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

with open("ma_hoa_don.txt", "r") as f:
    danh_sach_ma = [dong.strip() for dong in f if dong.strip()]

thu_muc_tai = os.path.join(os.getcwd(), "hoa_don_tai_ve")
if not os.path.exists(thu_muc_tai):
    os.makedirs(thu_muc_tai)

options = Options()
options.add_experimental_option("prefs", {
    "download.default_directory": thu_muc_tai,
    "download.prompt_for_download": False,
    "safebrowsing.enabled": True
})
options.add_argument("--start-maximized")

trinh_duyet = webdriver.Chrome(options=options)

for ma_hoa_don in danh_sach_ma:
    try:
        print(f"Đang tra cứu mã: {ma_hoa_don}")
        trinh_duyet.get("https://www.meinvoice.vn/tra-cuu")

        o_nhap = WebDriverWait(trinh_duyet, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Nhập mã tra cứu hóa đơn']"))
        )
        o_nhap.clear()
        o_nhap.send_keys(ma_hoa_don)

        nut_tim = WebDriverWait(trinh_duyet, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Tra cứu')]"))
        )
        nut_tim.click()

        time.sleep(5)

        try:
            nut_tai = WebDriverWait(trinh_duyet, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Tải hóa đơn')]"))
            )
            nut_tai.click()
            print(f"Đã tải hóa đơn cho mã: {ma_hoa_don}")
        except:
            print(f"Không tìm thấy hóa đơn cho mã: {ma_hoa_don}")

    except Exception as loi:
        print(f"Lỗi với mã {ma_hoa_don}: {loi}")

trinh_duyet.quit()
