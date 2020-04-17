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
#define clr(a) memset(a,-1,sizeof(a))
#define mod 1000000007
#define fastio ios_base::sync_with_stdio(false);cin.tie(NULL)
#define endl "\n"
#define INF 1e+18
using namespace std;

 /*
unique(all(vec)); will remove all duplicate elements from the vector
find_by_order() - Returns an iterator to the k-th largest element (counting from zero) 
order_of_key()  - The number of items in a set that are strictly smaller than our item 
 */
// ll dp[10000][10000][2];
vl dp(1000,vl(1000,-1);
ll special;
ll digSum(ll index,ll sum,ll tight,vl digits)
{
    ll i,j,k,l,m,n;
    if(index>=digits.size()){
        if(sum%special==0 && sum){
            // cout<<sum<<endl;
            return(1);

        }
        else
            return(0);
        // return(sum);
    }
 
    if(dp[index][sum][tight]!=-1 && tight!=1)
    {
        return(dp[index][sum][tight]);
    }
 
    ll range;
 
    if(tight)
        range = digits[index];
    else
        range = 9;
 
    ll val = 0;
 
    for(i=0;i<=range;i++)
    {
       ll new_tight = 0;
        if(tight)
        {
            if(digits[index]==i)
                new_tight = 1;
        }
 
        val+=digSum(index+1,sum+i,new_tight,digits);
        val%=mod;
 
    }
 
    if(!tight)
    {
        dp[index][sum][tight] = val;
    }

    val%=mod;
 
    return(val);
 
 
}
bool isSmaller(string str1, string str2) 
{ 
    // Calculate lengths of both string 
    int n1 = str1.length(), n2 = str2.length(); 
  
    if (n1 < n2) 
    return true; 
    if (n2 < n1) 
    return false; 
  
    for (int i=0; i<n1; i++) 
    if (str1[i] < str2[i]) 
        return true; 
    else if (str1[i] > str2[i]) 
        return false; 
  
    return false; 
} 
string findDiff(string str1, string str2) 
{ 
    // Before proceeding further, make sure str1 
    // is not smaller 
    if (isSmaller(str1, str2)) 
        swap(str1, str2); 
  
    // Take an empty string for storing result 
    string str = ""; 
  
    // Calculate length of both string 
    int n1 = str1.length(), n2 = str2.length(); 
  
    // Reverse both of strings 
    reverse(str1.begin(), str1.end()); 
    reverse(str2.begin(), str2.end()); 
      
    int carry = 0; 
  
    // Run loop till small string length 
    // and subtract digit of str1 to str2 
    for (int i=0; i<n2; i++) 
    { 
        // Do school mathematics, compute difference of 
        // current digits 
          
        int sub = ((str1[i]-'0')-(str2[i]-'0')-carry); 
          
        // If subtraction is less then zero 
        // we add then we add 10 into sub and 
        // take carry as 1 for calculating next step 
        if (sub < 0) 
        { 
            sub = sub + 10; 
            carry = 1; 
        } 
        else
            carry = 0; 
  
        str.push_back(sub + '0'); 
    } 
  
    // subtract remaining digits of larger number 
    for (int i=n2; i<n1; i++) 
    { 
        int sub = ((str1[i]-'0') - carry); 
          
        // if the sub value is -ve, then make it positive 
        if (sub < 0) 
        { 
            sub = sub + 10; 
            carry = 1; 
        } 
        else
            carry = 0; 
              
        str.push_back(sub + '0'); 
    } 
  
    // reverse resultant string 
    reverse(str.begin(), str.end()); 
  
    return str; 
} 
ll digitDP(string a)
{
    ll i,j,k,l,m,n;
    // ll places= digits(a);
    vl digits1;
 
    // ll copy = a;
 
    for(i=0;i<a.size();i++)
    {
        digits1.pb(a[i]-'0');
        // copy/=10;
    }
 
    // reverse(digits1.begin(),digits1.end());
 
    // copy = b;
 
    // vl digits2;
 
    // places = digits(b);
 
    // for(i=0;i<places;i++)
    // {
    //     digits2.pb(copy%10);
    //     copy/=10;
    // }
 
    // reverse(digits2.begin(),digits2.end());
 
    // clr(dp);
    // ll num1 = digSum(0,0,1,digits2);
    // clr(dp);
    // ll num2 = digSum(0,0,1,digits1);
 
    //cout<<num1<<" "<<num2<<endl;
 
 
    return(digSum(0,0,1,digits1));
 
 
 
}

int main()
{
    fastio;
 
    ll a,b,c,i,j,k,l,m,n,t,p;
    

    string inp;

    cin>>inp;

    inp = findDiff(inp,"1");
    
    // cout<<inp<<endl;
//     cin>>t;
 
//     while(t--)
//     {
        // clr(dp);
        cin>>b;

        special = b;


 
        cout<<digitDP(inp)<<endl;
 
    // }
 
 
    
    
} 