#include <iostream>
#include <fstream> // file I/O
#include <vector>
#include <math.h>
#include "MersenneTwister.h"
#include <string>
using namespace std;
#include "lg_class.h"

// 3D lattice gas
// Enables J_i in all three directions to allow for anisotropy
// Constraint applied (see trial_move) so as to study stacking/sterics in thylakoids

void Config::init_lattice() {
     int i,j,k;
     for (i=0; i<N; i++) {
         for (j=0; j<N; j++) {
             for (k=0; k<N; k++) {
                 coords[i][j][k] = 0.0; // initialize all sites as empty
            }
         }
     }
}

double Config::calc_energy() {
     int i,j,k,i0,j0,k0,i1,j1,k1; 
     double E;
     E = 0;
     for (i=0; i<N; i++) { 
         for (j=0; j<N; j++) {
             for (k=0; k<N; k++) {
             i0 = i-1;
             i1 = i+1;
             j0 = j-1;
             j1 = j+1;
             k0 = k-1;
             k1 = k+1;
             if (i == 0) {
                i0 = N-1;
             }
             else if (i == N-1) {
                i1 = 0;
             }
             if (j == 0) {
                j0 = N-1;
             }
             else if (j == N-1) {
                j1 = 0;
             }
             if (k == 0) {
                k0 = N-1;
             }
             else if (k == N-1) {
                k1 = 0;
             }
             // single site energy
             E += -mu*coords[i][j][k];
             // nearest neighbor coupling
             E += -0.5*coords[i][j][k]*(Jx*coords[i0][j][k] + Jx*coords[i1][j][k] + Jy*coords[i][j0][k] + Jy*coords[i][j1][k] + Jz*coords[i][j][k0] + Jz*coords[i][j][k1]);
             }
         }
     }
     return E;
}

double Config::calc_del_energy(int i,int j, int k) {
     // misleading name...calculate just the energy of a given spin (for Metropolis)
     int i0,j0,k0,i1,j1,k1; 
     double dE;
     dE = 0;
     // single site energy
     dE = -mu*coords[i][j][k];
     i0 = i-1;
     i1 = i+1;
     j0 = j-1;
     j1 = j+1;
     k0 = k-1;
     k1 = k+1;
     if (i == 0) {
        i0 = N-1;
     }
     else if (i == N-1) {
        i1 = 0;
     }
     if (j == 0) {
        j0 = N-1;
     }
     else if (j == N-1) {
        j1 = 0;
     }
     if (k == 0) {
        k0 = N-1;
     }
     else if (k == N-1) {
        k1 = 0;
     }
     // nearest neighbor coupling
     dE -= coords[i][j][k]*(Jx*coords[i0][j][k] + Jx*coords[i1][j][k] + Jy*coords[i][j0][k] + Jy*coords[i][j1][k] + Jz*coords[i][j][k0] + Jz*coords[i][j][k1]);
     return dE;
}

vector<double> Config::space_corr(double mag) {
    // calculate spatial correlation function
    int i,j,k,m, max_m;
    int ki, kj, kk;
    max_m = round(0.25*N); // AMR: Adjust this as desired. Here m = number of squares away from target site. So for m=1, dealing with nearest neighbors.
    vector<double> result;
    double sumc;
    int count;  
    result.resize(max_m,0);
    Chi = 0;
    for (m=0; m<max_m; m++) { 
       count = 0;
       for (i=0; i<N; i++) { 
           for (j=0; j<N; j++) {
              for (k=0; k<N; k++) {
                     ki = i + m;
                     kj = j + m;
                     kk = k + m;
                     if (ki >= N) { 
                        ki = abs(N - (i + m));
                     }       
                     if (kj >= N) { 
                        kj = abs(N - (j + m));
                     }       
                     if (kk >= N) { 
                        kk = abs(N - (k + m));
                     }  
                     //cout << "m = " << m << "interested in: " << i << " " << j << " " << k << " with stops at " << ki << " " << kj << " " << kk << endl;     
                     sumc = coords[ki][j][k] + coords[i][kj][k] + coords[i][j][kk];
                     result[m] += (double)sumc*coords[i][j][k]; 
                     count += 3; // add 3 to count because there are 3 terms in sumc??
              }
           }
        }
       result[m] /= (double)count; //AMR FIX NORMALIZATION
       Chi += result[m];
    }  
    // subtract off square of average density/magnetization per site
       //Chi -= mag*mag/(double)(N*N*N*N*N*N);
    
    return result;
}

