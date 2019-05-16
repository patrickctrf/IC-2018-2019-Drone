from numpy.random import rand
from array import array

byte_matrix = rand(2,3,2)
print(byte_matrix)

aux = [[[float(0)]*byte_matrix.shape[0]]*byte_matrix.shape[1]*byte_matrix.shape[2]]

aux = byte_matrix.flatten()

print(aux)

a = array('f', aux)
output_file = open('file', 'wb')
a.tofile(output_file)
output_file.close()

#for i in range(0, byte_matrix.shape[0]):
#	for j in range(0, byte_matrix.shape[1]):
#		for k in range(0, byte_matrix.shape[2]):
#			f.write(float(byte_matrix[i,j,k]))



