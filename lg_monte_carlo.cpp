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
    string name,intd_name;
    vector<double> corres; 
    double mag,m_stag;
   
/*
    T = 1.0;
    mu = 0.0;
    N = 10; // sites per side
    nsweeps = 1000000;
    Jx = 0.5;
    Jy = Jx;
    Jz = 6;
    name = "configT"+to_string(T)+"_mu"+to_string(mu)+"_N"+to_string(N)+"_J"+to_string(Jx)+"_E"+to_string(Jz)+"_"+to_string(nsweeps);
    intd_name = "configT"+to_string(T)+"_mu"+to_string(mu)+"_N"+to_string(N)+"_J"+to_string(Jx)+"_E"+to_string(Jz);
    //spincorr = fopen(("Corrs_3dLG_"+name+".out").c_str(),"w");
    Config config1 (N, T, mu, Jx, Jy, Jz); //N, temp, mu, Jx, Jy, Jz
    config1.init_lattice();

    // Monte Carlo simulation  
    config1.monte_carlo(nsweeps,intd_name);
   
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
*/

    T = 0.5;
    mu = -0.223;
    N = 10; // sites per side
    nsweeps = 1000000;
    Jx = 0.5;
    Jy = Jx;
    Jz = 1.0;
    name = "configT"+to_string(T)+"_mu"+to_string(mu)+"_N"+to_string(N)+"_J"+to_string(Jx)+"_E"+to_string(Jz)+"_"+to_string(nsweeps);
    intd_name = "configT"+to_string(T)+"_mu"+to_string(mu)+"_N"+to_string(N)+"_J"+to_string(Jx)+"_E"+to_string(Jz);
    //spincorr = fopen(("Corrs_3dLG_"+name+".out").c_str(),"w");
    Config config2 (N, T, mu, Jx, Jy, Jz); //N, temp, mu, Jx, Jy, Jz
    config2.init_lattice();

    // Monte Carlo simulation  
    config2.monte_carlo(nsweeps,intd_name);
   
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


    T = 0.5;
    mu = -0.288;
    N = 10; // sites per side
    nsweeps = 1000000;
    Jx = 0.5;
    Jy = Jx;
    Jz = 1.0;
    name = "configT"+to_string(T)+"_mu"+to_string(mu)+"_N"+to_string(N)+"_J"+to_string(Jx)+"_E"+to_string(Jz)+"_"+to_string(nsweeps);
    intd_name = "configT"+to_string(T)+"_mu"+to_string(mu)+"_N"+to_string(N)+"_J"+to_string(Jx)+"_E"+to_string(Jz);
    //spincorr = fopen(("Corrs_3dLG_"+name+".out").c_str(),"w");
    Config config3 (N, T, mu, Jx, Jy, Jz); //N, temp, mu, Jx, Jy, Jz
    config3.init_lattice();

    // Monte Carlo simulation  
    config3.monte_carlo(nsweeps,intd_name);
   
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

    T = 0.5;
    mu = -0.357;
    N = 10; // sites per side
    nsweeps = 1000000;
    Jx = 0.5;
    Jy = Jx;
    Jz = 1.0;
    name = "configT"+to_string(T)+"_mu"+to_string(mu)+"_N"+to_string(N)+"_J"+to_string(Jx)+"_E"+to_string(Jz)+"_"+to_string(nsweeps);
    intd_name = "configT"+to_string(T)+"_mu"+to_string(mu)+"_N"+to_string(N)+"_J"+to_string(Jx)+"_E"+to_string(Jz);
    //spincorr = fopen(("Corrs_3dLG_"+name+".out").c_str(),"w");
    Config config4 (N, T, mu, Jx, Jy, Jz); //N, temp, mu, Jx, Jy, Jz
    config4.init_lattice();

    // Monte Carlo simulation  
    config4.monte_carlo(nsweeps,intd_name);
   
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

    T = 0.5;
    mu = -0.5;
    N = 10; // sites per side
    nsweeps = 1000000;
    Jx = 0.25;
    Jy = Jx;
    Jz = 0.5;
    name = "configT"+to_string(T)+"_mu"+to_string(mu)+"_N"+to_string(N)+"_J"+to_string(Jx)+"_E"+to_string(Jz)+"_"+to_string(nsweeps);
    intd_name = "configT"+to_string(T)+"_mu"+to_string(mu)+"_N"+to_string(N)+"_J"+to_string(Jx)+"_E"+to_string(Jz);
    //spincorr = fopen(("Corrs_3dLG_"+name+".out").c_str(),"w");
    Config config5 (N, T, mu, Jx, Jy, Jz); //N, temp, mu, Jx, Jy, Jz
    config5.init_lattice();

    // Monte Carlo simulation  
    config5.monte_carlo(nsweeps,intd_name);
   
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

    T = 0.5;
    mu = -0.75;
    N = 10; // sites per side
    nsweeps = 1000000;
    Jx = 0.25;
    Jy = Jx;
    Jz = 0.5;
    name = "configT"+to_string(T)+"_mu"+to_string(mu)+"_N"+to_string(N)+"_J"+to_string(Jx)+"_E"+to_string(Jz)+"_"+to_string(nsweeps);
    intd_name = "configT"+to_string(T)+"_mu"+to_string(mu)+"_N"+to_string(N)+"_J"+to_string(Jx)+"_E"+to_string(Jz);
    //spincorr = fopen(("Corrs_3dLG_"+name+".out").c_str(),"w");
    Config config6 (N, T, mu, Jx, Jy, Jz); //N, temp, mu, Jx, Jy, Jz
    config6.init_lattice();

    // Monte Carlo simulation  
    config6.monte_carlo(nsweeps,intd_name);
   
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


    T = 0.5;
    mu = 0.0;
    N = 10; // sites per side
    nsweeps = 1000000;
    Jx = 0.25;
    Jy = Jx;
    Jz = 0.5;
    name = "configT"+to_string(T)+"_mu"+to_string(mu)+"_N"+to_string(N)+"_J"+to_string(Jx)+"_E"+to_string(Jz)+"_"+to_string(nsweeps);
    intd_name = "configT"+to_string(T)+"_mu"+to_string(mu)+"_N"+to_string(N)+"_J"+to_string(Jx)+"_E"+to_string(Jz);
    //spincorr = fopen(("Corrs_3dLG_"+name+".out").c_str(),"w");
    Config config7 (N, T, mu, Jx, Jy, Jz); //N, temp, mu, Jx, Jy, Jz
    config7.init_lattice();

    // Monte Carlo simulation  
    config7.monte_carlo(nsweeps,intd_name);
   
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

    T = 0.5;
    mu = -0.5;
    N = 10; // sites per side
    nsweeps = 1000000;
    Jx = 0.5;
    Jy = Jx;
    Jz = 1.0;
    name = "configT"+to_string(T)+"_mu"+to_string(mu)+"_N"+to_string(N)+"_J"+to_string(Jx)+"_E"+to_string(Jz)+"_"+to_string(nsweeps);
    intd_name = "configT"+to_string(T)+"_mu"+to_string(mu)+"_N"+to_string(N)+"_J"+to_string(Jx)+"_E"+to_string(Jz);
    //spincorr = fopen(("Corrs_3dLG_"+name+".out").c_str(),"w");
    Config config8 (N, T, mu, Jx, Jy, Jz); //N, temp, mu, Jx, Jy, Jz
    config8.init_lattice();

    // Monte Carlo simulation  
    config8.monte_carlo(nsweeps,intd_name);
   
    // print final configuration
    config8.print_config(name);
   
    // calculate spatial correlations 
    mag = config8.calc_mag();
    m_stag = config8.calc_avg_stagmag();
    corres = config8.space_corr(mag);
    cout << "T: " << T << " mu: " << mu <<" J: " << Jx << " Jz: " << Jz << " Chi: " << config8.Chi << "\n";
    cout << " m_stag: " << m_stag << endl;
    // write out spin-spin correlation function 
    //for (int d=0; d<round(0.25*N); d++) {
    //   fprintf(spincorr,"%d %f\n",d,corres[d]);
    //}

    T = 0.5;
    mu = 0.75;
    N = 10; // sites per side
    nsweeps = 1000000;
    Jx = 0.5;
    Jy = Jx;
    Jz = 1.0;
    name = "configT"+to_string(T)+"_mu"+to_string(mu)+"_N"+to_string(N)+"_J"+to_string(Jx)+"_E"+to_string(Jz)+"_"+to_string(nsweeps);
    intd_name = "configT"+to_string(T)+"_mu"+to_string(mu)+"_N"+to_string(N)+"_J"+to_string(Jx)+"_E"+to_string(Jz);
    //spincorr = fopen(("Corrs_3dLG_"+name+".out").c_str(),"w");
    Config config9 (N, T, mu, Jx, Jy, Jz); //N, temp, mu, Jx, Jy, Jz
    config9.init_lattice();

    // Monte Carlo simulation  
    config9.monte_carlo(nsweeps,intd_name);
   
    // print final configuration
    config9.print_config(name);
   
    // calculate spatial correlations 
    mag = config9.calc_mag();
    m_stag = config9.calc_avg_stagmag();
    corres = config9.space_corr(mag);
    cout << "T: " << T << " mu: " << mu <<" J: " << Jx << " Jz: " << Jz << " Chi: " << config9.Chi << "\n";
    cout << " m_stag: " << m_stag << endl;
    // write out spin-spin correlation function 
    //for (int d=0; d<round(0.25*N); d++) {
    //   fprintf(spincorr,"%d %f\n",d,corres[d]);
    //}


    T = 0.5;
    mu = 0.5;
    N = 10; // sites per side
    nsweeps = 1000000;
    Jx = 0.5;
    Jy = Jx;
    Jz = 1.0;
    name = "configT"+to_string(T)+"_mu"+to_string(mu)+"_N"+to_string(N)+"_J"+to_string(Jx)+"_E"+to_string(Jz)+"_"+to_string(nsweeps);
    intd_name = "configT"+to_string(T)+"_mu"+to_string(mu)+"_N"+to_string(N)+"_J"+to_string(Jx)+"_E"+to_string(Jz);
    //spincorr = fopen(("Corrs_3dLG_"+name+".out").c_str(),"w");
    Config config10 (N, T, mu, Jx, Jy, Jz); //N, temp, mu, Jx, Jy, Jz
    config10.init_lattice();

    // Monte Carlo simulation  
    config10.monte_carlo(nsweeps,intd_name);
   
    // print final configuration
    config10.print_config(name);
   
    // calculate spatial correlations 
    mag = config10.calc_mag();
    m_stag = config10.calc_avg_stagmag();
    corres = config10.space_corr(mag);
    cout << "T: " << T << " mu: " << mu <<" J: " << Jx << " Jz: " << Jz << " Chi: " << config10.Chi << "\n";
    cout << " m_stag: " << m_stag << endl;
    // write out spin-spin correlation function 
    //for (int d=0; d<round(0.25*N); d++) {
    //   fprintf(spincorr,"%d %f\n",d,corres[d]);
    //}

    T = 0.5;
    mu = 0.75;
    N = 10; // sites per side
    nsweeps = 1000000;
    Jx = 0.25;
    Jy = Jx;
    Jz = 0.5;
    name = "configT"+to_string(T)+"_mu"+to_string(mu)+"_N"+to_string(N)+"_J"+to_string(Jx)+"_E"+to_string(Jz)+"_"+to_string(nsweeps);
    intd_name = "configT"+to_string(T)+"_mu"+to_string(mu)+"_N"+to_string(N)+"_J"+to_string(Jx)+"_E"+to_string(Jz);
    //spincorr = fopen(("Corrs_3dLG_"+name+".out").c_str(),"w");
    Config config11 (N, T, mu, Jx, Jy, Jz); //N, temp, mu, Jx, Jy, Jz
    config11.init_lattice();

    // Monte Carlo simulation  
    config11.monte_carlo(nsweeps,intd_name);
   
    // print final configuration
    config11.print_config(name);
   
    // calculate spatial correlations 
    mag = config11.calc_mag();
    m_stag = config11.calc_avg_stagmag();
    corres = config11.space_corr(mag);
    cout << "T: " << T << " mu: " << mu <<" J: " << Jx << " Jz: " << Jz << " Chi: " << config11.Chi << "\n";
    cout << " m_stag: " << m_stag << endl;
    // write out spin-spin correlation function 
    //for (int d=0; d<round(0.25*N); d++) {
    //   fprintf(spincorr,"%d %f\n",d,corres[d]);
    //}

    T = 0.5;
    mu = 0.5;
    N = 10; // sites per side
    nsweeps = 1000000;
    Jx = 0.25;
    Jy = Jx;
    Jz = 0.5;
    name = "configT"+to_string(T)+"_mu"+to_string(mu)+"_N"+to_string(N)+"_J"+to_string(Jx)+"_E"+to_string(Jz)+"_"+to_string(nsweeps);
    intd_name = "configT"+to_string(T)+"_mu"+to_string(mu)+"_N"+to_string(N)+"_J"+to_string(Jx)+"_E"+to_string(Jz);
    //spincorr = fopen(("Corrs_3dLG_"+name+".out").c_str(),"w");
    Config config12 (N, T, mu, Jx, Jy, Jz); //N, temp, mu, Jx, Jy, Jz
    config12.init_lattice();

    // Monte Carlo simulation  
    config12.monte_carlo(nsweeps,intd_name);
   
    // print final configuration
    config12.print_config(name);
   
    // calculate spatial correlations 
    mag = config12.calc_mag();
    m_stag = config12.calc_avg_stagmag();
    corres = config12.space_corr(mag);
    cout << "T: " << T << " mu: " << mu <<" J: " << Jx << " Jz: " << Jz << " Chi: " << config12.Chi << "\n";
    cout << " m_stag: " << m_stag << endl;
    // write out spin-spin correlation function 
    //for (int d=0; d<round(0.25*N); d++) {
    //   fprintf(spincorr,"%d %f\n",d,corres[d]);
    //}

}      
