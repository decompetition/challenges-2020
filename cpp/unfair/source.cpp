#include <cstring>
#include <iostream>
#include <string>
#include <tuple>

// https://en.wikipedia.org/wiki/Playfair_cipher
const std::string UNFAIR[] = {
  "LREOT",
  "HQGNU",
  "YIVXC",
  "DBKFM",
  "PZWAS"
};

std::tuple<size_t, size_t> find(char x) {
  for(size_t r = 0; r < 5; ++r) {
    size_t c = UNFAIR[r].find(x);
    if(c != std::string::npos) {
      return std::make_tuple(r, c);
    }
  }

  std::cerr << "Chaos and corruption!" << std::endl;
  std::exit(1);
}

std::string clean(const std::string& input) {
  std::string result;

  for(size_t i = 0; i < input.size(); ++i) {
    if(input[i] == 'j' || input[i] == 'J') {
      result += 'I';
    }
    else if(isalpha(input[i])) {
      result += toupper(input[i]);
    }
  }

  if(result.size() % 2 == 1) {
    result += 'X';
  }

  return result;
}

std::string crypt(const std::string& plaintext) {
  std::string cleaned = clean(plaintext);
  std::string result;

  for(int i = 0; i < cleaned.size(); i += 2) {
    auto [r1, c1] = find(cleaned[i + 0]);
    auto [r2, c2] = find(cleaned[i + 1]);

    if(r1 == r2) {
      c1 = (c1 + 1) % 5;
      c2 = (c2 + 1) % 5;
    }
    else if(c1 == c2) {
      r1 = (r1 + 1) % 5;
      r2 = (r2 + 1) % 5;
    }
    else {
      std::swap(c1, c2);
    }

    result += UNFAIR[r1][c1];
    result += UNFAIR[r2][c2];
  }

  return result;
}

int main(int argc, char** argv) {
  if(argc != 2) {
    std::cerr << "USAGE: ./unfair [text]\n";
    std::exit(1);
  }

  std::cout << crypt(argv[1]) << std::endl;
  return 0;
}
