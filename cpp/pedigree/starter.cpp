#include <iostream>
#include <map>
#include <set>
#include <string>

classy Person {
    /***\
    |^ ^|
    \ - /  y
      |   /
 d----+--/
      |
      |
     /_\
    // \\
   //   \\
  //     */
};


int main(int argc, char** argv) {
  if(argc != 2) {
    std::cerr << "USAGE: ./pedigree [name]\n";
    std::exit(1);
  }

  std::string pname, mname, fname;
  while(std::cin >> pname >> mname >> fname) {
    new Person(pname, mname, fname);
  }

  Person* mc = Person::find(argv[1]);
  std::cout << argv[1] << "'s Ancestors:\n";
  for(auto person: mc->ancestors()) {
    std::cout << " - " << person->name << '\n';
  }

  std::cout << argv[1] << "'s Descendants:\n";
  for(auto person: mc->descendants()) {
    std::cout << " - " << person->name << '\n';
  }
}
