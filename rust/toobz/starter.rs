use std::env;
use std::io::Read;
use std::io::Write;
use std::net;

trait Suck {
  fn suck(&self) -> String;
}

trait Spew {
  fn spew(&self, what: &str);
}

// A seriez...
// ...of toobz.

fn main() {
  let mut sucks: Vec<String> = vec!["-".to_string()];
  let mut spews: Vec<String> = vec![];

  for arg in env::args().skip(1) {
    sucks.push(arg.clone());
    spews.push(arg.clone());
  }

  spews.push("-".to_string());

  let pairs = sucks.iter().zip(spews.iter());
  let threads: Vec<_> = pairs.map(|(su, sp)| {
    let su2 = su.clone();
    let sp2 = sp.clone();

    return std::thread::spawn(move || {
      let suck = new_suck(&su2);
      let spew = new_spew(&sp2);
      spew.spew(&suck.suck());
    })
  }).collect();

  for thread in threads {
    thread.join().unwrap();
  }
}
