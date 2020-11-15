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

fn find<'a, 'b>(tape: &String, reps: &'b Vec<Replacement>) -> Vec<Match<'a, 'b>> {
  let mut mats: Vec<Match> = vec![];

  for rep in reps {
    let mut part: &str = tape;
    let mut sum: usize = 0;

    loop {
      match part.find(rep.src) {
        None      => break,
        Some(pos) => {
          mats.push(Match{rep: rep, pos: pos + sum});
          part = &part[pos+1..];
          sum += pos + 1;
        }
      }
    }
  }

  return mats
}

fn rand(state: u64) -> u64 {
  let mut next = state;
  next ^= next << 13;
  next ^= next >>  7;
  next ^= next << 17;
  return next;
}

fn step(tape: &mut String, mat: &Match) {
  let rng = mat.pos .. mat.pos + mat.rep.src.len();
  tape.replace_range(rng, &mat.rep.dst);
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

  for arg in &args[4..] {
    let pair: Vec<&str> = arg.split(':').collect();
    if pair.len() != 2 {
      println!("Invalid pair: {}", arg);
      process::exit(1);
    }

    reps.push(Replacement{
      src: &pair[0],
      dst: &pair[1]
    })
  }

  for _ in  0..itrs {
    println!("{}", tape);

    let mats = find(&tape, &reps);
    let mlen = mats.len() as u64;
    if mlen == 0 {
      process::exit(0);
    }

    seed = rand(seed);
    let mat = &mats[(seed as usize) % mats.len()];
    step(&mut tape, mat);

    itrs -= 1;
  }

  println!("{}", tape);
}
