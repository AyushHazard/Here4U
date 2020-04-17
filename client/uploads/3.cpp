#include <iostream>
//#include <bits/stdc++.h>
#include <cstdio>
#include <list>
#include <vector>
#include <stack>
#include <queue>
#include <cstring>
#include <limits.h>
#include <set>
#include <cmath>
#include <algorithm>
#include <string>
#include <map>
#include <unordered_map>
#include <utility>
#define all(x) (x).begin(), (x).end() 
#define ull unsigned long long int
#define ll long long int 
#define ld long double
#define pb push_back
#define ep emplace_back
#define mp make_pair
#define pcc pair<char,char>
#define pii pair<int,int>
#define pll pair<ll,ll>
#define pq priority_queue <ll> 
#define ppq priority_queue <pll>
#define vi vector <int>
#define vb vector <bool>
#define vl vector <ll>
#define vpl vector <pll>
#define vc vector <char>
#define mmi multimap<int,int>
#define mml multimap<ll,ll>
#define mmc multimap<char,char>
#define mi map<int,int>
#define ml map<ll,ll>
#define mc map<char,char>
#define clr(a) memset(a,0,sizeof(a))
#define mod 1000000007
#define fastio ios_base::sync_with_stdio(false);cin.tie(NULL)
#define endl "\n"
#define INF 1e+18
using namespace std;
bool primecheck(ll a)
{
    bool check  = true;

    if(a==1)
        return(false);

    for(ll i=2;i<=sqrt(a);i++)
    {
        if(a%i==0){
            check = false;
            break;
        }
    }

    return(check);
}
vl printDivisors(ll n) 
{ 
    // Note that this loop runs till square root 
    vl sol;
    for (ll i=1; i<=sqrt(n); i++) 
    { 
        if (n%i == 0) 
        { 
            // If divisors are equal, print only one 
            if (n/i == i){ 
                //printf("%d ", i);
               sol.pb(i); 
                 }
  
            else {
                sol.pb(i);
                sol.pb(n/i);
            }// Otherwise print both 
                //printf("%d %d ", i, n/i); 
        } 
    } 
    return(sol);
} 
ll digits(ll a)
{
    return(floor(log10(a))+1);
}
ll bits(ll a)
{
    return(floor(log2(a))+1);
}
long long binpow(long long a, long long b, long long m) {
    a %= m;
    long long res = 1;
    while (b > 0) {
        if (b & 1)
            res = res * a % m;
        a = a * a % m;
        b >>= 1;
    }
    return res;
}
ll modInverse(ll a, ll m) 
{ 
    ll m0 = m; 
    ll y = 0, x = 1; 
  
    if (m == 1) 
      return 0; 
  
    while (a > 1) 
    { 
        // q is quotient 
        ll q = a / m; 
        ll t = m; 
  
        // m is remainder now, process same as 
        // Euclid's algo 
        m = a % m, a = t; 
        t = y; 
  
        // Update y and x 
        y = x - q * y; 
        x = t; 
    } 
  
    // Make x  
    if (x < 0) 
       x += m0; 
  
    return x; 
} 
// ll nCr(ll n,ll r)
// {
//     // fact needs to be pre-calculated
//     ll val1 = fact[n];
//     ll val2 = fact[n-r]*fact[r];
//     val2 = modInverse(val2,mod);
//     val1%=mod;
//     val2%=mod;
//     //cout<<val1<<" "<<val2<<endl;
//     return(val1*val2);
// }
int gcd(int a, int b) 
{ 
    // Everything divides 0  
    if (a == 0) 
       return b; 
    if (b == 0) 
       return a; 
   
    // base case 
    if (a == b) 
        return a; 
   
    // a is greater 
    if (a > b) 
        return gcd(a-b, b); 
    return gcd(a, b-a); 
}
ll lcm(ll a, ll b)  
 {  
    return (a*b)/gcd(a, b);  
 }
 void addEdge(vl adj[],ll u, ll v)
 {
    adj[u].pb(v);
    adj[v].pb(u);
 }
 vl path;
 void dfs(ll u, vl adj[], vb &visited, ll parent = -1)
 {
    visited[u] = true;
    path[u] = parent;
    // count<<u<<endl;
    for(ll i=0;i<adj[u].size();i++)
    {
        if(visited[adj[u][i]]==false)
        {
            dfs(adj[u][i],adj,visited,u);
        }
    }
 }
 /*
unique(all(vec)); will remove all duplicate elements from the vector
find_by_order() - Returns an iterator to the k-th largest element (counting from zero) 
order_of_key()  - The number of items in a set that are strictly smaller than our item 
 */

