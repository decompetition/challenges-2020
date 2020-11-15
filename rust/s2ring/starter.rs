use std::env;
use std::process;

struct Replacement<'a> {
  src: &'a str,
  dst: &'a str
}

struct Match<'a, 'b> {
  rep: &'a Replacement<'b>,
  pos: usize
}

fn main() {
  let args: Vec<String> = env::args().collect();
  if args.len() < 5 {
    println!("USAGE: {} [seed] [tape] [iters] [src:dst ...]", &args[0]);
    process::exit(1);
  }

  let mut seed = args[1].parse::<u64>().expect("Seed must be a number.");
  let mut itrs = args[3].parse::<u64>().expect("Iters must be a number.");
  let mut tape = String::from(&args[2]);
  let mut reps: Vec<Replacement> = vec![];

  // load

  // find
  // rand
  // step
  // loop
}
