import random

input_seconds = int (random.randint(1, 1000))
print(f"Random seconds {input_seconds}")
hours = input_seconds // 3600
seconds_after_hours = input_seconds % 3600
minutes = seconds_after_hours // 60
seconds = seconds_after_hours % 60
print(f"Hours {hours} Minutes {minutes} Seconds {seconds}")