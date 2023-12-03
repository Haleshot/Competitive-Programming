#include <iostream>
using namespace std;

long long mod_pow(long long base, long long exp, long long mod) {
    long long result = 1;
    while (exp > 0) {
        if (exp % 2 == 1) {
            result = (result * base) % mod;
        }
        base = (base * base) % mod;
        exp /= 2;
    }
    return result;
}

int main() {
    long T;
    cin >> T;
    while (T != 0) {
        long long N, X, M;
        cin >> N >> X >> M;
        long long power_value = mod_pow(N, X, M);
        cout << power_value << endl;
        T--;
    }
    return 0;
}