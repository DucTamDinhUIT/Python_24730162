import random
import statistics

def tao_day_A():
    N = random.randint(30, 80)
    A = []
    for _ in range(N):
        if random.choice([True, False]):
            A.append(random.randint(-79, 39))
        else:
            A.append(round(random.uniform(-79, 39), 2))
    return A

def dem_kieu(A):
    kq = {'int': 0, 'float': 0}
    for x in A:
        if type(x) == int:
            kq['int'] += 1
        elif type(x) == float:
            kq['float'] += 1
    return kq

def dem_phan_tu(A):
    return len(A)

def sap_xep(A):
    return sorted(A)

def tinh_tb(A):
    return round(statistics.mean(A), 2)

def gia_tri_giua(B):
    n = len(B)
    if n % 2 == 0:
        return round((B[n//2-1] + B[n//2]) / 2, 2)
    else:
        return B[n//2]

def khoang_cach(A):
    return round(max(A) - min(A), 2)

def so_sanh(tb, giua):
    if tb == giua:
        return "Trung binh A bang gia tri giua B"
    elif tb > giua:
        return "Trung binh A lon hon gia tri giua B"
    else:
        return "Trung binh A nho hon gia tri giua B"

def main():
    A = tao_day_A()
    print("Day A:", A)
    kieu = dem_kieu(A)
    print("So nguyen:", kieu['int'], "So thuc:", kieu['float'])
    print("So phan tu:", dem_phan_tu(A))
    B = sap_xep(A)
    print("Day B:", B)
    tb = tinh_tb(A)
    print("Trung binh A:", tb)
    giua = gia_tri_giua(B)
    print("Gia tri giua B:", giua)
    kc = khoang_cach(A)
    print("Khoang cach max-min:", kc)
    print("So sanh:", so_sanh(tb, giua))

if __name__ == "__main__":
    main()