use std::env;

fn main() {
  if let Some(arg1) = env::args().nth(1) {
    print!("Thanks");
    match arg1.parse::<i32>() {
      Ok(n) => print!(", {} could be a number", n),
      Err(_e) => print!(". This was unexpected"),
    }
    print!("\n");
  }
  else {
    println!("Please provide an argument")
  }
}
