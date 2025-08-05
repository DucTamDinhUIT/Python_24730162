import random

def khoi_tao_nv():
    ds = []
    n = random.randint(50, 300)
    for i in range(n):
        ma = f"NV{i+1:03d}"
        ten = f"Nhan Vien {i+1}"
        luongcb = random.randint(5000000, 15000000)
        loai = random.choice(['vanphong', 'banhang'])
        if loai == 'vanphong':
            songay = random.randint(20, 26)
            nv = {
                'ma': ma,
                'ten': ten,
                'loai': loai,
                'luongcb': luongcb,
                'songay': songay,
                'luong': 0
            }
        else:
            sosp = random.randint(50, 200)
            nv = {
                'ma': ma,
                'ten': ten,
                'loai': loai,
                'luongcb': luongcb,
                'sosp': sosp,
                'luong': 0
            }
        ds.append(nv)
    return ds

def tinh_luong(ds):
    for nv in ds:
        if nv['loai'] == 'vanphong':
            nv['luong'] = nv['luongcb'] + nv['songay'] * 150000
        else:
            nv['luong'] = nv['luongcb'] + nv['sosp'] * 18000

def in_ds(ds):
    print("\nDanh sach nhan vien:")
    print(f"{'Ma':<8} {'Ten':<15} {'Loai':<10} {'LuongCB':<10} {'Luong':<10}")
    for nv in ds:
        print(f"{nv['ma']:<8} {nv['ten']:<15} {nv['loai']:<10} {nv['luongcb']:<10} {nv['luong']:<10}")

def tim_nv_ma(ds, ma):
    for nv in ds:
        if nv['ma'] == ma:
            return nv
    return None

def nv_luong_cao_nhat(ds):
    if not ds: return None
    return max(ds, key=lambda x: x['luong'])

def nv_banhang_luong_thap(ds):
    bh = [nv for nv in ds if nv['loai'] == 'banhang']
    if not bh: return None
    return min(bh, key=lambda x: x['luong'])

def main():
    ds = khoi_tao_nv()
    tinh_luong(ds)
    in_ds(ds)
    ma = "NV001"
    nv = tim_nv_ma(ds, ma)
    print("\nTim nhan vien ma", ma)
    if nv:
        print(f"Ma: {nv['ma']}, Ten: {nv['ten']}, Loai: {nv['loai']}, LuongCB: {nv['luongcb']}, Luong: {nv['luong']}")
    else:
        print(f"Khong tim thay nhan vien co ma {ma}")
    nvmax = nv_luong_cao_nhat(ds)
    if nvmax:
        print("\nNhan vien luong cao nhat:")
        print(f"Ma: {nvmax['ma']}, Ten: {nvmax['ten']}, Luong: {nvmax['luong']}")
    nvminbh = nv_banhang_luong_thap(ds)
    if nvminbh:
        print("\nNhan vien ban hang luong thap nhat:")
        print(f"Ma: {nvminbh['ma']}, Ten: {nvminbh['ten']}, Luong: {nvminbh['luong']}")
    else:
        print("\nKhong co nhan vien ban hang")

if __name__ == "__main__":
    main()