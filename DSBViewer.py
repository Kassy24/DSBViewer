#Script to make the HIRS data decoded from Satdump into a concise GIF to view the layers! - Kassy
from PIL import Image
from tkinter import Tk
from tkinter import Label
from tkinter import Text
from tkinter import Button
import os




def make_gif(folder):
    global images
    print('Making Gif...')
    frames = []
    if jpgCloudDetection in images:
         frame0 = Image.open(f'{folder}\\{jpgCloudDetection}')
         frames.append(frame0)
         print('frame 0 added')
    if jpgN2OSounding in images:
         frame1 = Image.open(f'{folder}\\{jpgN2OSounding}')
         frames.append(frame1)
         print('frame 1 added')
    if jpgLowTroposphere in images:
         frame2 = Image.open(f'{folder}\\{jpgLowTroposphere}')
         frames.append(frame2)
         print('frame 2 added')
    if jpgMidTroposphere in images:
         frame3 = Image.open(f'{folder}\\{jpgMidTroposphere}')
         frames.append(frame3)
         print('frame 3 added')
    if jpgHighTroposphere in images:
         frame4= Image.open(f'{folder}\\{jpgHighTroposphere}')
         frames.append(frame4)
         print('frame 4 added')
    if jpgTopTroposphere in images:
         frame5 = Image.open(f'{folder}\\{jpgTopTroposphere}')
         frames.append(frame5)
         print('frame 5 added')
    if jpgLowstratosphere in images:
         frame6 = Image.open(f'{folder}\\{jpgLowstratosphere}')
         frames.append(frame6)
         print('frame 6 added')
    if jpgMidStratosphere in images:
         frames7 = Image.open(f'{folder}\\{jpgMidStratosphere}')
         frames.append(frames7)
         print('frame 7 added')
           
    frame_one = frames[0]
    frame_one.save(f"{folder}\\Atmosphere_Layers.gif", format="GIF", append_images=frames,
               save_all=True, duration=500, loop=0)
    print(f'Gif saved in {folder}\\Atmosphere_Layers.gif')
    if GUI == 'y':
         label.config(text=(f'Gif saved {folder}\\Atmosphere_Layers.gif'),font=('Arial',6))
         label.place(x=0,y=5)
        
         
    
def makejpg(folder):
   global images
   images = list(os.listdir(folder)) #Get images from Folder
   if GUI == 'y':
        label.config(text=f"Images found")

   
   print(f"\n\nImages: {images}")
   print(f"\nIn folder: {folder}")

   if pngN2OSounding in images: #convert each image from png to jpg to make compatible with gif maker
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
   make_gif(folder)

def getText():
     label.config(text="Making Gif!",font=(10))
     label.place(x=50,y=10)
     t.place(x=700,y=700)
     makebutton.place(x=700,y=700)
     folder = t.get(1.0,"end-1c")
     label.config(text=f"Making Gif from: {folder}",font=(3))
     makejpg(folder)
   
   
   
#Make life easier by putting this all in strings to use later
pngN2OSounding = 'hirs_rgb_Clouds_Only_(N2O_Sounding).png'
pngMidTroposphere = 'hirs_rgb_Mid_Troposphere_CO2_H2O_Temperature.png'
pngLowTroposphere = 'hirs_rgb_Low_Troposphere_CO2_H2O_Temperature.png'
pngCloudDetection = 'hirs_rgb_Cloud_Detection_Channel.png'
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

GUI = input("\nWould you like to use the GUI? Y/N: ").lower()

if GUI == 'n':
     folder = input("\n\nInput the folder containing all the HIRS imagery here:  ") #let user input file location for images
     makejpg(folder)

else:
     window = Tk()
     window.title('DSB Viewer')
     window.geometry('500x500')
     window.resizable=False
     window.config(bg="#303030")
     label = Label(window, text="HIRS File Location")
     label.place(x=100,y=50)

     t = Text(window,width=40,height=1,highlightthickness=1)
     t.place(x=100,y=80)

     makebutton = Button(window,width=10,height=1,text="Make Gif!",command=getText)
     makebutton.place(x=210,y=120)


     window.mainloop()
