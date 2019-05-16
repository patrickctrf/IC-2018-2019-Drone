
from array import array

input_file = open('file', 'rb')
float_array = array('f')
float_array.fromfile(input_file, 2*3*2)
input_file.close()

print(float_array)
