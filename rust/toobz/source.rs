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


struct TSuck {
  sucker: net::TcpListener
}

impl TSuck {
  pub fn new(port: &str) -> TSuck {
    let addr = "127.0.0.1:".to_owned() + port;
    TSuck{sucker: net::TcpListener::bind(addr).unwrap()}
  }
}

impl Suck for TSuck {
  fn suck(&self) -> String {
    let (mut stream, _) = self.sucker.accept().unwrap();

    let mut buffer = String::new();
    stream.read_to_string(&mut buffer).unwrap();
    return buffer;
  }
}


struct TSpew {
  target: String
}

impl TSpew {
  pub fn new(port: &str) -> TSpew {
    TSpew{target: "127.0.0.1:".to_owned() + port}
  }
}

impl Spew for TSpew {
  fn spew(&self, what: &str) {
    let mut stream = net::TcpStream::connect(&self.target).unwrap();
    stream.write(what.as_bytes()).unwrap();
  }
}


struct ISuck {
  // Nothing to see here.
}

impl ISuck {
  pub fn new(_: &str) -> ISuck {
    ISuck{}
  }
}

impl Suck for ISuck {
  fn suck(&self) -> String {
    let mut buffer = String::new();
    std::io::stdin().read_to_string(&mut buffer).unwrap();
    return buffer
  }
}


struct ISpew {
  // Nothing to see here.
}

impl ISpew {
  pub fn new(_: &str) -> ISpew {
    ISpew{}
  }
}

impl Spew for ISpew {
  fn spew(&self, what: &str) {
    print!("{}", what);
  }
}


fn new_suck(arg: &str) -> Box<dyn Suck> {
  if arg == "-" {
    return Box::new(ISuck::new(arg))
  } else {
    return Box::new(TSuck::new(arg))
  }
}

fn new_spew(arg: &str) -> Box<dyn Spew> {
  if arg == "-" {
    return Box::new(ISpew::new(arg))
  } else {
    return Box::new(TSpew::new(arg))
  }
}


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
