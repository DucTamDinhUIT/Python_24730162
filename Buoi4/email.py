import re

# update cac ten mien hop le
valid_domains = [
    "gmail.com", "yahoo.com", "hotmail.com", "outlook.com",
    "icloud.com", "yandex.com", "gov.vn", "edu.vn", "com.vn",
    "org.vn", "net.vn", "biz.vn", "info.vn",
]

def kiem_tra_email(email):
    # Tach phan truoc va sau @
    if "@" not in email:
        return "Khong phai dia chi email hop le."
    username, domain = email.partition("@")
    # Kiem tra domain
    if domain.lower() not in valid_domains:
        return "Ten mien khong nam trong danh sach cho phep."
    # check user - it nht 6 ky tu, khong khoang trang, khong ky tu dac biet
    if len(username) < 6:
        return "Ten dang nhap truoc @ phai co it nhat 6 ky tu."
    if re.search(r"\s", username):
        return "Ten dang nhap khong duoc chua khoang trang."
    if re.search(r"[^a-zA-Z0-9._%+-]", username):
        return "Ten dang nhap khong duoc chua ky tu dac biet."
    return "Dia chi email hop le."

email = input("Nhap email: ")
print(kiem_tra_email(email))