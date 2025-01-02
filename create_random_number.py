import random
import os

#Hàm tạo ra một danh sách chứa count số  ngẫu nhiên.
def generate_numbers(count=10000):
    numbers = []
    for _ in range(count):
        random_suffix = random.randint(1000000, 9999999)
        number = f"096{random_suffix}"
        numbers.append(number)
    return numbers


def save_to_file(numbers, filename="096.txt", folder=None):
    if folder:
        os.makedirs(folder, exist_ok=True)
        filepath = os.path.join(folder, filename)
    else:
        filepath = filename

    with open(filepath, "w") as file:
        for number in numbers:
            file.write(number + "\n")

numbers = generate_numbers(10000000) #nơi tạo ra bao nhiêu số cần tạo
#nơi lưu file
save_to_file(numbers, filename="tênfile.txt", folder="nơi chứa file lưu")

print("Danh sách các số đã được lưu vào file tênfile.txt.")

