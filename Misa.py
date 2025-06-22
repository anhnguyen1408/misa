from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os


ma_hoa_don = "B1HEIRR8N0WP"


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

try:
    trinh_duyet.get("https://www.meinvoice.vn/tra-cuu")
    time.sleep(2)  # đợi trang load

    o_nhap_ma = trinh_duyet.find_element(By.CSS_SELECTOR, "input[placeholder='Nhập mã tra cứu hóa đơn']")
    o_nhap_ma.send_keys(ma_hoa_don)
    time.sleep(1)

    nut_tim = trinh_duyet.find_element(By.CSS_SELECTOR, "button[type='submit']")
    nut_tim.click()
    time.sleep(5)  # chờ kết quả hiện ra

    try:
        nut_tai = trinh_duyet.find_element(By.XPATH, "//button[contains(text(),'Tải hóa đơn')]")
        nut_tai.click()
        print("✅ Hóa đơn đã được tải về trong thư mục:", thu_muc_tai)
    except:
        print("⚠️ Không tìm thấy hóa đơn với mã:", ma_hoa_don)

except Exception as loi:
    print("❌ Có lỗi xảy ra trong quá trình tra cứu:", loi)

finally:
    time.sleep(5)
    trinh_duyet.quit()
