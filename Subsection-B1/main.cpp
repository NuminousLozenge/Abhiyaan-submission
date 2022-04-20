#include <bits/stdc++.h>
#define int long long

using namespace std;

int32_t main()
{
    int m,n,k;
    cin>>m>>n>>k;

    int t = m*n;    //t is total length
    int num[t];     // array of length m*n

    int l = -1;  //left partition
    int r = t;   //right partition
    int flag = 0;

    for(int i = 0; i<t; i++ )
    {
        cin>>num[i];
    }

    while(true)
    {
        int mid = (r+l)/2;

        if(num[mid]<k)     // to find the position of k wrt middle element
        {
            l = mid;
        }
        else
        {
            r = mid;
        }

        if(r<t && num[r] == k)    //element is found
        {
            flag = 1;
            break;
        }
        else if(r == l+1)     //search exhausted as limiting condition is reached
        {
            break;
        }
    }


    if(flag == 1 )
    {
        cout<<"True"<<endl;
        if(r%n == 0)
        {
            cout<<n-1<<" "<<r/n;         //determining position of element in matrix
        }                                // from final value of r
        else
        {
            cout<<(r%n) - 1<<" "<<(r/n)+1;
        }
    }
    else
    {
        cout<<"False";
    }

    return 0;
}
