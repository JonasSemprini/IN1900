#include <iostream>
using namespace std;

class Quadratic
{
public:
    double a;
    double b;
    double c;

    double evaluate(double x)
    {
        return a * x * x + b * x + c;
    }
};

int main()
{
    Quadratic f{1, 2, 1};
    cout << f.evaluate(3) << endl;
}