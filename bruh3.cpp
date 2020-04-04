#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    int f, s;

    cout<<"input f:";
    cin>>f;

    cout<<"input s:";
    cin>>s;

    if( s > 0 && s < f)
    {
        cout<<"Benda berada di ruang 1"<<endl;
    }
    else if( s > f && s <= 2*f )
    {
        cout<<"Benda berada di ruang 2";
    }
    else if( s > 2*f)
    {
        cout<<"Benda berada di ruang 3";
    }
    else
    {
        cout<<"benda tidak berada di ruang 1, 2 ataupun 3";
    }
    
}