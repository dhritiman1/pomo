import argparse
import time


def timer(mint):
    for s in range(mint * 60):
        mins, secs = divmod(s, 60)
        time.sleep(1)
        print(
            f"\r{"0" + str(mins) if mins < 10 else mins}m:{"0" + str(secs) if secs < 10 else secs}s",
            end="",
        )


def main():
    parser = argparse.ArgumentParser("a timer for you little terminal")
    parser.add_argument(
        "study_time", help="how long do you want the study session to be"
    )
    parser.add_argument("break_time", help="how long do you want the breaks to be")
    parser.add_argument(
        "long_break",
        help="how long do you want the breaks to be after 4 study sessions",
    )
    parser.add_argument("sessions", help="how many study sessions do you want to do")

    args = parser.parse_args()

    for c in range(int(args.sessions)):
        print("\n\nstudy")
        timer(int(args.study_time))

        print("\nbreak")
        if c % 4 != 0:
            timer(int(args.break_time))
        else:
            timer(int(args.long_break))


if __name__ == "__main__":
    main()
