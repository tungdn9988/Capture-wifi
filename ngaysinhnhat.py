from datetime import datetime, timedelta

def generate_birthdays(start_year, end_year):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    
    current_date = start_date
    birthdays = []
    
    while current_date <= end_date:
        birthdays.append(current_date.strftime("%d%m%Y"))  # Xóa "/" trong định dạng
        current_date += timedelta(days=1)
    
    return birthdays

# Tạo danh sách ngày sinh từ 1960 đến 2027
birthdays_list = generate_birthdays(1960, 2027)

# Ghi ngày sinh nhật vào một tập tin
with open("birthdays_list.txt", "w") as file:
    for birthday in birthdays_list:
        file.write(birthday + "\n")
