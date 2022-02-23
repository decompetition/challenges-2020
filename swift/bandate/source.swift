import Foundation

struct DateInfo {
  let month:   String
  let weekday: String
  let day:     Int
}

func parse(text: String) -> DateInfo {
  let formatter = DateFormatter()
  formatter.dateFormat = "yyyy-MM-dd"
  let date = formatter.date(from: text)!

  let calendar = Calendar(identifier: .gregorian)
  let m = calendar.component(.month,   from: date)
  let w = calendar.component(.weekday, from: date)
  let d = calendar.component(.day,     from: date)

  return DateInfo(
    month:   formatter.monthSymbols[m-1],
    weekday: formatter.weekdaySymbols[w-1],
    day:     d
  )
}

func reply(date: DateInfo) {
  print("That's a " + date.weekday + " in " + date.month + ".")

  if date.month == "February" && date.day == 25 {
    print("It's George's birthday!")
  }
  else if date.month == "June" {
    if date.day == 18 {
      print("It's Paul's birthday!")
    }
    else if date.day == 23 {
      print("It's Stuart's birthday!")
    }
    else {
      print("June is a good month.")
    }
  }
  else if date.month == "July" && date.day == 7 {
    print("It's Ringo's birthday!")
  }
  else if date.month == "October" && date.day == 9 {
    print("It's John's birthday!")
  }
  else if date.month == "November" && date.day == 24 {
    print("It's Pete's birthday!")
  }
  else {
    print("What a boring day.")
  }
}


if CommandLine.arguments.count != 2 {
  print("USAGE: ./bandate [date]")
  exit(1)
}

let date = parse(text: CommandLine.arguments.last!)
reply(date: date)
