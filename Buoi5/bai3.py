# Cho dãy tên seqA:
# 1. Viết hàm khởi tạo giá trị tự động cho seqA gồm N phần tử các số nguyên
# (âm, dương) và số thực (âm, dương).
# • N chọn ngẫu nhiên từ 30 đến 80.
# • Các giá trị số nguyên, số thực chọn ngẫu nghiên từ -79 đến 39. Giá trị số thực
# được làm tròn 2 số thập phân.
# 2. Viết hàm kiểm tra kiểu dữ liệu từng phần tử.
# 3. Viết hàm thống kê số lượng phần tử có trong seqA.
# 4. Viết hàm sắp xếp dãy seqA thành dãy seqB tăng dần.
# 5. Viết hàm tính trung bình các phần tử trong seqA.

import random
def create_seqA():
    n = random.randint(30,80)
    print(f"Generated N: {n}")
    seqA = []
    for _ in range(n):
        if random.choice([True, False]):
            # Generate integer
            value = random.randint(-79, 39)
        else:
            # Generate float
            value = round(random.uniform(-79, 39), 2)
        seqA.append(value)
    return seqA 

def check_data_types(seqA):
    return [type(item) for item in seqA]

def count_elements(seqA):
    return len(seqA)

def sort_seqA(seqA):
    return sorted(seqA)

def calculate_average(seqA):
    if not seqA:
        return 0
    return sum(seqA) / len(seqA)

# Example usage
if __name__ == "__main__":
    seqA = create_seqA()
    print("Dãy seqA:", seqA)
    print("Kiểu dữ liệu từng phần tử:", check_data_types(seqA))
    print("Số lượng phần tử trong seqA:", count_elements(seqA))
    seqB = sort_seqA(seqA)
    print("Dãy seqB (sắp xếp tăng dần):", seqB)
    average = calculate_average(seqA)
    print("Trung bình các phần tử trong seqA:", average)