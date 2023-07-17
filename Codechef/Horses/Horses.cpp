#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

int main() 
{
	int T;
	cin >> T;
	while(T--) 
    {
	    int N;
	    cin >> N;
	    long long nums[N];
	    for(int i = 0; i < N; i++) 
        {
	        cin >> nums[i];
	    }
	    sort(nums, nums+N);
	    long long diff = 100000000000;
	    for(int i = 0; i < N - 1; i++) 
        {
	        if(nums[i+1] - nums[i] < diff)
            {
	            diff = nums[i+1] - nums[i];
	        }
	    }
	    cout << diff << '\n';
	}
	return 0;
}