#include <cstring>
#include <iostream>
#include <string>
#include <vector>

bool check(const std::string& hand, const std::string& word) {
  std::vector<int> counts(26, 0);
  for(char c: hand) {
    if(!isalpha(c)) return false;
    counts[toupper(c) - 'A'] += 1;
  }

  for(char c: word) {
    if(!isalpha(c)) return false;
    if((counts[toupper(c) - 'A'] -= 1) < 0) {
      return false;
    }
  }

  return true;
}

int score(const std::string& word) {
  int score = 0;
  std::vector<int> points{
    1, 3,  3, 2,  1, 4, 2,
    4, 1,  8, 5,  1, 3, 1,
    1, 3, 10, 1,  1, 1, 1,
    5, 4,  8, 3, 10
  };

  for(char c: word) {
    score += points[toupper(c) - 'A'];
  }

  return score;
}

int main(int argc, char** argv) {
  if(argc != 3) {
    std::cerr << "USAGE: ./clabbers [hand] [word]" << std::endl;
    return 1;
  }

  std::string hand = argv[1];
  std::string word = argv[2];

  if(check(hand, word)) {
    int points = score(word);
    const char* s = (points == 1)? "" : "s";
    std::cout << points << " point" << s << "." << std::endl;
    return 0;
  }
  else {
    std::cout << "Invalid." << std::endl;
    return 2;
  }
}
