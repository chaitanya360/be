#include <iostream>
using namespace std;

int main()
{
    int p = 7;
    int q = 5;
    int r = 4;

    for (r = 4; r <= 8; r++)
    {
        if ((p - q - r) < (r - p))
            continue;
        p = 8 + r;
        q = 6 + r;
    }

    cout << p + q;
}