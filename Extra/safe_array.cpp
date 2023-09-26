#include <iostream>
#include <cassert>
using namespace std;
class SafeArray
{
private:
    double *data;
    int length;

public:
    SafeArray(int N)
    {
        length = N;
        data = new double[N];
        for (int i = 0; i < N; i++)
        {
            data[i] = 0;
        }
    }

    ~SafeArray()
    {
        cout << "Running Destructor" << endl;
        delete[] data;
    }

    void set_entry(int index, double val)
    {
        assert(index >= 0 && index < length);
        data[index] = val;
    }

    double get_entry(int index)
    {
        assert(index >= 0 && index < length);
        return data[index];
    }
};

int main()
{
    SafeArray arr{10};
    arr.set_entry(5, 4.6);
    double val = arr.get_entry(2);
    cout << val << endl;
}