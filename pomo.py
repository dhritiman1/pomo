import argparse
import datetime
import os
import time


def read_stats():
    stats = {}
    with open("stats.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            date, count = line.split(",")
            stats[date] = int(count)

    return stats


def write_stats(stats):
    with open("stats.txt", "w") as f:
        for date, time in stats.items():
            f.write(f"{date},{time}")


def update_stats(count):
    today = datetime.datetime.today().strftime("%Y-%m-%d")
    stats = read_stats()

    if today in stats:
        stats[today] += count
    else:
        stats[today] = count

    write_stats(stats)


def timer(mint):
    try:
        for s in range(mint * 60):
            mins, secs = divmod(s, 60)
            mins = "0" + str(mins) if mins < 10 else mins
            secs = "0" + str(secs) if secs < 10 else secs
            time.sleep(1)
            print(f"\r{mins}m:{secs}s", end="")
    except KeyboardInterrupt as k:
        print("\ntimer stopped")
        raise
    print()


def main():
    parser = argparse.ArgumentParser("a timer for you little terminal")
    parser.add_argument(
        "study_time", type=int, help="how long do you want the study session to be"
    )
    parser.add_argument(
        "break_time", type=int, help="how long do you want the breaks to be"
    )
    parser.add_argument(
        "long_break",
        type=int,
        help="how long do you want the breaks to be after 4 study sessions",
    )
    # parser.add_argument("sessions", help="how many study sessions do you want to do")

    args = parser.parse_args()

    count = 0

    if not os.path.exists("stats.txt"):
        with open("stats.txt", "w") as f:
            f.write("")

    try:
        while count <= 12:
            print("\nstudy")
            timer(args.study_time)

            count += 1

            print("\nbreak")
            if count % 4 != 0:
                timer(args.break_time)
            else:
                timer(args.long_break)

            update_stats(count)

        
        print(f"today you completed {count} successful pomodoro!")

    except KeyboardInterrupt:
        update_stats(count)
        print(f"Today's final count: {count} Pomodoros completed.")


if __name__ == "__main__":
    main()
