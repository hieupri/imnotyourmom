import datetime
import os
import random
import time  # Import thư viện time để sử dụng hàm sleep

try:
    count = 0
    while True:  # Vòng lặp vô hạn
        today = datetime.date.today()

        current_year = today.year
        current_month = today.month
        current_day = today.day

        last_year = current_year - 1
        last_month = today.month
        last_day = current_day - 1  # In case it is a leap year

        start = datetime.date(last_year, last_month, last_day)
        end = datetime.date(current_year, current_month, current_day)
        res_date = start

        while res_date <= end:
            for i in range(random.randrange(1, 6)):
                with open('change-file.txt', 'a') as wf:
                    wf.write(f'\n{res_date}')
                os.system(f'git add .')
                os.system(f'git commit --date "{res_date}" -m "#{i} commit for {res_date}"')
                count += 1
                if count >= 5000:
                    raise StopIteration  # Raise ngoại lệ để thoát khỏi vòng lặp
            res_date += datetime.timedelta(days=1)

        # Chờ 1 giờ trước khi chạy lại
        time.sleep(1)  # 3600 giây = 1 giờ

except StopIteration:
    print("Đã hoàn thành 5000 lần chạy.")
except KeyboardInterrupt:
    print("Chương trình đã dừng bởi người dùng.")
