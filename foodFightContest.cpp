#include <string>
#include <vector>

using namespace std;

string solution(vector<int> food) {
    string answer = "";
    string front = "", back = "";
    for (int i = 1; i <= (food.size()-1); i++) {
        int iter = (food[i] / 2);
        front.append(iter, i+'0'); // (문자로 바꾸고 싶은 숫자)+'0' -> '(바뀐 문자)'
    }
    front.push_back(0+'0');
    for (int i = (food.size()-1); i >= 1; i--) {
        int iter = (food[i] / 2);
        back.append(iter, i+'0');
    }
    answer = front + back;
    return answer;
}