#include <iostream>
#include <vector>
using namespace std;

bool is_prime(int n)
{
    if (n == 1)
    {
        return false;
    }
    for (int d = 2; d < n; d++)
    {
        if (n % d == 0)
        {
            return false;
        }
    }
    return true;
}
/*
int main()
{
    for (int i = 1; i <= 11; i++)
    {
        if (is_prime(i))
        {
            cout << i << " Is prime" << endl;
        }
        else
        {
            cout << i << " Is not prime" << endl;
        }
    }
    return 0;
}
*/
vector<int> find_primes(int nr)
{
    vector<int> primes;
    int n = 1;
    while (primes.size() < nr)
    {
        if (is_prime(n))
        {
            primes.push_back(n);
        }
        n++;
    }
    return primes;
}

int main()
{
    vector<int> primes = find_primes(100);

    for (int p : primes)
    {
        cout << p << endl;
    }
    return 0;
}