#include <exception>
#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <vector>

class Node {
protected:
  Operator* mParent;
  std::string mText;

public:
  Node(const std::string& text): mParent(nullptr), mText(text) {}
  virtual ~Node() {}

  virtual int precedence() const = 0;
  virtual std::ostream& write(std::ostream& stream) const = 0;

  friend std::ostream& operator << (std::ostream& stream, const Node& node) {
    return node.write(stream);
  }
};


int main(int argc, char** argv) {
  // Here be Dragons
}
