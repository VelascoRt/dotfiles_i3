from skimage.color import rgb2gray
from skimage.io import imread
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Read images
def read_image(img):    
    if len(img.shape) == 3:
        img = rgb2gray(img)
        img = (img * 255).astype(np.float32)
    else:
        img = img.astype(np.float32)
    return img

# Quantize an image
def quantize(img,i,k):
    q_img = (img/((2**k)-1)) * ((2**i)-1)
    return q_img

# Make an histogram of an image
def histogram(f,bins,normalize):
    hist = np.zeros(bins)
    w,h = f.shape
    intense = 0
    for x in range(w):
        for y in range(h):
            intense = int(f[x,y])
            hist[intense] += 1
    if normalize:
        hist /= w * h 
    return hist

# L - 1 
def multiply_bins(pr,l):
    out = pr
    for i in range(len(pr)):
        out[i] = (l - 1) * pr[i]
    return out

# Saving the lut thable in a csv file
def lut(values,q):
    df = pd.DataFrame(values)
    # df.to_csv(f"{path}{img_name}_lut{q}.csv")
    return df

def comparison(img1,img2,q):
    comp= np.hstack((img1,img2))
    return comp
    #plt.imshow(comp,cmap="gray")
    #plt.title("Ecualized image comparison")
    #plt.savefig(f"data/{img_name}{q}_ecualized_comparison.png")
    #plt.show()
 
def graph(img,q):
    bins = 2 ** q
    fig, (ax1,ax2) = plt.subplots(1,2)
    ax1.set_title("Image")
    ax2.set_title("Histogram")
    ax1.imshow(img,cmap="gray")
    hist = histogram(img,bins,False)
    ax2.plot(hist)
    plt.title("Image and its histogram")
    #if ecualized:
       # plt.savefig(f"data/{img_name}{q}_histogram_ecualized.png")
    #else:
        # plt.savefig(f"data/{img_name}{q}_histogram.png")
    plt.show()

# Equalize the image
def histogram_equalization(img,q): 
    bins = 2 ** q
    normalize = False
    hist = histogram(img,bins,normalize)

    # Probability of the intensities
    normalize = True
    pr_histogram = histogram(img,bins,normalize)

    # Sum of Probability of intensities
    prcumsum_histogram = pr_histogram.cumsum()
    pr = hist.cumsum()

    # L - 1 Sum of Probability of intensities
    multiply_histogram = multiply_bins(prcumsum_histogram,bins)

    # Floor of the last multiply
    floor_histogram = np.floor(multiply_histogram)

    # File of the values
    values_histogram = {"Intensity count" : hist, "Intensity Probability" : pr_histogram,"Cumulative sum of Probabilities" : prcumsum_histogram,"Multiply" : multiply_histogram,"Floor": floor_histogram}
    df = lut(values_histogram,q) 
    min_hist = np.ma.masked_equal(pr,0)
    min_hist = ((min_hist - min_hist.min()) * (bins-1)) /(min_hist.max() - min_hist.min())
    lutt = np.ma.filled(min_hist,0).astype("uint8") 
    img = img.astype("uint8") 
    # Ecualize the image
    return lutt[img]

