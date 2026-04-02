import math

class Diem:
    def __init__ (self, x = 0.0, y = 0.0):
        self.x = x
        self.y = y

class HinhTron:
    def __init__(self, tam, ban_kinh):
        self.tam = tam
        self.ban_kinh = ban_kinh

class HinhChuNhat:
    def __init__ (self, goc_duoi, chieu_rong, chieu_dai):
        self.goc_duoi = goc_duoi
        self.chieu_dai = chieu_rong
        self.chieu_rong = chieu_dai

def khoang_cach (d1, d2):
    return math.sqrt ((d1.x - d2.x) ** 2 + (d1.y - d2.y) **2)

def diem_trong_vong_tron (vong_tron, diem):
    return khoang_cach (vong_tron.tam, diem) <= vong_tron.ban_kinh

def lay_goc_duoi_hcn(hcn):
    d1 = hcn.goc_duoi
    d2 = Diem (d1.x + hcn.chieu_rong, d1.y)
    d3 = Diem (d1.x, d1.y + hcn.chieu_dai)
    d4 = Diem (d1.x + hcn.chieu_rong, d1.y + hcn.chieu_dai)
    return [d1, d2, d3, d4]


def hcn_trong_vong_tron (vong_tron, hcn):
    goc_duoi = lay_goc_duoi_hcn (hcn)
    return all (diem_trong_vong_tron (vong_tron, d) for d in goc_duoi)

def hcn_giao_voi_vong_tron (vong_tron, hcn):
    goc_duoi = lay_goc_duoi_hcn (hcn)
    return any (diem_trong_vong_tron (vong_tron, d) for d in goc_duoi)

tam = Diem ( 2, 2)
vong_tron = HinhTron (tam, 23)

hcn_nho = HinhChuNhat (Diem (12,36), 17, 46)
print (f"Hcn nho nam trong vong tron? {hcn_trong_vong_tron (vong_tron, hcn_nho)}")

hcn_lon = HinhChuNhat (Diem (113,362), 173, 416)
print (f"Hcn lon co giao voi vong tron? {hcn_giao_voi_vong_tron (vong_tron, hcn_lon)}")