int Config::trial_move(int hi,int hj,int hk,double num_test) { 
    // trial move for Metropolis Monte Carlo
    // returns 0 or 1 to add to accept counter
    double coords_save,constraint_product,constraint_sum; 
    double dE,E1,E2,whatif;
 
    //apply constraint: n_1^(a) n_1^(a+1) = 0 ==> two sites in adjacent layers (going up) can't be occupied 
    // check that constraint is maintained on chosen site + all nearest neighbors
    constraint_sum = 0;
    if (coords[hi][hj][hk] == 1) { 
               whatif = 0;
    } else {  
       whatif = 1;
    }  
    if (hk % 2 == 0) { // only apply constraint on even-numbered layers (0 is the bottom-most layer)     
       constraint_product = coords[hi][hj][hk+1]*whatif;
    } else {
       constraint_product = coords[hi][hj][hk-1]*whatif;
    }  
    constraint_sum += constraint_product;
    coords_save = coords[hi][hj][hk];
       
    // apply Metropolis criterion
    E1 = 0;
    E2 = 0;
    dE = 0;
    E1 = calc_del_energy(hi,hj,hk);
    //dE = config.calc_del_energy(hi,hj,hk);
    if (coords_save == 1) { 
       coords[hi][hj][hk] = 0;
    } else {  
       coords[hi][hj][hk] = 1;
    }
    E2 = calc_del_energy(hi,hj,hk);
    dE = E2 - E1;
    coords[hi][hj][hk] = coords_save;
    // if (dE <= 0) {
    if ((dE <= 0) && (constraint_sum == 0)) {
       if (coords[hi][hj][hk] == 1) { 
          coords[hi][hj][hk] = 0;
       } else {  
          coords[hi][hj][hk] = 1;
       }
       return 1;
    }
    //else if (dE > 0) {
    else if ((dE > 0) && (constraint_sum == 0)) {
        if (num_test <= exp(-dE/temp)) {
           if (coords[hi][hj][hk] == 1) { 
              coords[hi][hj][hk] = 0;
           } else {  
              coords[hi][hj][hk] = 1;
           }
           return 1;
        }
        else { 
           coords[hi][hj][hk] *= 1;
           return 0;
        }
    }
}

double Config::calc_mag() {
  int i,j,k;
  double mag;
  mag = 0;
  for (i=0; i<N; i++) { 
      for (j=0; j<N; j++) {
          for (k=0; k<N; k++) {
             mag += coords[i][j][k];
          }      
      }      
  }  
  return mag;
}

double Config::calc_mag_layer(int zcoord) {
  int i,j,k;
  double mag_layer_z;
  mag_layer_z = 0;
  if ((zcoord >= N) || (zcoord < 0)) {
     cout << "invalid z-coordinate" << endl;
     mag_layer_z = -1;
  }
  else {
    for (i=0; i<N; i++) { 
      for (j=0; j<N; j++) {
          mag_layer_z += coords[i][j][zcoord];
      }      
    }
  }  
  return mag_layer_z;
}

double Config::calc_staggered_mag(int zcoord1, int zcoord2) {
   double m_layer_1, m_layer_2,m_stag; 
   m_layer_1 = calc_mag_layer(zcoord1);
   m_layer_2 = calc_mag_layer(zcoord2);
   m_stag = 0.5*(m_layer_1 - m_layer_2); 
   
   return m_stag;
}

double Config::calc_mag_odd() { 
  int i,j,k;
  double mag_odd;
  mag_odd = 0;
  for (i=0; i<N; i++) { 
      for (j=0; j<N; j++) {
          for (k=1; k<N; k+=2) { // only increment on odd layers!
             mag_odd += coords[i][j][k];
          }      
      }      
  }  
  return mag_odd;
}

double Config::calc_mag_even() { 
  int i,j,k;
  double mag_even;
  mag_even = 0;
  for (i=0; i<N; i++) { 
      for (j=0; j<N; j++) {
          for (k=0; k<N; k+=2) { // only increment on even layers!
             mag_even += coords[i][j][k];
          }      
      }      
  }  
  return mag_even;
}

double Config::calc_avg_stagmag() {
  int i,count;
  double avg_stagmag,stag;
  avg_stagmag = 0;
  count = 0;
  for (i=0; i<N; i+=2) { // increment on even layers 
      stag = calc_staggered_mag(i,i+1);
      avg_stagmag += stag;
      //cout << "m_s for layers " << i << " " << i+1 << ": " << stag << endl;
      count++;
  }
  avg_stagmag /= (double)count*N*N;  
  return avg_stagmag;
}

