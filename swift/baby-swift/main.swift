func setup() -> Set<String> {
  var hotdogs = Set<String>()
  hotdogs.insert("🌭")
  hotdogs.insert("HOTDOG")
  hotdogs.insert("HOT DOG")
  hotdogs.insert("HOT-DOG")
  hotdogs.insert("SAUSAGE")
  hotdogs.insert("BRATWURST")
  hotdogs.insert("FRANKFURTER")
  hotdogs.insert("POLISH SAUSAGE")
  return hotdogs
}

func query() -> String {
  print("What do you have there?")
  return readLine()!
}

func clean(_ input: String) -> String {
  var cleaned = input.uppercased()

  if(cleaned.starts(with: "A ")) {
    cleaned.removeFirst(2)
  }
  else if(cleaned.starts(with: "THE ")) {
    cleaned.removeFirst(4)
  }

  return cleaned
}

let hotdogs = setup()
let found   = clean(query())
if(hotdogs.contains(found)) {
  print("HOTDOG")
}
else {
  print("NOT HOTDOG")
}
