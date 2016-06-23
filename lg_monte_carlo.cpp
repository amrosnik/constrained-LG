#include <iostream>
#include <fstream> // file I/O
#include <vector>
#include <math.h>
#include "MersenneTwister.h"
#include <string>
using namespace std;

#include "lg_class.h"

// How to run 3D lattice gas
// Enables J_i in all three directions to allow for anisotropy


int main() {
    // files for printing
    //FILE *spincorr;

    // initialize configuration
    int i,j,k,N;
    int nsweeps;
    double T,mu,Jx,Jy,Jz;
    string name;
    vector<double> corres; 
    double mag,m_stag;
   
    T = 15.82;
    mu = 0;
    N = 100; // sites per side
    nsweeps = 100000;
    Jx = 5.0;
    Jy = Jx;
    Jz = 5.0;
    name = "configT15-82_mu0_N100_J5_E5_nsw100000";
    //spincorr = fopen(("Corrs_3dLG_"+name+".out").c_str(),"w");
    Config config1 (N, T, mu, Jx, Jy, Jz); //N, temp, mu, Jx, Jy, Jz
    config1.init_lattice();

    // Monte Carlo simulation  
    config1.monte_carlo(nsweeps);
   
    // print final configuration
    config1.print_config(name);
   
    // calculate spatial correlations 
    mag = config1.calc_mag();
    m_stag = config1.calc_avg_stagmag();
    corres = config1.space_corr(mag);
    cout << "T: " << T << " mu: " << mu <<" J: " << Jx << " Jz: " << Jz << " Chi: " << config1.Chi << "\n";
    cout << " m_stag: " << m_stag << endl;
    // write out spin-spin correlation function 
    //for (int d=0; d<round(0.25*N); d++) {
    //   fprintf(spincorr,"%d %f\n",d,corres[d]);
    //}

    T = 15.84;
    mu = 0;
    N = 100; // sites per side
    nsweeps = 100000;
    Jx = 5.0;
    Jy = Jx;
    Jz = 5.0;
    name = "configT15-84_mu0_N100_J5_E5_nsw100000";
    //spincorr = fopen(("Corrs_3dLG_"+name+".out").c_str(),"w");
    Config config2 (N, T, mu, Jx, Jy, Jz); //N, temp, mu, Jx, Jy, Jz
    config2.init_lattice();

    // Monte Carlo simulation  
    config2.monte_carlo(nsweeps);
   
    // print final configuration
    config2.print_config(name);
   
    // calculate spatial correlations 
    mag = config2.calc_mag();
    m_stag = config2.calc_avg_stagmag();
    corres = config2.space_corr(mag);
    cout << "T: " << T << " mu: " << mu <<" J: " << Jx << " Jz: " << Jz << " Chi: " << config2.Chi << "\n";
    cout << " m_stag: " << m_stag << endl;
    // write out spin-spin correlation function 
    //for (int d=0; d<round(0.25*N); d++) {
    //   fprintf(spincorr,"%d %f\n",d,corres[d]);
    //}

    T = 15.86;
    mu = 0;
    N = 100; // sites per side
    nsweeps = 100000;
    Jx = 5.0;
    Jy = Jx;
    Jz = 5.0;
    name = "configT15-86_mu0_N100_J5_E5_nsw100000";
    //spincorr = fopen(("Corrs_3dLG_"+name+".out").c_str(),"w");
    Config config3 (N, T, mu, Jx, Jy, Jz); //N, temp, mu, Jx, Jy, Jz
    config3.init_lattice();

    // Monte Carlo simulation  
    config3.monte_carlo(nsweeps);
   
    // print final configuration
    config3.print_config(name);
   
    // calculate spatial correlations 
    mag = config3.calc_mag();
    m_stag = config3.calc_avg_stagmag();
    corres = config3.space_corr(mag);
    cout << "T: " << T << " mu: " << mu <<" J: " << Jx << " Jz: " << Jz << " Chi: " << config3.Chi << "\n";
    cout << " m_stag: " << m_stag << endl;
    // write out spin-spin correlation function 
    //for (int d=0; d<round(0.25*N); d++) {
    //   fprintf(spincorr,"%d %f\n",d,corres[d]);
    //}

    T = 15.88;
    mu = 0;
    N = 100; // sites per side
    nsweeps = 100000;
    Jx = 5.0;
    Jy = Jx;
    Jz = 5.0;
    name = "configT15-88_mu0_N100_J5_E5_nsw100000";
    //spincorr = fopen(("Corrs_3dLG_"+name+".out").c_str(),"w");
    Config config4 (N, T, mu, Jx, Jy, Jz); //N, temp, mu, Jx, Jy, Jz
    config4.init_lattice();

    // Monte Carlo simulation  
    config4.monte_carlo(nsweeps);
   
    // print final configuration
    config4.print_config(name);
   
    // calculate spatial correlations 
    mag = config4.calc_mag();
    m_stag = config4.calc_avg_stagmag();
    corres = config4.space_corr(mag);
    cout << "T: " << T << " mu: " << mu <<" J: " << Jx << " Jz: " << Jz << " Chi: " << config4.Chi << "\n";
    cout << " m_stag: " << m_stag << endl;
    // write out spin-spin correlation function 
    //for (int d=0; d<round(0.25*N); d++) {
    //   fprintf(spincorr,"%d %f\n",d,corres[d]);
    //}

/*
    T = 9.5;
    mu = 0;
    N = 100; // sites per side
    nsweeps = 100000;
    Jx = 5.0;
    Jy = Jx;
    Jz = 5.0;
    name = "configT9-5_mu0_N100_J5_E5_nsw100000";
    //spincorr = fopen(("Corrs_3dLG_"+name+".out").c_str(),"w");
    Config config5 (N, T, mu, Jx, Jy, Jz); //N, temp, mu, Jx, Jy, Jz
    config5.init_lattice();

    // Monte Carlo simulation  
    config5.monte_carlo(nsweeps);
   
    // print final configuration
    config5.print_config(name);
   
    // calculate spatial correlations 
    mag = config5.calc_mag();
    m_stag = config5.calc_avg_stagmag();
    corres = config5.space_corr(mag);
    cout << "T: " << T << " mu: " << mu <<" J: " << Jx << " Jz: " << Jz << " Chi: " << config5.Chi << "\n";
    cout << " m_stag: " << m_stag << endl;
    // write out spin-spin correlation function 
    //for (int d=0; d<round(0.25*N); d++) {
    //   fprintf(spincorr,"%d %f\n",d,corres[d]);
    //}

    T = 25;
    mu = 0;
    N = 100; // sites per side
    nsweeps = 100000;
    Jx = 5.0;
    Jy = Jx;
    Jz = 5.0;
    name = "configT25_mu0_N100_J5_E5_nsw100000";
    //spincorr = fopen(("Corrs_3dLG_"+name+".out").c_str(),"w");
    Config config6 (N, T, mu, Jx, Jy, Jz); //N, temp, mu, Jx, Jy, Jz
    config6.init_lattice();

    // Monte Carlo simulation  
    config6.monte_carlo(nsweeps);
   
    // print final configuration
    config6.print_config(name);
   
    // calculate spatial correlations 
    mag = config6.calc_mag();
    m_stag = config6.calc_avg_stagmag();
    corres = config6.space_corr(mag);
    cout << "T: " << T << " mu: " << mu <<" J: " << Jx << " Jz: " << Jz << " Chi: " << config6.Chi << "\n";
    cout << " m_stag: " << m_stag << endl;
    // write out spin-spin correlation function 
    //for (int d=0; d<round(0.25*N); d++) {
    //   fprintf(spincorr,"%d %f\n",d,corres[d]);
    //}


    T = 1000;
    mu = 0;
    N = 100; // sites per side
    nsweeps = 100000;
    Jx = 5.0;
    Jy = Jx;
    Jz = 5.0;
    name = "configT1000_mu0_N100_J5_E5_nsw100000";
    //spincorr = fopen(("Corrs_3dLG_"+name+".out").c_str(),"w");
    Config config7 (N, T, mu, Jx, Jy, Jz); //N, temp, mu, Jx, Jy, Jz
    config7.init_lattice();

    // Monte Carlo simulation  
    config7.monte_carlo(nsweeps);
   
    // print final configuration
    config7.print_config(name);
   
    // calculate spatial correlations 
    mag = config7.calc_mag();
    m_stag = config7.calc_avg_stagmag();
    corres = config7.space_corr(mag);
    cout << "T: " << T << " mu: " << mu <<" J: " << Jx << " Jz: " << Jz << " Chi: " << config7.Chi << "\n";
    cout << " m_stag: " << m_stag << endl;
    // write out spin-spin correlation function 
    //for (int d=0; d<round(0.25*N); d++) {
    //   fprintf(spincorr,"%d %f\n",d,corres[d]);
    //}
*/
}      
