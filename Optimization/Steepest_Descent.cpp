#include<iostream>
#include<fstream>
#include<Math.h>

using namespace std;

double f (double x1, double x2);

double f (double x1, double x2)
{
       double d = (((x1*x1) + (x2) - 11) * ((x1*x1) + (x2) - 11)) + (((x1) + (x2*x2) - 7) * ((x1) + (x2*x2) - 7));
       return d;
}

int main()
{
    cout<<"Pushkar Godbole (09D01005)"<<"\n\n";
    fstream fout("Output_Steepest_Descent_Method.txt", ios :: out);
    fstream fo("Output_Steepest_Descent_Method.xls", ios :: out);
    fo<<"Iteration No."<<"\t"<<"X1"<<"\t"<<"X2"<<"\t"<<"f(X1,X2)"<<"\n\n";
    double x1_initial, x2_initial, epsilon, x1, x2, counter=0, gradient[20], d[20], mod=1000, delta, alpha[3], interval, delta1, delta2, alpha_a, alpha_b, gss_epsilon, alpha_final;
    cout<<"Please enter the intial values for x1 and x2"<<"\n\n";
    cin>>x1_initial>>x2_initial;
    cout<<"Please enter the value for epsilon"<<"\n\n";
    cin>>epsilon;
    cout<<"Please enter the value for epsilon for golden section search"<<"\n\n";
    cin>>gss_epsilon;
    cout<<"Enter the value for delta"<<"\n\n";
    cin>>delta;
    x1=x1_initial;
    x2=x2_initial;
    //cout<<f(x1,x2)<<"\n\n";
    while (mod >= epsilon)
    {
          counter++;
          fo<<counter<<"\t"<<x1<<"\t"<<x2<<"\t"<<f(x1,x2)<<"\n";
          delta1 = 1.618 * delta;
          delta2 = 1.618 * delta1;
          alpha[0] = delta;
          alpha[1] = alpha[0] + delta1;
          alpha[2] = alpha[1] + delta2;
          gradient[0] = (f(x1+0.00001,x2) - f(x1,x2)) / 0.00001 ;
          gradient[1] = (f(x1,x2+0.00001) - f(x1,x2)) / 0.00001 ;   
          //cout<<gradient[0]<<"  "<<gradient[1]<<"\n\n";
          mod = sqrt((gradient[0] * gradient[0]) + (gradient[1] * gradient[1]));
          //cout<<mod<<"\n\n";
          if(mod < epsilon)
          {
                 fout<<"The points of minima are : "<<x1<<" and "<<x2<<"\n\n";
                 fout<<"The minimum value of the function is : "<<f(x1,x2)<<"\n\n";
                 break;
          }
          d[0] = -gradient[0];
          d[1] = -gradient[1];
          //cout<<f(x1 + (alpha[1]*d[0]) , x2 + (alpha[1]*d[1]))<<"\t"<<f(x1 + (alpha[0]*d[0]) , x2 + (alpha[0]*d[1]))<<"\n\n";
          while ((f(x1 + (alpha[1]*d[0]) , x2 + (alpha[1]*d[1])) >= f(x1 + (alpha[0]*d[0]) , x2 + (alpha[0]*d[1]))) || (f(x1 + (alpha[1]*d[0]) , x2 + (alpha[1]*d[1])) >= f(x1 + (alpha[2]*d[0]) , x2 + (alpha[2]*d[1]))))
          {
                delta2 = 1.618 * delta2;
                alpha[0] = alpha[1];
                alpha[1] = alpha[2]; 
                alpha[2] = alpha[1] + delta2;
          }
          interval = alpha[2] - alpha[0];
          //cout<<interval<<"\n\n";
          alpha_b = alpha[0] + (0.618*interval);
          alpha_a = alpha[1];
          while(interval>gss_epsilon)
          {
                                     if(f(x1 + (alpha_a*d[0]), x2 + (alpha_a*d[0])) < f(x1 + (alpha_b*d[0]), x2 + (alpha_b*d[0])))
                                     {
                                         alpha[2] = alpha_b;
                                         alpha_b = alpha_a;
                                         interval = alpha[2] - alpha[0];
                                         alpha_a = alpha[0] + (0.382 * interval);
                                     }
                                     else if(f(x1 + (alpha_a*d[0]), x2 + (alpha_a*d[0])) > f(x1 + (alpha_b*d[0]), x2 + (alpha_b*d[0])))    
                                     {
                                         alpha[0] = alpha_a;
                                         alpha_a = alpha_b;
                                         interval = alpha[2] - alpha[0];
                                         alpha_b = alpha[0] + (0.618 * interval);
                                     }
                                     else if(f(x1 + (alpha_a*d[0]), x2 + (alpha_a*d[0])) == f(x1 + (alpha_b*d[0]), x2 + (alpha_b*d[0])))    
                                     {
                                         alpha[0] = alpha_a;
                                         alpha[2] = alpha_b;
                                         interval = alpha[2] - alpha[0];
                                         alpha_b = alpha[0] + (0.618 * interval);
                                         alpha_a = alpha[0] + (0.382 * interval);
                                     }
          }
          alpha_final = (alpha[0] + alpha[2]) / 2;
          //cout<<alpha_final<<"\n\n";
          x1 = x1 + (alpha_final * d[0]);
          x2 = x2 + (alpha_final * d[1]);
    }
    return 1;
}      
          
          
                
                  
          
          
     
    
