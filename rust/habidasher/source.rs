use std::env;
use std::num::Wrapping;
// http://www.cse.yorku.ca/~oz/hash.html

fn foo(input: &str) -> u32 {
  let mut hash = Wrapping(0u32);
  for c in input.chars() {
    hash = (hash << 16) + (hash << 6) + Wrapping(c as u32) - hash;
  }

  return hash.0
}

fn bar(input: &str) -> u32 {
  let mut hash = Wrapping(5381u32);
  for c in input.chars() {
    hash = (hash << 5) + hash + Wrapping(c as u32);
  }

  return hash.0
}

fn main() {
  match env::args().nth(1) {
    None    => println!("USAGE: ./habidasher [input]"),
    Some(s) => {
      println!("djb2: {:08x}", bar(&s));
      println!("sdbm: {:08x}", foo(&s));
    }
  }
}
