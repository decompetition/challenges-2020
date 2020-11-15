#include <algorithm>
#include <functional>
#include <iomanip>
#include <iostream>
#include <string>
#include <vector>

// Example mangled lambda name:
// _ZZZ4mainENKUlvE5_clEvENKUlP4BeerE_clES1_

// Lambda patterns:
// _ZZ4mainENKUl*
// _ZZZ4mainENKUl*

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

  auto choose = [&]() {
    std::cout << "> ";
    std::cin >> choice;

    if(std::cin.eof()) {
      std::cout << '\n';
      std::exit(2);
    }
    else {
      std::cin.clear();
      std::cin.ignore(100, '\n');
    }

    return choice;
  };

  auto beerror = []() {
    std::cout << "That's not an option.\n";
  };

  auto list_beers = [&]() {
    int index = 1;
    std::for_each(beers.begin(), beers.end(), [&](Beer* beer) {
      std::cout << std::setw(4) << index++
                << ") A " << beer->age << "-week-old " << beer->type
                << " called " << beer->name << ".\n";
    });
  };

  std::function<Beer*()> pick_a_beer = [&]() -> Beer* {
    std::cout << "Choose a beer:\n";
    list_beers();

    auto choice = choose();
    if(choice > 0 && choice <= beers.size()) {
      return beers[choice - 1];
    }

    beerror();
    return pick_a_beer();
  };

  std::function<std::string()> pick_a_type = [&]() {
    std::cout << "What sort of beer is this?\n";
    for(size_t i = 0; i < types.size(); ++i) {
      std::cout << std::setw(4) << (i+1) << ") " << types[i] << '\n';
    }

    choose();
    if(choice > 0 && choice <= types.size()) {
      return types[choice - 1];
    }

    beerror();
    return pick_a_type();
  };

  auto pick_a_name = []() {
    std::string name;
    std::cout << "What's this beer called?\n> ";
    std::getline(std::cin, name);
    return name;
  };

  auto customize_beer = [&](Beer* beer) {
    beer->type = pick_a_type();
    beer->name = pick_a_name();
    beer->age  = 0;

    std::cout << "You brew up a " << beer->type
              << " called " << beer->name << ".\n";
  };

  auto age_beers = [&]() {
    std::cout << "A week goes by...\n\n";
    std::for_each(beers.begin(), beers.end(), [](Beer* beer) {
      beer->age += 1;
    });
  };

  auto sell_beer = [&](Beer* beer) {
    std::cout << "You sell your " << beer->name << ' ' << beer->type
              << " for $" << (900 + 100 * beer->age) << ".\n";

    auto itr = std::find(beers.begin(), beers.end(), beer);
    beers.erase(itr);
    delete beer;
  };

  auto leave_the_beerery = []() {
    std::cout << "And one for the road!\n";
    std::exit(0);
  };

  auto beer_menu = [&]() -> std::function<void()> {
    std::cout << "What would you like to do this week?\n";
    std::cout << "   1) Create a Beer\n";
    std::cout << "   2) View your Beers\n";
    std::cout << "   3) Sell a Beer\n";
    std::cout << "   4) Drink some Beer\n";
    std::cout << "   5) Exit\n";
    auto choice = choose();

    if(choice > 0 && choice < 6) {
      if(choice == 1) {
        auto beer = new Beer();
        beers.push_back(beer);
        return std::bind(customize_beer, beer);
      }
      else if(choice == 5) {
        return leave_the_beerery;
      }

      if(beers.size() < 1) {
        return []() {
          std::cout << "There's no beer here :(\n";
        };
      }

      if(choice == 2) {
        return [&]() {
          std::cout << "In the cellar you find:\n";
          list_beers();
        };
      }
      else if(choice == 3) {
        Beer* beer = pick_a_beer();
        return std::bind(sell_beer, beer);
      }
      else if(choice == 4) {
        return [](){};
      }
    }

    return []() {
      std::cout << "Go home. You're drunk.\n";
      std::exit(1);
    };
  };

  std::cout << "Welcome to the Beerery!\n";
  while(true) {
    beer_menu()();
    age_beers();
  }
}
