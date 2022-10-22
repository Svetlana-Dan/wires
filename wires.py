import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import face
from skimage.measure import label
from skimage.morphology import binary_erosion


image = np.load('/Users/svetaparilova/Downloads/wires3.npy')

mask = np.array([[0,1,0], 
                [0,1,0],
                [0,1,0]])

plt.subplot(121)
plt.imshow(image)

count = 0
arr1 = image.copy()
for y in range(0, arr1.shape[0]):
    if  (arr1[y, 0]==1):
        count+=1
        result = label(binary_erosion(arr1[y:y+3, :], mask))
        arr1[y:y+3] = 0
        print(count, result.max())
        print()
result = binary_erosion(image,mask)
image = label(result)

plt.subplot(121)
plt.imshow(image)
plt.subplot(122)
plt.imshow(result)

