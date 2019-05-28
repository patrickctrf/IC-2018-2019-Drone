
from array import array

input_file = open('file', 'rb')
float_array = array('f')
float_array.fromfile(input_file, 512*640*3)# (512, 640, 3): GlobalShutter, 
input_file.close()

print(float_array)
