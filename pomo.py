import argparse
import time

def main():
  parser = argparse.ArgumentParser("a timer for you little terminal")
  parser.add_argument("study_time", help="how long do you want the study session to be")
  parser.add_argument("break_time", help="how long do you want the breaks to be")
  parser.add_argument("long_break", help="how long do you want the breaks to be after 4 study sessions")
  parser.add_argument("sessions", help="how many study sessions do you want to do")

  args = parser.parse_args()

  print(args.study_time, args.break_time, args.sessions)

  for c in range(int(args.sessions)):
    print("study")
    for s in range(int(args.study_time) * 60):
      time.sleep(1)
      print(s)

    print("break")
    break_time = args.break_time if int(args.sessions) % 4 != 0 else args.long_break
    for s in range(int(break_time) * 60):
      time.sleep(1)
      print(s)
    

if __name__ == "__main__":
  main()