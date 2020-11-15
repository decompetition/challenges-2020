#include <algorithm>
#include <functional>
#include <iomanip>
#include <iostream>
#include <string>
#include <vector>

struct Beer {
  std::string name;
  std::string type;
  int age;
};

int main() {
  size_t choice;
  std::vector<Beer*> beers;
  std::vector<std::string> types {
    "Belgian",
    "Gruit",
    "Lager",
    "Lambic",
    "Pale Ale",
    "Porter",
    "Stout",
    "Witbier"
  };

   /*
    \\
     \\
    //\\
   //  \\
  //    */

  std::cout << "Welcome to the Beerery!\n";
  while(true) {
    beer_menu()();
    age_beers();
  }
}
