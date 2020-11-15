import Foundation

struct DateInfo {
  let month:   String
  let weekday: String
  let day:     Int
}

func parse(text: String) -> DateInfo {
  // Yesterday...
}

func reply(date: DateInfo) {
  // ...all my troubles seemed so far away...
}


if CommandLine.arguments.count != 2 {
  print("USAGE: ./bandate [date]")
  exit(1)
}

let date = parse(text: CommandLine.arguments.last!)
reply(date: date)
