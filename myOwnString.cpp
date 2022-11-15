#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

vector<string> solution(vector<string> strings, int n) { // 인덱스 기준으로 문자열 정렬
    vector<string> answer;
    vector<vector<string>> splited(26); // 문자열이 담긴 이차원 벡터
    for (string &elem: strings) // 주어진 strings 벡터의 객체들에 대해
        splited[(int)elem[n]-97].push_back(elem); // elem[0]이 a이면 splited 벡터의 0번째 벡터에 elem을 추가함.
    // elem의 n번째 알파벳이 무엇인지에 따라 elem이 나눠짐.
    for(auto &v: splited){ // 나눠진 splited 배열에서 각각의 벡터들을 또다시 알파벳 기준으로 정렬
        sort(v.begin(), v.end()); // n번째 알파벳이 똑같이 a인 경우, 둘을 정렬하기 위함.
    }

    for(auto &v: splited){ // 모든 string이 정렬되었으므로, answer벡터에 푸쉬백
        for (auto &e: v){
            answer.push_back(e);
        }
    }

    return answer;
}