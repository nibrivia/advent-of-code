from aoc_helpers import *
import parse
records_str = get_input(4)

def event_parse(event_str):
    event = dict()
    if "Guard" in event_str:
        event["type"] = "guard"
        event["value"] = parse.parse("Guard #{:d} begins shift", event_str)[0]
        return event
    if "falls" in event_str:
        event["type"] = "sleep"
        return event
    if "wakes" in event_str:
        event["type"] = "wake"
        return event


def records_parse(records_str):
    parser = parse.compile("[{} {}:{:d}] {:event}", dict(event=event_parse))

    guard      = None
    sleep_time = None
    sleep_log = []

    # Sorting on the string puts in chronological order :)
    for r in sorted(records_str):
        day, hour, minute, event = parser.parse(r)

        if event["type"] == "guard":
            guard = event["value"]
        if event["type"] == "sleep":
            sleep_time = minute
        if event["type"] == "wake":
            sleep_entry = (guard, sleep_time, minute)
            sleep_log.append(sleep_entry)

    return sleep_log

def dict_key(entry):
    key, value = entry
    return value

records = records_parse(records_str)

sleep_totals = dict()
for guard, sleep, wake in records:
    duration = wake-sleep
    sleep_totals[guard] = sleep_totals.get(guard, 0) + duration

sleepiest_guard = sorted(sleep_totals.items(), key = dict_key)[-1][0]

minutes_freq = dict()
for guard, sleep, wake in records:
    for minute in range(sleep, wake):
        key = (guard, minute)
        minutes_freq[key] = minutes_freq.get(key, 0) + 1


# Just the sleepiest guard
sleepiest_guard_minutes = {minute: count for (guard, minute), count in minutes_freq.items() if guard == sleepiest_guard}
sleepiest_guard_minute = sorted(sleepiest_guard_minutes.items(), key = dict_key)[-1][0]
print(sleepiest_guard_minute * sleepiest_guard)

# All of them
guard, minute = sorted(minutes_freq.items(), key = dict_key)[-1][0]
print(guard*minute)
