#include <iostream>
#include <vector>
using namespace std;

void solve()
{
    int N = 10001;

    double *t = new double[N];
    double *u = new double[N];

    double a = 4.3;
    double u0 = 15.7;

    double dt = 0.001;
    t[0] = 0;
    u[0] = u0;

    for (int i = 1; i < N - 1; i++)
    {
        t[i] = t[i - 1] + dt;
        u[i] = u[i - 1] + dt * (-a * u[i - 1]);
        if (i % 100 == 0)
        {
            // cout << "t=" << t << "u=" << u << endl;
            printf("t=%4.1f u=%g\n", t[i], u[i]);
        }
    }

    delete[] t;
    delete[] u;
}
void solve_with_vectors()
{
    int N = 10001;

    vector<double> t;
    vector<double> u;

    double a = 4.3;
    double u0 = 15.7;

    double dt = 0.001;
    t.push_back(0);
    u.push_back(u0);

    for (int i = 1; i < N; i++)
    {
        t.push_back(t[i - 1] + dt);
        u.push_back(u[i - 1] + dt * (-a * u[i - 1]));

        if (i % 100 == 0)
        {
            // cout << "t=" << t << "u=" << u << endl;
            printf("t=%4.1f u=%g\n", t[i], u[i]);
        }
    }
}

int main()
{
    //solve();
    solve_with_vectors();
}