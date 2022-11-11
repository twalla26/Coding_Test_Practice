using namespace std;

long long solution(int price, int money, int count)
{
    long long answer = -1;
    long long fee = 0;
    for (int i = 1; i <= count; i++) {
        fee += price * i;
    }
    if (fee < money) {
        answer = 0;
    }
    else {
        answer = fee - money;
    }
    return answer;
}