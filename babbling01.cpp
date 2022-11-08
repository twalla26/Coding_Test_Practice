#include <string>
#include <vector>
using namespace std;

int solution(vector<string> babbling) {
    int answer = 0;
    vector<string> bBabbling = {"aya", "ye", "woo", "ma"};
    for (string elem : babbling) {
        for (int i = 0; i < 4; i++) {
            int n = elem.find(bBabbling[i]);
            if (n == -1)
                continue;
            int stringSize = bBabbling[i].size();
            elem.replace(n, stringSize, "_");
        }
        bool result = true;
        for (int i = 0; i < elem.size(); i++) {
            if (elem[i] != '_')
                result = false;
        }
        if (result == true)
            answer += 1;
    }
    return answer;
}