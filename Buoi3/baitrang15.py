#• Tính tiền taxi theo số km quãng đường đi được.
#Cho biết:
#• 1 km đầu tiên: 20k
#• 3 km đầu tiên: 13k/km
#• Từ km thứ 4 đến km thứ 8: 12k/km
#• Còn lại giá 10k/km
#• Nếu đi hơn 100k thì giảm thêm 8% cho tổng tiền



def calculate_taxi_fare(km):
    if km <= 1:
        dongia = 20
    elif km <= 4:
        dongia = 20 + (km - 1) * 13
    elif km <= 8:
        dongia = 20 + 3 * 13 + (km - 4) * 12
    else:
        dongia = 20 + 3 * 13 + 4 * 12 + (km - 8) * 10

    if dongia > 100:
        dongia *= 0.92

    return dongia


km = float(input("Nhập số km đã đi: "))
print(f"Tiền taxi phải trả là: {calculate_taxi_fare(km)}k")

