## Code to visualize/animate lattice gas simulations

import numpy as np
from Tkinter import *

## note to self: maybe rewrite code in Python to prevent saving lots of files? 

## note to self: cool way to visualize could be taking slices in xz plane and
## then have slices arranged in y plane...

## import data from C++ code configurations

## LATER: define a function for this...for when have >1 image

conf = np.genfromtxt('configT4_mu-2_N100_J05_E2_nsw100000.out')
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

conf = np.genfromtxt('configT4_mu-1_N100_J05_E2_nsw100000.out')
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

conf = np.genfromtxt('configT4_mu-05_N100_J05_E2_nsw100000.out')
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

conf = np.genfromtxt('configT4_mu-1d5_N100_J05_E2_nsw100000.out')
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

conf = np.genfromtxt('configT10_mu-3d4_N100_J3_E5_nsw100000.out')
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

conf = np.genfromtxt('configT10_mu-1d7_N100_J3_E5_nsw100000.out')
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

conf = np.genfromtxt('configT10_mu-0d85_N100_J3_E5_nsw100000.out')
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

conf = np.genfromtxt('configT10_mu-2d55_N100_J3_E5_nsw100000.out')
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

conf = np.genfromtxt('configT2_mu-2_N100_J05_E2_nsw100000.out')
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

conf = np.genfromtxt('configT2_mu-1_N100_J05_E2_nsw100000.out')
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

conf = np.genfromtxt('configT2_mu-4_N100_J05_E2_nsw100000.out')
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

conf = np.genfromtxt('configT05_mu-8_N100_J05_E2_nsw100000.out')
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

conf = np.genfromtxt('configT05_mu-4_N100_J05_E2_nsw100000.out')
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

conf = np.genfromtxt('configT05_mu-12_N100_J05_E2_nsw100000.out')
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

conf = np.genfromtxt('configT2_mu-8d5_N100_J3_E5_nsw100000.out')
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

conf = np.genfromtxt('configT2_mu-17_N100_J3_E5_nsw100000.out')
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

conf = np.genfromtxt('configT2_mu-4d25_N100_J3_E5_nsw100000.out')
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

conf = np.genfromtxt('configT2_mu-12d75_N100_J3_E5_nsw100000.out')
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

conf = np.genfromtxt('configT1_mu-34_N100_J3_E5_nsw100000.out')
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

conf = np.genfromtxt('configT1_mu-17_N100_J3_E5_nsw100000.out')
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

conf = np.genfromtxt('configT1_mu-8d5_N100_J3_E5_nsw100000.out')
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

conf = np.genfromtxt('configT1_mu-25d5_N100_J3_E5_nsw100000.out')
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