void Config::monte_carlo(int nsweeps,string name) { 
    // Monte Carlo simulation  
    int seed;
    seed = 1098796; // change as desired...maybe make this randomly generated?
    MTRand generator(seed);   
    double mag,num_test;
    int hi,hj,hk,avg_count; 
    int accept = 0;
    avg_count = 0;
    double avg_m = 0;
    double avg_m2 = 0;
    double flucts = 0;
    mag = 0; 
    ofstream mag_out; // average occupancy output file
    mag_out.open("avg_mag_tot_"+name+".out",ios::out);
    ofstream mag_odd_out; // average odd layer occupancy output file
    mag_odd_out.open("avg_mag_odd_"+name+".out",ios::out);
    ofstream mag_even_out; // average even layer occupancy output file
    mag_even_out.open("avg_mag_even_"+name+".out",ios::out);

    for (int sweep = 0; sweep < nsweeps; sweep++) {
        for (int step = 0; step < N; step++) {
            hi = generator.randInt(N-1);
            hj = generator.randInt(N-1);
            hk = generator.randInt(N-1);
            num_test = generator.rand();
            accept += trial_move(hi,hj,hk,num_test);
         }
  
         // calculate magnetization/density
         if ((sweep > 150000) && (sweep % 1000 == 0)) {
            mag_out << sweep << "  " << (1/(double)(N*N*N))*calc_mag() << endl;
            mag_odd_out << sweep << "  " << (1/(double)(N*N*0.5*N))*calc_mag_odd() << endl; // only do half of z
            mag_even_out << sweep << "  " << (1/(double)(N*N*0.5*N))*calc_mag_even() << endl; // only do half of z
         }      
         if ((sweep > 150000) && (sweep % 20000 == 0)) {
            print_config(name+"_"+to_string(sweep));
            mag = calc_mag();
            avg_m += mag;
            avg_m2 += mag*mag;
            avg_count += 1;
         }      
    }
    // average magnetization
    avg_m /= (double)avg_count; 
    avg_m2 /= (double)avg_count; 
    flucts =(1/(double)(N*N*N))*(avg_m2 - avg_m);
    //flucts = (avg_m2 - avg_m);
    avg_m /= (double)(N*N*N); 
    cout << "Average total mag: " << avg_m << "\n";
    cout << "Average fluctuations: " << flucts << "\n";
    //fprintf(misc,"%d %f\n",avg_count,avg_m);
    //printf("%f %d %f\n",temp,avg_count,avg_m);
    mag_out.close();
    mag_odd_out.close();
    mag_even_out.close();
}

void Config::print_config(string name){
   // NOTE: This prints a slice of the XZ plane at y = 0. 
   int i,k;
   ofstream config_out; // output file
   config_out.open(name+".out",ios::out);
   for (i=0; i<N; i++) { 
        config_out << "\n";
            for (k=0; k<N; k++) {  
               config_out << coords[i][0][k] << "   " ;
            }
        config_out << "\n";
    }
    config_out.close();
}
/*int main() {
//int main(int argc, char*argv[]) {

    // take some values from std in: oddconst-nsweeps, seed, file name
    //if (argc < 4) {
    //   cerr << "Usage: " << argv[0] << " oddconst-nsweeps" << " temperature" << " box side length" << endl;
    //   return 1;
    //}

    // files for printing
    FILE *spincorr;

    // initialize configuration
    int i,j,k,N;
    int nsweeps;
    double T,mu;
    string name;
    vector<double> corres; 
    double mag;
   
    T = 0.0;
    mu = 0;
    N = 100; // sites per side
    nsweeps = 100000;
    name = "configT0-mu0-N100-isoF-nsw100000";
    spincorr = fopen(("Corrs_3dLG_"+name+".out").c_str(),"w");
    Config config1 (N, T, mu, 1.0, 1.0, 1.0); //N, temp, mu, Jx, Jy, Jz
    config1.init_lattice();

    // Monte Carlo simulation  
    config1.monte_carlo(nsweeps);
   
    // print final configuration
    config1.print_config(name);
   
    // calculate spatial correlations 
    mag = config1.calc_mag();
    corres = config1.space_corr(mag);
    cout << "T: " << T << " mu: " << mu << " Chi: " << config1.Chi << "\n";
    // write out spin-spin correlation function 
    for (int d=0; d<round(0.25*N); d++) {
       fprintf(spincorr,"%d %f\n",d,corres[d]);
    }      


    // analysis: calculate shit
    // TO DO: MAKE PRINTING INTO ONE METHOD?? 

    // acceptance ratio
    //double acceptance = 0;
    //acceptance = (double)accept/sweeps_tot;
    //fprintf(misc,"Acceptance ratio is %f\n",acceptance);
    //printf("Acceptance ratio is %f\n",acceptance);
}
*/
