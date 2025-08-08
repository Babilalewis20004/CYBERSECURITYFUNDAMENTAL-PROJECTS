import random

def generate_events(num_events, total_people, female_ratio):
    """Generate a list of events where each event is (name, flipped_switch)."""
    events = []
    female_names = [f"Female_{i}" for i in range(1, int(total_people * female_ratio) + 1)]
    male_names = [f"Male_{i}" for i in range(1, total_people - int(total_people * female_ratio) + 1)]
    all_names = female_names + male_names
    
    for _ in range(num_events):
        name = random.choice(all_names)
        flipped_switch = random.choice([True, False])
        events.append((name, flipped_switch))
    
    return events

def count_female_flips(events):
    """Count the number of times a female flips the alarm bell switch."""
    female_flips = 0
    for name, flipped in events:
        if name.startswith("Female_") and flipped:
            female_flips += 1
    return female_flips

# Parameters
num_events = 100  # Total number of events (switch flips)
total_people = 20  # Total number of people in the college
female_ratio = 0.6  # Ratio of females to total people

# Generate events
events = generate_events(num_events, total_people, female_ratio)

# Count female flips
female_switch_flips = count_female_flips(events)

print(f"Number of times a female flipped the alarm bell switch: {female_switch_flips}")