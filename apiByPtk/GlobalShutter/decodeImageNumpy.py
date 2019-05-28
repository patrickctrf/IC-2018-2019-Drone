import numpy as np
import cv2

input_file = open('1559009040.6886272', 'rb')
		
imgMatriz = np.load(input_file)

input_file.close()

cv2.imshow("SimpleLive_Python_uEye_OpenCV", imgMatriz)
cv2.waitKey(1)# Nao sei direito pra que precisa disso, mas só mostra a img se fizer este comando.


