## Code to visualize/animate lattice gas simulations

from PIL import Image
from images2gif import writeGif
import glob
import numpy as np
import sys
import os.path

# input arguments: config_base_file_name
name = sys.argv[1]
 
## import data from C++ code configurations
file_counter = len(glob.glob(name+'*out'))
count = file_counter - 1
count_files = 0
im_array = []
for i in range(0,count):
   nsw = i*10000 + 150000 
   file_name = name+str(nsw)+'.out'
   if os.path.exists(file_name):
      conf = np.genfromtxt(name+str(nsw)+'.out')
### # get system size from length of of row or column:
      N = len(conf[0])
### # format should be a matrix where row = x-coordinate and column = z-coordinate, where y-coordinate = 0 unless otherwise specified
      img = Image.new('RGB',(N,N),"white")
      pixels = img.load()
 
      for i in range(N):
         for k in range(N):
            if conf[i][k] == 0:
               pixels[i,k] = (255,255,1)
            elif conf[i][k] == 1:
               pixels[i,k] = (255,1,255)
            else:
               print "ERROR"
      img = img.resize((1000,1000))
      im_array.append(img)
      #img.close()

#images = [Image.open(image) for image in glob.glob(name+'*.png')]
gif_name = 'gif-'+name+'.gif'
writeGif(gif_name,im_array,duration=0.1)
#IPdisplay.Image(url=gif_name)   

