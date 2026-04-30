#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter number of rows (half diamond): ";
    cin >> n;

    int total = 2 * n - 1;

    for (int i = 1; i <= total; i++) {
        int stars = (i <= n) ? i : total - i + 1;

        // print spaces
        for (int s = 0; s < n - stars; s++)
            cout << " ";

        // print stars
        for (int j = 0; j < 2 * stars - 1; j++)
            cout << "*";

        cout << endl;
    }

    return 0;
}