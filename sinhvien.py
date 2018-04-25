class SinhVien:
	Ten=""
	Namsinh=""
	Khoa=""
	def __init__(self,Ten,Namsinh,Khoa):
		self.Ten=Ten
		self.Namsinh=Namsinh
		self.Khoa=Khoa
	def getTen(self):        
        	return self.Ten
	def getNamsinh(self):        
        	return self.Namsinh
	def getKhoa(self):        
        	return self.Khoa

	def toString(self):
		print ("ten:"+self.Ten)
		print ("nam:"+self.Namsinh)
		print ("khoa:"+self.Khoa)


