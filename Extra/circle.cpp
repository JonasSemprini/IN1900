#include <iostream>
#include <cmath>
using namespace std;

const double pi = M_PI;

class Circle
{
private:
    double radius;
    double cx;
    double cy;

public:
    Circle(double r)
    {
        radius = r;
        cx = 0;
        cy = 0;
    }
    double area()
    {
        return pi * radius * radius;
    }
};

int main()
{
    Circle s(4);
    cout << s.area() << endl;
    // Circle *s_ptr = new Circle(4);
    // cout << s_ptr->area() << endl;
    // delete s_ptr;
}