int main()
{
    fastio;

    ll a,b,c,i,j,k,l,m,n,t,p;

    cin>>t;

    while(t--)
    {
        cin>>a>>b>>c;

        vl one,two,three;

        for(i=0;i<a;i++)
        {
            cin>>m;
            one.pb(m);
        }

        for(i=0;i<b;i++)
        {
            cin>>m;
            two.pb(m);
        }

        for(i=0;i<b;i++)
        {
            cin>>n;
            three.pb(n);
        }

        vl final;

        sort(one.begin(),one.end());
        sort(two.begin(),two.end());
        sort(three.begin(),three.end());

        for(i=0;i<a;i++)
        {
            auto it = lower_bound(two.begin(), two.end(), one[i]);
            auto it2 = lower_bound(three.begin(), three.end(), one[i]);

            ll diff = INF;
            ll local = 0;ll sel2,sel1;

            if(it!=two.end())
            {
                diff = abs(one[i]-(*it));
                sel1 = *it;

            }
            ll gap = it-two.begin();
            gap--;

            if(gap!=-1)
            {
               if(abs(one[i]-two[gap])<diff)
                sel1 = two[gap];

                diff = min(diff,abs(one[i]-two[gap]));
            }

            local+=diff*diff;

            diff = INF;

            if(it2!=three.end())
            {
                diff = one[i]-(*it);
                sel2 = *it;

            }
            gap = it-three.begin();
            gap--;

            if(gap!=-1)
            {
                if(abs(one[i]-three[gap])<diff)
                {
                    sel2 = three[gap];
                }
                diff = min(diff,abs(one[i]-three[gap]));
            }

            local+=diff*diff;
            diff = abs(sel2-sel1);

            local+=diff*diff;

            final.pb(local);
        }

        for(i=0;i<b;i++)
        {
            auto it = lower_bound(one.begin(), one.end(), two[i]);
            auto it2 = lower_bound(three.begin(), three.end(), two[i]);

            ll diff = INF;
            ll local = 0;ll sel2,sel1;

            if(it!=one.end())
            {
                diff = abs(two[i]-(*it));
                sel1 = *it;

            }
            ll gap = it-two.begin();
            gap--;

            if(gap!=-1)
            {
               if(abs(two[i]-one[gap])<diff)
               {
                sel1 = one[gap];
               }
                diff = min(diff,abs(two[i]-one[gap]));
            }

            local+=diff*diff;

            diff = INF;

            if(it2!=three.end())
            {
                diff = two[i]-(*it);
                sel2 = *it;
            }
            gap = it-three.begin();
            gap--;

            if(gap!=-1)
            {
                if(abs(two[i]-three[gap])<diff)
                    sel2 = three[gap];
                diff = min(diff,abs(two[i]-three[gap]));
            }

            local+=diff*diff;

            diff = abs(sel2-sel1);

            local+=diff*diff;

            final.pb(local);
        }

        for(i=0;i<c;i++)
        {
            auto it = lower_bound(two.begin(), two.end(), three[i]);
            auto it2 = lower_bound(one.begin(), one.end(), three[i]);

            ll diff = INF;
            ll local = 0;
            ll sel1,sel2;

            if(it!=two.end())
            {
                diff = abs(three[i]-(*it));
                sel1 = *it;

            }
            ll gap = it-two.begin();
            
            gap--;

            if(gap!=-1)
            {
                if(abs(three[i]-two[gap])<diff)
                {
                    sel1 = two[gap];
                }
                diff = min(diff,abs(three[i]-two[gap]));

            }

            local+=diff*diff;

            diff = INF;

            if(it2!=one.end())
            {
                diff = abs(three[i]-(*it));
                sel2 = *it;

            }
            gap = it-one.begin();
            gap--;

            if(gap!=-1)
            {
                if(abs(three[i]-one[gap])<diff)
                    sel2 = one[gap];
                diff = min(diff,abs(three[i]-one[gap]));
            }

            local+=diff*diff;

            diff = abs(sel2-sel1);

            local+=diff*diff;

            final.pb(local);
        }

        sort(final.begin(),final.end());
        reverse(final.begin(),final.end());

        cout<<final[0]<<endl;
    }
    
}