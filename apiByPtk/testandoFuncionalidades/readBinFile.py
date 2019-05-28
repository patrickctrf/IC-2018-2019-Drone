
from array import array
import numpy as np

input_file = open('/media/patrick/HD/Downloads/IC 2018-2019 Drone/PWM/IC-2018-2019-Drone/apiByPtk/testandoFuncionalidades/1559001923.4375935', 'rb')
float_array = array('f')
float_array.fromfile(input_file, 512*640*3)# (512, 640, 3): GlobalShutter, 
input_file.close()

imgReta = np.array(float_array)
imgMatriz = imgReta.reshape(512, 640, 3)

print(float_array)
