# Buoi4/bai1.py
str_input = input("Nhap chuoi: ")


print(f"Do dai chuoi: {len(str_input)}")


ky_tu_dac_biet = "!@#$%^&*()-=+./"
chu_thuong = []
chu_hoa = []
chu_so = []
dac_biet = []


for char in str_input:
    if char in ky_tu_dac_biet:
        dac_biet.append(char)
    elif char.islower():
        chu_thuong.append(char)
    elif char.isupper():
        chu_hoa.append(char)
    elif char.isdigit():
        chu_so.append(char)


print(f"\nSo ky tu dac biet: {len(dac_biet)} -> {dac_biet}")
print(f"So chu cai thuong [a-z]: {len(chu_thuong)} -> {chu_thuong}")
print(f"So chu cai hoa [A-Z]: {len(chu_hoa)} -> {chu_hoa}")
print(f"So chu so [0-9]: {len(chu_so)} -> {chu_so}")