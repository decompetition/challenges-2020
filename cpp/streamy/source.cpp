#include <exception>
#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <vector>

std::map<std::string, int> PRECEDENCE {
  {"+", 1},
  {"-", 1},
  {"*", 2},
  {"/", 2},
  {"%", 2},
  {"^", 3}
};

std::map<std::string, int> ASSOCIATIVITY {
  {"-", 1},
  {"/", 1},
  {"%", 1},
  {"^", 0}
};

class Operator;

class Node {
protected:
  Operator* mParent;
  std::string mText;

protected:
  Node* reparent(Operator* parent) {
    mParent = parent;
    return this;
  }

public:
  Node(const std::string& text): mText(text) {
    mParent = nullptr;
  }

  virtual ~Node() {
    // Nothing to do.
  }

  virtual int precedence() const = 0;
  virtual std::ostream& write(std::ostream& stream) const = 0;

  friend std::ostream& operator << (std::ostream& stream, const Node& node) {
    return node.write(stream);
  }

  friend class Operator;
};

class Number: public Node {
public:
  Number(const std::string& text): Node(text) {
    // That is all.
  }

  int precedence() const {
    return 0;
  }

  std::ostream& write(std::ostream& stream) const {
    return stream << mText;
  }
};

class Operator: public Node {
private:
  Node* mOps[2];

private:
  std::string paren(std::string text) const {
    if(mParent) {
      int pprec = mParent->precedence();
      int cprec = precedence();

      if(pprec > cprec) {
        return text;
      }

      if(pprec == cprec && ASSOCIATIVITY.count(mText)) {
        int assoc = ASSOCIATIVITY[mText];
        if(mParent->mOps[assoc] == this) {
          return text;
        }
      }
    }

    return "";
  }

public:
  Operator(const std::string& text, Node* lhs, Node* rhs): Node(text) {
    mOps[0] = lhs->reparent(this);
    mOps[1] = rhs->reparent(this);
  }

  ~Operator() {
    delete mOps[0];
    delete mOps[1];
  }

  int precedence() const {
    return PRECEDENCE[mText];
  }

  std::ostream& write(std::ostream& stream) const {
    return stream << paren("(") << *mOps[0] << ' ' << mText << ' ' << *mOps[1] << paren(")");
  }
};

std::istream& get_istream(int argc, char** argv) {
  if(argc < 2 || argv[1] == std::string("-")) return std::cin;
  else return *new std::ifstream(argv[1]);
}

std::ostream& get_ostream(int argc, char** argv) {
  if(argc < 3 || argv[2] == std::string("-")) return std::cout;
  else return *new std::ofstream(argv[2]);
}

int main(int argc, char** argv) {
  std::istream& inn = get_istream(argc, argv);
  std::ostream& oot = get_ostream(argc, argv);

  std::string line;
  while(std::getline(inn, line)) {
    std::istringstream iss(line);
    std::vector<Node*> stack;

    try {
      std::string token;
      while(iss >> token) {
        if(PRECEDENCE.count(token)) {
          if(stack.size() < 2) {
            throw std::underflow_error("Not enough operands.");
          }

          Node* rhs = stack.back();
          stack.pop_back();

          Node* lhs = stack.back();
          stack.pop_back();

          stack.push_back(new Operator(token, lhs, rhs));
        }
        else {
          char* end = nullptr;
          std::strtol(token.c_str(), &end, 0);
          if(*end != '\0') {
            throw std::runtime_error("Unknown token.");
          }

          stack.push_back(new Number(token));
        }
      }

      if(stack.size() == 1) {
        oot << *stack.back() << std::endl;
      }
      else {
        throw std::overflow_error("Too many operands.");
      }
    }
    catch(std::exception& e) {
      oot << "INVALID: " << e.what() << std::endl;
    }

    for(auto node: stack) {
      delete node;
    }
  }

  oot.flush();
}
