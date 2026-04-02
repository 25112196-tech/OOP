class SieuNhan:
    """Lop dai dien cho mot Sieu Nhan trong he thong."""
    def __init__ (self, ten: str, vu_khi: str, mau_sac: str):
        self.ten = ten
        self.vu_khi = vu_khi
        self.mau_sac = mau_sac

    def __str__(self):
        return f"Sieu nhan {self.ten:2} | Vu khi: {self.vu_khi:6} | Mau sac: {self.mau_sac}" 
    
sieu_nhan_A = SieuNhan ("A", "kiem", "do")
sieu_nhan_B = SieuNhan ("B", "khien", "xanh")

print ("Danh sach sieu nhan dã khoi tao: ")
print (sieu_nhan_A)
print (sieu_nhan_B)
    