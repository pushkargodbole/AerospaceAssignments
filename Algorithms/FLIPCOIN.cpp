
/*****************************************************************************************************************************************************************
Problem : FLIPCOIN (Level 4) From Codechef
******************************************************************************************************************************************************************
Problem statement :
There are N coins kept on the table, numbered from 0 to N - 1. Initally, each coin is kept tails up. You have to perform two types of operations :
1) Flip all coins numbered between A and B. This is represented by the command "0 A B"
2) Answer how many coins numbered between A and B are heads up. This is represented by the command "1 A B".
Input :
The first line contains two integers, N and Q. Each of the next Q lines are either of the form "0 A B" or "1 A B" as mentioned above.
Output :
Output 1 line for each of the queries of the form "1 A B" containing the required answer for the corresponding query.
Sample Input :
4 7
1 0 3
0 1 2
1 0 1
1 0 0
0 0 3
1 0 3 
1 3 3

Sample Output :
0
1
0
2
1

Constraints :
1 <= N <= 100000
1 <= Q <= 100000
0 <= A <= B <= N - 1
*******************************************************************************************************************************************************************
Programmer :
Pushkar Godbole
UG Sophomore
Aerospace Engineering IIT-Bombay
*******************************************************************************************************************************************************************
Language used : C++
*******************************************************************************************************************************************************************
Codechef Username : pushkar_g
Note :
I tried to submit this problem on Codechef, but it always gives a "time limit exceeded" error. I have tried to optimize the code as much as I can and it works in less than 2sec(time limit) on my machine. But the site still won't accept it
THE MAIN PART OF THE CODE ACTUALLY EXECUTES WITHIN NO TIME. IT IS THE 'printf' ACCORDING TO ME, WHICH IS TAKING ALL THE TIME. COMMENTING OUT THAT LINE(146) OR REDIRECTING THE OUTPUT TO A TEXT FILE TESTIFIES THE DIFFERENCE.
So I am mailing this solution to you. Sincerely hoping that you will consider my request and accept the solution after verifying its correctness.
*******************************************************************************************************************************************************************
Idea behind the code :
@ Input data is taken and stored in variables, N, Q, A, B, option using 'scanf'.
Part 1 :
@ The key points and the total number of keys, where there is a transition between heads and tails, are stored and edited dynamically in the array 'cursor'. 
@ initially the 'cursor' array has, 2 key points '0' and 'N'. More points get added to the array at appropriate places according to the inputs.
Part 2 :
@ For the next part, of counting the number of heads, the fact that the state(head/tail) of the first coin, determines the state of all remaining coins has been utilized. Variable 'init' stores this state. (init=0 => tail / init=1 => head)
@ First the values of 'i' and 'j' such that cursor[i]<=A and cursor[j]>=B are computed. The number of heads between cursor[i] and cursor[j] is stored in 'dump'.
@ Then excess number of coins which had been introduced as a result of A>cursor[i] and B<cursor[j] are subtracted from 'dump' and the new number is stored in 'heads'.
@ Finally, the number 'heads' is printed using printf.
******************************************************************************************************************************************************************/

#include<iostream>
#include <stdio.h>
#include<string>
#include<sstream>
using namespace std;
int main()
{
	int N,Q,A,B,option,cursor[100000],keys=2,init=0,flagA,flagB,i,j,k,count=0;					//Defining all variables.		
	scanf("%d %d", &N, &Q);																		//Taking in values for N and Q
	cursor[0] = 0;
	cursor[1] = N;																				//Storing the initial and final values of cursor
	for(int count=0;count<Q;count++)															//Iterating over Q, to take in values of A and B
	{
		scanf("%d %d %d", &option, &A, &B);										
		i = 0;
		j = 0;
		if(option==0)																			//Flipping coins
		{
			while(cursor[i]<A && i<keys) i++;													//Computing location of A w.r.t. keys
			if(cursor[i]==A && A!=0)															//If value of A equals value at some key
			{
				for(int k=i;k<keys;k++) cursor[k] = cursor[k+1];								//Removing that particular key and rearranging the cursor array
				keys--;
			}
			else if(cursor[i]!=A)																//For a new value of A introduced
			{
				for(int k=keys;k+1>i;k--) cursor[k+1] = cursor[k];								//Making space for new value of A
				cursor[i] = A;																	//Adding the new value of A to the array
				keys++;
			}
			while(cursor[j]<B && j<keys) j++;													//Computing location of B w.r.t. keys
			if(cursor[j]==B && B+1!=N && cursor[j+1]!=B+1)										//A special case of introducing a section with just one coin			
			{
				for(int k=keys;k>j;k--) cursor[k+1] = cursor[k];								//Making space for new value of B
				cursor[j+1] = B+1;																//Adding the new value of B to the array
				keys++;
			}
			else if(cursor[j]==B && B+1!=N && cursor[j+1]==B+1)									//A special case of deleting the key for a section with just one coin
			{
				for(int k=j+1;k<keys;k++) cursor[k] = cursor[k+1];								//Removing that particular key and rearranging the cursor array
				keys--;
			}
			if(cursor[j]==B+1 && B+1!=N)														//If value of B+1 equals value at some key				
			{
				for(int k=j;k<keys;k++) cursor[k] = cursor[k+1];								//Removing that particular key and rearranging the cursor array
				keys--;
			}
			else if(cursor[j]>B+1)																//For a new value of B+1 introduced
			{	
				for(int k=keys-1;k+1>j;k--) cursor[k+1] = cursor[k];							//Making space for new value of B+1
				cursor[j] = B+1;																//Adding the new value of B+1 to the array
				keys++;
			}
			if(A==0)																			//Case when the first coin flips changing the state of subsequent coins
			{
				if(init==0) init = 1;
				else init = 0;
			}
		}
		if(option==1)																			//Counting heads
		{
			while(cursor[i]<=A && i<keys) i++;													//Computing location of A w.r.t. keys such tat 
			if(cursor[i]!=A) i--;
			while(cursor[j]<B && j<keys) j++;													//Computing location of B w.r.t. keys
			if(cursor[j]==B) j++;
			int heads=0,dump=0;
			int k = i;
			if(init==1 && i%2==0 || init==0 && i%2!=0)											//When A lies in the heads region
			{
				while(k+1<=j)
				{
					dump = dump + cursor[k+1] - cursor[k];
					k = k + 2;
				}
			}
			else if(init==0 && i%2==0 || init==1 && i%2!=0)										//When A lies in tails region
			{
				while(k+2<=j)
				{
					dump = dump + cursor[k+2] - cursor[k+1];
					k = k + 2;
				}
			}
			if(init==0 && i%2!=0 || init==1 && i%2==0) dump = dump - A + cursor[i];				//Subtracting the extra heads behind A from dump when A is in the heads region
			if(init==0 && (j-1)%2!=0 || init==1 && (j-1)%2==0) dump = dump - cursor[j] + B + 1;	//Subtracting the extra heads after B from dump when B is in the heads region
			heads = dump;
			printf("%d\n", heads);																//Printing out the data
		}
	}
	return(0);
}
