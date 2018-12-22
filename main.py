from PIL import Image
import numpy as np
import matplotlib.pylab as plt
im = Image.open("sample/IMG_8217.jpg")

print(im)

im2arr = np.array(im) # im2arr.shape: height x width x channel
arr2im = Image.fromarray(im2arr)

plt.imshow(im2arr)
plt.show()

print(np.min(im2arr[:,:,2]), np.max(im2arr[:,:,2]))

# substract the minimal colour intensity from each pixel.
# here, but not done yet

x = 860
y = 250
plt.imshow(im2arr[y+50:y+250, x+50:x+250, :])
plt.show()

green_r = np.mean(im2arr[y+50:y+250, x+50:x+250, 0])
green_g = np.mean(im2arr[y+50:y+250, x+50:x+250, 1])
green_b = np.mean(im2arr[y+50:y+250, x+50:x+250, 2])

print("green", green_r, green_g, green_b)


x = 2070
y = 250
plt.imshow(im2arr[y+50:y+250, x+50:x+250, :])
plt.show()

blue_r = np.mean(im2arr[y+50:y+250, x+50:x+250, 0])
blue_g = np.mean(im2arr[y+50:y+250, x+50:x+250, 1])
blue_b = np.mean(im2arr[y+50:y+250, x+50:x+250, 2])

print("blue", blue_r, blue_g, blue_b)



x = 800
y = 1020
plt.imshow(im2arr[y+50:y+250, x+50:x+250, :])
plt.show()

brown_r = np.mean(im2arr[y+50:y+250, x+50:x+250, 0])
brown_g = np.mean(im2arr[y+50:y+250, x+50:x+250, 1])
brown_b = np.mean(im2arr[y+50:y+250, x+50:x+250, 2])

print("brown", brown_r, brown_g, brown_b)

plt.plot([brown_r, brown_g, brown_b])
plt.plot([blue_r, blue_g, blue_b])
plt.plot([green_r, green_g, green_b])
plt.show()


for i in range(len(im2arr)):
    for j in range(len(im2arr[i])):
        if im2arr[i][j][0] > brown_r - 30 and im2arr[i][j][0] < brown_r + 30 and im2arr[i][j][1] > brown_g - 30 and im2arr[i][j][1] < brown_g + 30 and im2arr[i][j][2] > brown_b - 30 and im2arr[i][j][2] < brown_b + 30:
            print(i,j, "brown")
            im2arr[i, j, 0] = 0
            im2arr[i, j, 1] = 0
            im2arr[i, j, 2] = 0

plt.imshow(im2arr)
plt.show()