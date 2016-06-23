#
# Makefile for 3D anisotropic lattice gas model 
#
# 

CC = g++
####### FLAGS #######
#
# -Wall -- Turn on all warnings
#
#####################
CFLAGS = -Wall 
# List of programs generated here
SRC = lg_class.cpp lg_monte_carlo.cpp 
OBJ = lg_class.o lg_monte_carlo.o 
all: latticegas 

latticegas: $(OBJ)
	$(CC) $(CFLAGS) -o latticegas $(OBJ)

lg_class.o: lg_class.h lg_class.cpp
	$(CC) $(CFLAGS) -o lg_class.o -c lg_class.cpp

lg_monte_carlo.o: lg_class.h lg_monte_carlo.cpp
	$(CC) $(CFLAGS) -o lg_monte_carlo.o -c lg_monte_carlo.cpp

clean:
	rm latticegas
	rm lg_class.o
	rm lg_monte_carlo.o



