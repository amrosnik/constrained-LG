#include <iostream>
#include <fstream> // file I/O
#include <vector>
#include <math.h>
#include "MersenneTwister.h"
#include <string>
using namespace std;


class Config { 
          int N;
          vector< vector<double> > place; // place-holder so can initialize arrays more easily
          double temp; // temperature 
          double mu; // chemical potential 
          double Jx; // coupling constant x direction 
          double Jy; // coupling constant y direction
          double Jz; // coupling constant z direction..."stacking potential"
      public:
          vector< vector< vector<double> > > coords; 
          double Chi; // susceptibility
          Config(int n, double t, double Mu, double jx, double jy, double jz) : N(n), place(N,vector<double>(N)), temp(t), mu(Mu), Jx(jx), Jy(jy), Jz(jz), coords((double)n,place),Chi() {} 
          void init_lattice(); 
          double calc_energy(); 
          double calc_del_energy(int i,int j, int k); 
          vector<double> space_corr(double mag);
          int trial_move(int hi,int hj,int hk,double num_test);
          double calc_mag();
          double calc_mag_layer(int z);
          double calc_staggered_mag(int z1, int z2);
          double calc_avg_stagmag();
          void monte_carlo(int nsweeps);
          void print_config(string name);
 
          private:

};


