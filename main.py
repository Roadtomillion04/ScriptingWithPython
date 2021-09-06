from PIL import Image, ImageFilter
'''Image.open only looks for an image'''

                    #filepath
img1 = Image.open("./Pokedex/pikachu.jpg")
img2 = Image.open("./Pokedex/squirtle.jpg")
img3 = Image.open("./Pokedex/bulbasaur.jpg")

print(img1)
print(img1.format)
print(img1.size)
print(img1.mode)

# we can filter the image
blur_image = img1.filter(ImageFilter.BLUR)
smooth_image = img2.filter(ImageFilter.SMOOTH)
sharp_image = img3.filter(ImageFilter.SHARPEN)

# to save it        #filepath            #format
blur_image.save("Blurred Pikachu.png", "png") # The reason why it's converted to png because JPEG won't support filters
smooth_image.save("Smooth Squirtle.png", "png")
sharp_image.save("Sharp Bulbasaur.png", "png")

img4 = Image.open("./Blurred Pikachu.png")
print(img4.format)

'''we can use convert to change mode like rgb'''
convert_img = img1.convert("L") #L means greyscale which is black and white
convert_img.save("Grey Pikachu.png", "png")

'''To show in editor'''
#convert_img.show()

'''we can rotate, resize'''
rotation = convert_img.rotate(180)
rotation.save("rotated Pikachu.png", 'png')
#rotation.show()

resize_img = rotation.resize((320, 320))
'''resize accepts tuple value'''

#resize_img.show() #but remember filepath is different and it's not saved


'''To crop a image'''
with Image.open("./Grey Pikachu.png") as im:
                      #left,top,right,bottom
    crop_dimensions = (100, 100, 400, 400)
    im.crop(crop_dimensions).show()

'''resizing larger size images'''
with Image.open("./astro.jpg") as new_img:
    new_img.thumbnail((400, 300)) #We use thumbnail here because it won't squish the image on compression
    new_img.save("Thumbnail.jpg")
    new_img.show()

    print(new_img.size) # we wont get exact size here because thumbnail chooses best fit size

 