class Sinhvien:
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

	def inra(self):
		print ("ten:"+self.Ten)
		print ("nam:"+self.Namsinh)
		print ("khoa:"+self.Khoa)

sv1=Sinhvien("ngan","10","10")
sv1.inra()
