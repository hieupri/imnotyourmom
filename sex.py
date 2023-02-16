import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import time

def get_contributions(url):
    ua = UserAgent()
    headers = {'User-Agent': ua.random}
    
    # Gửi yêu cầu GET đến URL và lấy nội dung
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # Sử dụng BeautifulSoup để phân tích cú pháp HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        # Tìm tất cả các thẻ có class như yêu cầu
        tags = soup.find_all(class_="f4 text-normal mb-2")
        if tags:
            # Trích xuất con số từ nội dung của thẻ
            for tag in tags:
                # Sử dụng phương thức split() để tách chuỗi thành các phần
                # và lấy phần tử đầu tiên là con số
                contribution_text = tag.text.strip()
                contribution_number = int(contribution_text.split()[0].replace(',', ''))
                return contribution_number
    return None

def main():
    url = 'https://github.com/hieupri'
    previous_contributions = None
    
    while True:
        # Lấy số lần đóng góp hiện tại
        contributions = get_contributions(url)
        if contributions is not None:
            print("Số lần đóng góp trong năm qua:", contributions)
        else:
            print("Không thể truy cập hoặc không tìm thấy thông tin.")
        
        # Làm mới request
        time.sleep(60)  # Chờ một khoảng thời gian trước khi gửi yêu cầu mới

if __name__ == "__main__":
    main()
