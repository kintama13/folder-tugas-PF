import collections
  
Student = collections.namedtuple('Mahasiswa', ['nama', 'umur', 'NIM'])
  
S = Student('Bilal', '20', '11201059')

print("Nama :", S.nama) 
print("Umur : ", S[1])
print("Nomor Induk Mahasiswa : ", getattr(S, 'NIM'))