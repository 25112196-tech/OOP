class HangHoa:
    def __init__(self, ma, ten, nha_sx):
        self.__ma_hang = ma
        self.__ten_hang = ten
        self.__nha_sx = nha_sx

    def hien_thi(self):
        print(f"Ma: {self.__ma_hang} | Ten: {self.__ten_hang} | Nha SX: {self.__nha_sx}")

class HangDienMay(HangHoa):
    def __init__(self, ma, ten, nha_sx, gia, bao_hanh):
        super().__init__(ma, ten, nha_sx)
       
        self.gia = gia
        self.bao_hanh = bao_hanh

    def hien_thi(self):
        super().hien_thi() 
        print(f"-> Loai: Dien may | Gia: {self.gia:,} VNĐ | BH: {self.bao_hanh} thang")

class HangThucPham(HangHoa):
    def __init__(self, ma, ten, nha_sx, ngay_het_han):
        super().__init__(ma, ten, nha_sx)
        self.ngay_het_han = ngay_het_han

    def hien_thi(self):
        super().hien_thi()
        print(f"-> Loai: Thuc pham | Han dung: {self.ngay_het_han}")

tu_lanh = HangDienMay("DM01", "Tu lanh LG", "LG Electronics", 15000000, 24)
sua_tuoi = HangThucPham("TP01", "Sua TH True Milk", "TH Group", "20/05/2026")

tu_lanh.hien_thi()
sua_tuoi.hien_thi()