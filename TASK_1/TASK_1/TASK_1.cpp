#include <iostream>

void check(double z) {
    if (!z) {
        std::cout << "error n/0!";
        exit(1);
    }
}


int main()
{
    const int size = 5, sub_size = 4;
    const double d_base = -3, q_base = -4.67,
        q[size]{ q_base,-2,-2,-2,q_base },
        p[size]{ 0,1,1,1,1 },
        r[size]{ 1,1,1,1,0 },
        d[size]{ 0,d_base,d_base,d_base,0 };
    double e[sub_size], nn[size], x[size], z;

    //calculate all e in array and all-1 nn
    e[0] = -r[0] / q[0];
    nn[0] = d[0] / q[0];
    for (int i = 1; i < sub_size; i++) {
        z = q[i] + p[i] * e[i-1];
        check(z);
        e[i] = -r[i] / z;
        nn[i] = (d[i] - p[i] * nn[i-1])/z;
    }
    
    //calculate last nn in array
    z = q[sub_size] + p[sub_size] * e[sub_size-1];
    check(z);
    nn[sub_size] = d[sub_size] - p[sub_size] * nn[sub_size-1] / z;

    //calculate all x in array
    z = q[sub_size] + p[sub_size] * e[sub_size - 1];
    x[sub_size] = d[sub_size] - p[sub_size] * nn[sub_size - 1] / z;
    check(z);
    for (int i = size - 2; i > -1; i--) {
        x[i] = e[i] * x[i + 1] + nn[i];
    }

    int i = 1;
    for (auto val : x) {
        std::cout << "x[" << i++ << "] = " << val << std::endl;
    }
    return 0;
}


