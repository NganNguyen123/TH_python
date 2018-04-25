from sinhvien import SinhVien

a = []
n = int(input('Nhap so luong Sinh Vien can nhap : '))
x = n
while(x > 0):
	ten = raw_input( 'Nhap ten SV : ')
	namsinh = raw_input('Nhap nam sinh : ')
	khoa = raw_input('Nhap khoa : ')
	a.append(SinhVien(ten,namsinh,khoa))
	x = x - 1 
for abc in a:
	abc.toString()


