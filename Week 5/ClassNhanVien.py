class CanBo:
    def __init__ (self, hoten, tuoi, gioitinh, diachi):
        self.hoten = hoten
        self.tuoi = tuoi
        self.gioitinh = gioitinh
        self.diachi = diachi

    def loai_cb (self):
        return "Can Bo"
    
    def hien_thi (self):
        print (f" [{self.loai_cb()}] {self.hoten}")
        print (f" Tuoi: {self.tuoi} | Gioi tinh: {self.gioitinh} | Dia chi: {self.diachi}")

class CongNhan (CanBo):
    def __init__ (self, hoten, tuoi, gioitinh, diachi, bac):
        super().__init__(hoten, tuoi, gioitinh, diachi)
        self.bac = bac
    
    def loai_cb (self):
        return "Cong Nhan"
    
    def hien_thi (self):
        super ().hien_thi()
        print (f"Bac: {self.bac}/10")

class KySu (CanBo):
    def __init__ (self, hoten, tuoi, gioitinh, diachi, nganh):
        super().__init__(hoten, tuoi, gioitinh, diachi)
        self.nganh = nganh
    
    def loai_cb (self):
        return "Ky Su"
    
    def hien_thi (self):
        super().hien_thi()
        print (f"Nganh: {self.nganh}")


class NhanVien (CanBo):
    def __init__ (self, hoten, tuoi, gioitinh, diachi, congviec):
        super().__init__ (hoten, tuoi, gioitinh, diachi)
        self.congviec = congviec

        def loai_cb (self):
            return "Nhan Vien"

        def hien_thi (self):
            super (). hien_thi()
            print (f"Cong viec: {self.congviec}")

class QuanLyCanBo:
    def __init__(self):
        self.__danhsach_cb = []

    def them (self):
        """Nhap thong tin va them can bo moi vao danh sach"""
        print ("\n---Them can bo moi---")
        print (" 1. Cong nhan")
        print (" 2. Ky su")
        print (" 3. Nhan vien")
        loai = input ("Chon loai can bo (1-3): ").strip()

        hoten = input ("Nhap ho va ten: ")
        tuoi = input ("Nhap tuoi: ")
        gioitinh = input ("Nhap gioi tinh: ")
        diachi = input ("Nhap dia chi: ")

        cb = None
        if loai == "1":
            bac = input ("Nhap bac (1-10): ")
            cb = CongNhan (hoten, tuoi, gioitinh, diachi, bac)
        elif loai == "2":
            nganh = input ("Nhap nganh: ")
            cb = KySu (hoten, tuoi, gioitinh, diachi, nganh)
        elif loai == "3":
            congviec = input ("Nhap cong viec: ")
            cb = NhanVien (hoten, tuoi, gioitinh, diachi, congviec)
        else:
            print ("Lua chon khong hop le!") 
            return
        
        if cb:
            self.__danhsach_cb.append(cb)
            print ("Them can bo moi thanh cong!")

    def timkiem (self):
        """Tim kiem can bo theo ho và ten"""
        hoten = input ("Nhap ho va ten can bo can tim: ").strip()
        for cb in self.__danhsach_cb:
            if cb.hoten.lower() == hoten.lower():
                cb.hien_thi()
                found = True
        if not found:
            print ("Khong tim thay can bo voi ho va ten nay.")
    
    def hienthi (self):
        """Hien thi thong tin tat ca can bo"""
        if not self.__danhsach_cb:
            print ("Danh sach can bo trong.")
            return
        print ("---Danh sach can bo---")
        for cb in self.__danhsach_cb:
            cb.hien_thi()
            print ("----------------------")
    
    def chay (self):
        """Chay chuong trinh quan ly can bo"""
        while True:
            print ("---Quan ly can bo---")
            print (" 1. Them can bo moi")
            print (" 2. Tim kiem can bo theo ho va ten")
            print (" 3. Hien thi thong tin tat ca can bo")
            print (" 4. Thoat")
            chon = input ("Chon chuc nang (1-4): ").strip()

            if chon == "1":
                self.them()
            elif chon == "2":
                self.timkiem()
            elif chon == "3":
                self.hienthi()
            elif chon == "4":
                print ("Thoat chuong trinh.")
                break
            else:
                print ("Lua chon khong hop le. Vui long chon lai.")

if __name__ == "__main__":
    qlcb = QuanLyCanBo()
    qlcb.chay()

