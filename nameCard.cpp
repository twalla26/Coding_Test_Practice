#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> sizes) {
    int answer = 0;
    for (vector<int> &v : sizes) {
        vector<int> temp;
        if (v[0] < v[1]) {
            temp.push_back(v[1]);
            temp.push_back(v[0]);
            v.swap(temp);
            temp.clear();
        }
    }
    int wMax = sizes[0][0], hMax = sizes[0][1];
    for (vector<int> &v : sizes) {
        if (v[0] > wMax)
            wMax = v[0];
        if (v[1] > hMax)
            hMax = v[1];
    }
    answer = wMax * hMax;
    return answer;
}
