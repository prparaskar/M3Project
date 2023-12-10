import matplotlib.pyplot as plt
import cv2
import easyocr
from pylab import rcParams
from IPython.display import Image


rcParams['figure.figsize'] = 8, 16
reader = easyocr.Reader(['en', 'hi'])

file_name = "dataset\dev\hindi1.jpg"

Image(file_name)
output = reader.readtext(file_name)
print(output[1][1])
# cord = output[0][0]
# x_min, y_min = [int(min(idx)) for idx in zip(*cord)]
# x_max, y_max = [int(max(idx)) for idx in zip(*cord)]


# image = cv2.imread(file_name)
# cv2.rectangle(image,(x_min,y_min),(x_max,y_max),(255,0,0),2)
# plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    #  [([[445.6076433315133, 358.4975796624806],
    #     [654.1836785148745, 294.9784975501534], 
    #     [665.3923566684867, 346.5024203375194], 
    #     [456.81632148512557, 410.0215024498466]],
    #    'महाराष्ट्रश२जीसी', 0.588208565983764),
    #   ([[411.80053053104257, 404.00132632760636], 
    #     [724.9545652436879, 338.7138233733727],
    #     [741.1994694689574, 454.99867367239364],
    #    [427.04543475631215, 520.2861766266273]                                                                                                                                                                '२८६८', 0.8293330865762295)]