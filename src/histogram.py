import tools as tl
import matplotlib.pyplot as plt


# Insert path to.
path = rf"~/Desktop/School/Python/Hw3/data/"
# Insert image name
img_name = "image"
# Insert image.
img = tl.read_image(rf"{path}{img_name}.jpg")



# Quantize selected image
q = 8
img_q = tl.quantize(img,q,8)

# histogram of the quantize image
ecualize_img = tl.histogram_equalization(img_q,q,path,img_name)

# stack images
tl.comparison(img_q,ecualize_img,img_name,q)
tl.graph(img_q,img_name,q,False)
tl.graph(ecualize_img,img_name,q,True)

