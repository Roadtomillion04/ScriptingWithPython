import sys
import os
from PIL import Image
import glob #glob.glob finds the filepath of directory in pattern

'''you have to make it accept two arguemnts First one is JPG directory and second one is new directory to store PNG images '''
JPG_directory = sys.argv[1]
PNG_directory = sys.argv[2]

'''check PNG directory exists or not, if not create'''
if not os.path.exists(PNG_directory):
    os.makedirs(PNG_directory, exist_ok=True) #makedirs is similar to mkdir in cmd

'''Loop through Pokedex directory | Convert JPG to PNG | Save it to PNG Directory'''

if not os.path.exists(JPG_directory):
    print("No File named " + str(JPG_directory))

# We are not putting / after parent directory because we already put name\ in output
else:
    for filepath in os.listdir(JPG_directory): #filepath only returns filename
        all_img = Image.open(f'./{JPG_directory}{filepath}') #remeber you'll have to give parent directory

        print(os.path.splitext(filepath)) # THis returns in tuple
        clean_name = os.path.splitext(filepath)[0] #splitest is splitting name and .extensions

        all_img.save(f'./{PNG_directory}{clean_name}.png', 'png')

print(os.listdir(JPG_directory))

'''This wont work because it does not returns in list to iterate for loop
#    for filepath in glob.glob(f'./{JPG_directory}'): * grabs all file paths as we only have JPG images now
#        with Image.open(f'{JPG_directory}{filepath}') as img:
#            img_name = os.path.splitext(filepath)[0]
#            img.save(f'./{PNG_directory}{img_name}.png', 'png')
'''



