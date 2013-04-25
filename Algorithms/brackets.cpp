#include<iostream>
#include<string>
#include<math.h>
using namespace std;
int main()
{
	int n;
	cout << "n = ";
	cin >> n;
	int count = 1;
	cout << count << " ";
	string print = "";
	for(int i=0;i<n;i++) print = "}" + print;
	for(int i=0;i<n;i++) print = "{" + print;
	cout << print << endl;
	int max;
	max = pow(2, n)-1;
	max = max << n;
	int x = max;
	while(x>(pow(2,n)-1))
	{
		print = "";
		x--;
		int sum = 0;
		bool done = true;
		int temp = x;
		for(int i=0;i<2*n;i++)
		{
			int mod = temp%2;
			temp = temp/2;
			if(mod==0) sum++;
			else sum--;
			if(sum<0)
			{
				done = false;
				break;
			}
		}
		if(sum!=0) done = false;
		if(done==true)
		{
			count++;
			cout << count << " ";
			temp = x;
			for(int i=0;i<2*n;i++)
			{
				if(temp%2==0) print = "}" + print;
				else print = "{" + print;
				temp = temp/2;
			}
			cout << print << endl;
		}
	}
	return 0;
}
