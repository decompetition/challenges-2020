#include <iostream>
#include <map>
#include <set>
#include <string>

// _ZN6PersonC2ERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEES7_S7_
// _ZNK6Person9ancestorsEv
// _ZNK6Person11descendantsEv
// _ZN6Person4findERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE

class Person {
public:
  std::string       name;
  Person*           mother;
  Person*           father;
  std::set<Person*> children;

public:
  Person(const std::string& name, const std::string& mname, const std::string& fname) {
    this->name   = name;
    this->mother = find(mname);
    this->father = find(fname);

    if(this->mother) {
      this->mother->children.insert(this);
    }

    if(this->father) {
      this->father->children.insert(this);
    }

    ALL[name] = this;
  }

  std::set<Person*> ancestors() const {
    std::set<Person*> result;
    if(mother) {
      result.merge(mother->ancestors());
      result.insert(mother);
    }

    if(father) {
      result.merge(father->ancestors());
      result.insert(father);
    }

    return result;
  }

  std::set<Person*> descendants() const {
    std::set<Person*> result = children;
    for(auto child: children) {
      result.merge(child->descendants());
    }

    return result;
  }

public:
  static std::map<std::string, Person*> ALL;
  static Person* find(const std::string& name) {
    auto itr = ALL.find(name);
    if(itr == ALL.end()) {
      std::cerr << "Unknown person: " << name << '\n';
      std::exit(2);
    }

    return itr->second;
  }
};

std::map<std::string, Person*> Person::ALL{{"???", nullptr}};


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
