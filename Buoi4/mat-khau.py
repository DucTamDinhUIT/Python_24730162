import re

def kiem_tra_dang_nhap(user_id, password):
    # Kiem tra ID User
    if not (6 <= len(user_id) <= 24):
        return "ID phai tu 6 den 24 ky tu."
    if re.search(r"[!@#$%^&*()\-=+]", user_id):
        return "ID khong duoc chua ky tu dac biet !@#$%^&*()-=+."
    if " " in user_id:
        return "ID khong duoc chua khoang trang."

    # Kiem tra Password
    if not (6 <= len(password) <= 24):
        return "Mat khau phai tu 6 den 24 ky tu."
    if not re.search(r"[a-z]", password):
        return "Mat khau phai chua it nhat 1 chu cai thuong [a-z]."
    if not re.search(r"[A-Z]", password):
        return "Mat khau phai chua it nhat 1 chu cai hoa [A-Z]."
    if not re.search(r"[0-9]", password):
        return "Mat khau phai chua it nhat 1 chu so [0-9]."
    if not re.search(r"[$#@]", password):
        return "Mat khau phai chua it nhat 1 ky tu dac biet [$#@]."

    return "Dang nhap hop le!"

# Vi du su dung:
user = input("Nhap ID: ")
pw = input("Nhap Password: ")

print(kiem_tra_dang_nhap(user, pw))