"""
conf = np.genfromtxt('configT4_mu-1_N100_J05_E2_nsw100000.out')
conf = np.genfromtxt('configT4_mu-05_N100_J05_E2_nsw100000.out')
conf = np.genfromtxt('configT4_mu-1d5_N100_J05_E2_nsw100000.out')

conf = np.genfromtxt('configT10_mu-3d4_N100_J3_E5_nsw100000.out')
conf = np.genfromtxt('configT10_mu-1d7_N100_J3_E5_nsw100000.out')
conf = np.genfromtxt('configT10_mu-0d85_N100_J3_E5_nsw100000.out')
conf = np.genfromtxt('configT10_mu-2d55_N100_J3_E5_nsw100000.out')
conf = np.genfromtxt('configT2_mu-2_N100_J05_E2_nsw100000.out')
conf = np.genfromtxt('configT2_mu-1_N100_J05_E2_nsw100000.out')
conf = np.genfromtxt('configT2_mu-4_N100_J05_E2_nsw100000.out')
conf = np.genfromtxt('configT2_mu-3_N100_J05_E2_nsw100000.out')
## get system size from length of of row or column:
N = len(conf[0])
## format should be a matrix where row = x-coordinate and column = z-coordinate, where y-coordinate = 0 unless otherwise specified

master = Tk()
canvas_width = 1200
canvas_height = 1200
canvas = Canvas(master,width=canvas_width,height=canvas_height)
canvas.pack()
image = PhotoImage(width=canvas_width,height=canvas_height)
canvas.create_image((3,3),image=image,anchor="nw",state="normal")

spin_width = canvas_width/N
for i in range(N):
  for k in range(N):
     if conf[i][k] == 0:
       image.put("#A1E3B2",to=(i*spin_width,k*spin_width,
                   (i+1)*spin_width,(k+1)*spin_width))
     else:
       image.put("#2A76B5",to=(i*spin_width,k*spin_width,
                    (i+1)*spin_width,(k+1)*spin_width))
master.update_idletasks()
mainloop()

conf = np.genfromtxt('configT1_mu-4_N100_J05_E2_nsw100000.out')
#conf = np.genfromtxt('testT2-N100-sw100000.out')
## get system size from length of of row or column:
N = len(conf[0])
## format should be a matrix where row = x-coordinate and column = z-coordinate, where y-coordinate = 0 unless otherwise specified

master = Tk()
canvas_width = 1200
canvas_height = 1200
canvas = Canvas(master,width=canvas_width,height=canvas_height)
canvas.pack()
image = PhotoImage(width=canvas_width,height=canvas_height)
canvas.create_image((3,3),image=image,anchor="nw",state="normal")

spin_width = canvas_width/N
for i in range(N):
  for k in range(N):
     if conf[i][k] == 0:
       image.put("#A1E3B2",to=(i*spin_width,k*spin_width,
                   (i+1)*spin_width,(k+1)*spin_width))
     else:
       image.put("#2A76B5",to=(i*spin_width,k*spin_width,
                    (i+1)*spin_width,(k+1)*spin_width))
master.update_idletasks()
mainloop()

conf = np.genfromtxt('configT1_mu-2_N100_J05_E2_nsw100000.out')
## get system size from length of of row or column:
N = len(conf[0])
## format should be a matrix where row = x-coordinate and column = z-coordinate, where y-coordinate = 0 unless otherwise specified

master = Tk()
canvas_width = 1200
canvas_height = 1200
canvas = Canvas(master,width=canvas_width,height=canvas_height)
canvas.pack()
image = PhotoImage(width=canvas_width,height=canvas_height)
canvas.create_image((3,3),image=image,anchor="nw",state="normal")

spin_width = canvas_width/N
for i in range(N):
  for k in range(N):
     if conf[i][k] == 0:
       image.put("#A1E3B2",to=(i*spin_width,k*spin_width,
                   (i+1)*spin_width,(k+1)*spin_width))
     else:
       image.put("#2A76B5",to=(i*spin_width,k*spin_width,
                    (i+1)*spin_width,(k+1)*spin_width))
master.update_idletasks()
mainloop()

conf = np.genfromtxt('configT1_mu-1_N100_J05_E2_nsw100000.out')
## get system size from length of of row or column:
N = len(conf[0])
## format should be a matrix where row = x-coordinate and column = z-coordinate, where y-coordinate = 0 unless otherwise specified

master = Tk()
canvas_width = 1200
canvas_height = 1200
canvas = Canvas(master,width=canvas_width,height=canvas_height)
canvas.pack()
image = PhotoImage(width=canvas_width,height=canvas_height)
canvas.create_image((3,3),image=image,anchor="nw",state="normal")

spin_width = canvas_width/N
for i in range(N):
  for k in range(N):
     if conf[i][k] == 0:
       image.put("#A1E3B2",to=(i*spin_width,k*spin_width,
                   (i+1)*spin_width,(k+1)*spin_width))
     else:
       image.put("#2A76B5",to=(i*spin_width,k*spin_width,
                    (i+1)*spin_width,(k+1)*spin_width))
master.update_idletasks()
mainloop()

conf = np.genfromtxt('configT1_mu-3_N100_J05_E2_nsw100000.out')
## get system size from length of of row or column:
N = len(conf[0])
## format should be a matrix where row = x-coordinate and column = z-coordinate, where y-coordinate = 0 unless otherwise specified

master = Tk()
canvas_width = 1200
canvas_height = 1200
canvas = Canvas(master,width=canvas_width,height=canvas_height)
canvas.pack()
image = PhotoImage(width=canvas_width,height=canvas_height)
canvas.create_image((3,3),image=image,anchor="nw",state="normal")

spin_width = canvas_width/N
for i in range(N):
  for k in range(N):
     if conf[i][k] == 0:
       image.put("#A1E3B2",to=(i*spin_width,k*spin_width,
                   (i+1)*spin_width,(k+1)*spin_width))
     else:
       image.put("#2A76B5",to=(i*spin_width,k*spin_width,
                    (i+1)*spin_width,(k+1)*spin_width))
master.update_idletasks()
mainloop()

conf = np.genfromtxt('configT4_mu-8d5_N100_J3_E5_nsw100000.out')
## get system size from length of of row or column:
N = len(conf[0])
## format should be a matrix where row = x-coordinate and column = z-coordinate, where y-coordinate = 0 unless otherwise specified

master = Tk()
canvas_width = 1200
canvas_height = 1200
canvas = Canvas(master,width=canvas_width,height=canvas_height)
canvas.pack()
image = PhotoImage(width=canvas_width,height=canvas_height)
canvas.create_image((3,3),image=image,anchor="nw",state="normal")

spin_width = canvas_width/N
for i in range(N):
  for k in range(N):
     if conf[i][k] == 0:
       image.put("#A1E3B2",to=(i*spin_width,k*spin_width,
                   (i+1)*spin_width,(k+1)*spin_width))
     else:
       image.put("#2A76B5",to=(i*spin_width,k*spin_width,
                    (i+1)*spin_width,(k+1)*spin_width))
master.update_idletasks()
mainloop()

conf = np.genfromtxt('configT4_mu-4d25_N100_J3_E5_nsw100000.out')
## get system size from length of of row or column:
N = len(conf[0])
## format should be a matrix where row = x-coordinate and column = z-coordinate, where y-coordinate = 0 unless otherwise specified

master = Tk()
canvas_width = 1200
canvas_height = 1200
canvas = Canvas(master,width=canvas_width,height=canvas_height)
canvas.pack()
image = PhotoImage(width=canvas_width,height=canvas_height)
canvas.create_image((3,3),image=image,anchor="nw",state="normal")

spin_width = canvas_width/N
for i in range(N):
  for k in range(N):
     if conf[i][k] == 0:
       image.put("#A1E3B2",to=(i*spin_width,k*spin_width,
                   (i+1)*spin_width,(k+1)*spin_width))
     else:
       image.put("#2A76B5",to=(i*spin_width,k*spin_width,
                    (i+1)*spin_width,(k+1)*spin_width))
master.update_idletasks()
mainloop()

conf = np.genfromtxt('configT4_mu-2d125_N100_J3_E5_nsw100000.out')
## get system size from length of of row or column:
N = len(conf[0])
## format should be a matrix where row = x-coordinate and column = z-coordinate, where y-coordinate = 0 unless otherwise specified

master = Tk()
canvas_width = 1200
canvas_height = 1200
canvas = Canvas(master,width=canvas_width,height=canvas_height)
canvas.pack()
image = PhotoImage(width=canvas_width,height=canvas_height)
canvas.create_image((3,3),image=image,anchor="nw",state="normal")

spin_width = canvas_width/N
for i in range(N):
  for k in range(N):
     if conf[i][k] == 0:
       image.put("#A1E3B2",to=(i*spin_width,k*spin_width,
                   (i+1)*spin_width,(k+1)*spin_width))
     else:
       image.put("#2A76B5",to=(i*spin_width,k*spin_width,
                    (i+1)*spin_width,(k+1)*spin_width))
master.update_idletasks()
mainloop()

conf = np.genfromtxt('configT4_mu-6d375_N100_J3_E5_nsw100000.out')
## get system size from length of of row or column:
N = len(conf[0])
## format should be a matrix where row = x-coordinate and column = z-coordinate, where y-coordinate = 0 unless otherwise specified

master = Tk()
canvas_width = 1200
canvas_height = 1200
canvas = Canvas(master,width=canvas_width,height=canvas_height)
canvas.pack()
image = PhotoImage(width=canvas_width,height=canvas_height)
canvas.create_image((3,3),image=image,anchor="nw",state="normal")

spin_width = canvas_width/N
for i in range(N):
  for k in range(N):
     if conf[i][k] == 0:
       image.put("#A1E3B2",to=(i*spin_width,k*spin_width,
                   (i+1)*spin_width,(k+1)*spin_width))
     else:
       image.put("#2A76B5",to=(i*spin_width,k*spin_width,
                    (i+1)*spin_width,(k+1)*spin_width))
master.update_idletasks()
mainloop()

conf = np.genfromtxt('configT05_mu-16_N100_J05_E2_nsw100000.out')

conf = np.genfromtxt('configT05_mu-8_N100_J05_E2_nsw100000.out')

conf = np.genfromtxt('configT05_mu-4_N100_J05_E2_nsw100000.out')

conf = np.genfromtxt('configT05_mu-12_N100_J05_E2_nsw100000.out')

conf = np.genfromtxt('configT2_mu-8d5_N100_J3_E5_nsw100000.out')

conf = np.genfromtxt('configT2_mu-17_N100_J3_E5_nsw100000.out')

conf = np.genfromtxt('configT2_mu-4d25_N100_J3_E5_nsw100000.out')

conf = np.genfromtxt('configT2_mu-12d75_N100_J3_E5_nsw100000.out')

conf = np.genfromtxt('configT1_mu-34_N100_J3_E5_nsw100000.out')
conf = np.genfromtxt('configT1_mu-17_N100_J3_E5_nsw100000.out')

conf = np.genfromtxt('configT1_mu-8d5_N100_J3_E5_nsw100000.out')

conf = np.genfromtxt('configT1_mu-25d5_N100_J3_E5_nsw100000.out')
"""
