import datetime
import os
import random
import time  # Import thư viện time để sử dụng hàm sleep

try:
    count = 0
    start_date = datetime.date(1, 1, 1) 
    end_date = datetime.date(2024, 1, 1)

    while True:  # Vòng lặp vô hạn
        res_date = start_date

        while res_date < end_date:
            for i in range(random.randrange(1, 6)):
                with open('change-file.txt', 'a') as wf:
                    wf.write(f'\n{res_date}')
                os.system(f'git add .')
                os.system(f'git commit --date "{res_date}" -m "#{i} commit for {res_date}"')
                count += 1
                if count >= 5000000:
                    raise StopIteration  # Raise ngoại lệ để thoát khỏi vòng lặp
            res_date += datetime.timedelta(days=1)

        # Chờ 1 giờ trước khi chạy lại
        time.sleep(1)  # 3600 giây = 1 giờ

except StopIteration:
    print("Đã hoàn thành 5000 lần chạy.")
except KeyboardInterrupt:
    print("Chương trình đã dừng bởi người dùng.")