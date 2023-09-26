#include <iostream>
#include <string>

using namespace std;

double F2C(double F)
{
    return 5 * (F - 32) / 9;
}

int main()
{
    double temp = 110.;
    cout << temp << " F" << endl;
    cout << F2C(temp) << " C" << endl;
    return 0;
}