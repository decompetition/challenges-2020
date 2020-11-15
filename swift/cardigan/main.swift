import Foundation

struct Static {
  static var txt = Array(
    "Qg-\"eq|s/ohI{'$nRVp;M1}" +
    "wGB@(52=J`^C!E0tPi>:Y+~y" +
    "HfS\\OZlm4D<.cTrK]?FLj)," +
    "k3a&*bN#d%U8[6XWxz9uvA_7"
  )

  static var map = [
    ("5019", "oBKwD$W"),
    ("6011", "ozm{DYO$"),
    ("6040", "^w$8B$J"),
    ("6041", "^w$8B$J"),
    ("6500", "?O$YO"),
    ("6521", "]:xB7"),
    ("6522", "]:xB7"),
    ("9792", "'$D7"),
    ("506",  "?O$YO"),
    ("30",   "ozKO$m 8|:5"),
    ("31",   "'S^KzDK"),
    ("34",   "+sO$z{BK 6PF$Omm"),
    ("35",   "d8a"),
    ("36",   "ozKO$m 8|:5"),
    ("37",   "+sO$z{BK 6PF$Omm"),
    ("38",   "ozKO$m 8|:5"),
    ("39",   "ozKO$m 8|:5"),
    ("60",   "]:xB7"),
    ("62",   "^KzDKxB7"),
    ("64",   "ozm{DYO$"),
    ("65",   "ozm{DYO$"),
    ("81",   "^KzDKxB7"),
    ("1",    "^+'x"),
    ("4",    "?zmB"),
    ("5",    "jBmWO${B$J"),
  ]
}

func types(_ input: String) -> String? {
  for (pfx, name) in Static.map {
    if input.starts(with: pfx) {
      return name
    }
  }

  return nil
}

func check(_ input: String) -> Bool {
  let len: Int = input.length
  var mul: Int = 2 - len % 2
  var sum: Int = 0

  if len < 12 || len > 19 {
    return false
  }

  for char in input {
    var val = Int(char.asciiValue!) - 0x30
    if val < 0 || val > 9 {
      return false
    }

    val *= mul
    sum += val / 10
    sum += val % 10
    mul ^= 3
  }

  return (sum % 10 == 0)
}

var rot = [Character:Character]()
for i in 0 ..< 94 {
  rot[Static.txt[i]] = Static.txt[(i + 94 / 2) % 94]
}

// ROT-94 all the card company names:
// for (pfx, name) in Static.map {
//   print(pfx, String(name.map {rot[$0] ?? $0}))
// }

print("Thirteen sweaters @ $35.95: $467.35")
print("Enter payment: ", terminator: "")
let input = readLine()!

if(check(input)) {
  var type = types(input)
  if type != nil {
    type = String(type!.map {rot[$0] ?? $0})
    print(type! + " payment accepted.")
    exit(0)
  }
  else {
    print("ERROR: Unrecognized PAN.")
  }
}
else {
  print("ERROR: Invalid input.")
}

print("Try your cardigan.")
