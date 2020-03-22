#include <iostream>
#include <queue>

using namespace std;

int main(int argc, char const *argv[])
{
    vector <int> arr;

    cout<<"array awal:"<<endl;
    for (int i = 1; i < 13; i++)
    {
        arr.push_back(i);
        cout<<i<<" ";
    }
    cout<<endl;
    
    vector <int> result;

    queue < vector<int> > arrQueue;
    arrQueue.push(arr);

    while ( !arrQueue.empty() )
    {
        vector <int> arrToCheck = arrQueue.front();
        arrQueue.pop();

        int length = arrToCheck.size();

        if (length != 0)
        {
            int midIndex = length/2;
            result.push_back(arrToCheck[midIndex]);

            vector <int> leftArr;
            for (int i = 0; i < midIndex; i++)
            {
                leftArr.push_back(arrToCheck[i]);
            }

            vector <int> rightArr;
            for (int i = midIndex + 1; i < length; i++)
            {
                rightArr.push_back(arrToCheck[i]);
            }

            arrQueue.push(leftArr);
            arrQueue.push(rightArr);
        }
    }
    
    cout<<"array hasil:"<<endl;
    for (int i = 0; i < result.size(); i++)
    {
        cout<<result[i]<<" ";
    }

    return 0;
}
