#Script to make the HIRS data decoded from Satdump into a concise GIF to view the layers! - Kassy
from PIL import Image
import os


def make_gif():
    global images
    print('Making Gif...')
    frames = []
    if jpgCloudDetection in images:
         frame0 = Image.open(f'{folder}\\{jpgCloudDetection}')
         frames.append(frame0)
    if jpgN2OSounding in images:
         frame1 = Image.open(f'{folder}\\{jpgN2OSounding}')
         frames.append(frame1)
    if jpgLowTroposphere in images:
         frame2 = Image.open(f'{folder}\\{jpgLowTroposphere}')
         frames.append(frame2)
    if jpgMidTroposphere in images:
         frame3 = Image.open(f'{folder}\\{jpgMidTroposphere}')
         frames.append(frame3)
    if jpgHighTroposphere in images:
         frame4= Image.open(f'{folder}\\{jpgHighTroposphere}')
         frames.append(frame4)
    if jpgTopTroposphere in images:
         frame5 = Image.open(f'{folder}\\{jpgTopTroposphere}')
         frames.append(frame5)
    if jpgLowstratosphere in images:
         frame6 = Image.open(f'{folder}\\{jpgLowstratosphere}')
         frames.append(frame6)
    if jpgMidStratosphere in images:
         frames7 = Image.open(f'{folder}\\{jpgMidStratosphere}')
         frames.append(frames7)
           
    frame_one = frames[0]
    frame_one.save(f"{folder}\\Atmosphere_Layers.gif", format="GIF", append_images=frames,
               save_all=True, duration=500, loop=0)
    print(f'Gif saved in {folder}\\Atmosphere_Layers.png')
    
def makejpg():
   global images
   images = list(os.listdir(folder)) #Get images from Folder
   
   print(f"Images: {images}")

   if {pngN2OSounding} in images: #convert each image from png to jpg to make compatible with gif maker
         jpg = Image.open(f'{folder}\\{pngN2OSounding}', mode='r')
         jpg.save(f'{folder}\\{jpgN2OSounding}')
         print(f'\n{folder}\\{jpgN2OSounding} saved.')
   if pngCloudDetection in images:
         jpg = Image.open(f'{folder}\\{pngCloudDetection}', mode='r')
         jpg.save(f'{folder}\\{jpgCloudDetection}')
         print(f'\n{folder}\\{jpgCloudDetection} saved.')
   if pngLowTroposphere in images:
         jpg = Image.open(f'{folder}\\{pngLowTroposphere}', mode='r')
         jpg.save(f'{folder}\\{jpgLowTroposphere}')
         print(f'\n{folder}\\{jpgLowTroposphere} saved.')
   if pngMidTroposphere in images:
         jpg = Image.open(f'{folder}\\{pngMidTroposphere}', mode='r')
         jpg.save(f'{folder}//{jpgMidTroposphere}')
         print(f'\n{folder}\\{jpgMidTroposphere} saved.')
   if pngHighTroposphere in images:
         jpg = Image.open(f'{folder}\\{pngHighTroposphere}', mode='r')
         jpg.save(f'{folder}\\{jpgHighTroposphere}')
         print(f'\n{folder}\\{jpgHighTroposphere} saved.')
   if pngTopTroposphere in images:
         jpg = Image.open(f'{folder}\\{pngTopTroposphere}', mode='r')
         jpg.save(f'{folder}\\{jpgTopTroposphere}')
         print(f'\n{folder}\\{jpgTopTroposphere} saved.')
   if pngLowStratopshere in images:
         jpg = Image.open(f'{folder}\\{pngLowStratopshere}', mode='r')
         jpg.save(f'{folder}\\{jpgLowstratosphere}')
         print(f'\n{folder}\\{jpgLowstratosphere} saved.')
   if pngMidStratosphere in images:
         jpg = Image.open(f'{folder}\\{pngMidStratosphere}', mode='r')
         jpg.save(f'{folder}\\{jpgMidStratosphere}')
         print(f'\n{folder}\\{jpgMidStratosphere} saved.')


    
   
   
   
#Make life easier by putting this all in strings to use later
pngN2OSounding = 'hirs_rgb_Clouds_Only_(N2O_Sounding).png'
pngMidTroposphere = 'hirs_rgb_Mid_Troposphere_CO2_H2O_Temperature.png'
pngLowTroposphere = 'hirs_rgb_Low_Troposphere_CO2_H2O_Temperature.png'
pngCloudDetection = 'hirs_rgb_Cloud_Detection_Channel.png'
pngCloudsOnly = 'hirs_rgb_Clouds_Only_(N2O_Sounding).png'
pngHighTroposphere = 'hirs_rgb_High_Troposphere_CO2_Temperature.png'
pngTopTroposphere = 'hirs_rgb_Top_Troposphere_CO2_Temperature.png'
pngLowStratopshere = 'hirs_rgb_Low_Stratosphere_CO2_Temperature.png'
pngMidStratosphere = 'hirs_rgb_Mid_Stratosphere_CO2_Temperature.png'

jpgN2OSounding = 'hirs_rgb_Clouds_Only_(N2O_Sounding).jpg'
jpgCloudDetection = 'hirs_rgb_Cloud_Detection_Channel.jpg'
jpgLowTroposphere = 'hirs_rgb_Low_Troposphere_CO2_H2O_Temperature.jpg'
jpgMidTroposphere = 'hirs_rgb_Mid_Troposphere_CO2_H2O_Temperature.jpg'
jpgHighTroposphere = 'hirs_rgb_High_Troposphere_CO2_Temperature.jpg'
jpgTopTroposphere = 'hirs_rgb_Top_Troposphere_CO2_Temperature.jpg'
jpgLowstratosphere = 'hirs_rgb_Low_Stratosphere_CO2_Temperature.jpg'
jpgMidStratosphere = 'hirs_rgb_Mid_Stratosphere_CO2_Temperature.jpg'




#GUI = input("Would you like to use the GUI? Y/N: ").lower()
folder = input("\n\nInput the folder containing all the HIRS imagery here:  ") #let user input file location for images


makejpg()

make_gif()