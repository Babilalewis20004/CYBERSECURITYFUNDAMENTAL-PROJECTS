import os
import re
from datetime import datetime
import matplotlib.pyplot as plt

# Initialize the dictionary with Event IDs as keys and 0 as values
event_ids = {
    1102: 0, 4611: 0, 4624: 0, 4634: 0, 4648: 0, 4661: 0, 4662: 0, 4663: 0,
    4672: 0, 4673: 0, 4688: 0, 4698: 0, 4699: 0, 4702: 0, 4703: 0, 4719: 0,
    4732: 0, 4738: 0, 4742: 0, 4776: 0, 4798: 0, 4799: 0, 4985: 0, 5136: 0,
    5140: 0, 5142: 0, 5156: 0, 5158: 0
}

# Function to process the log file and update event_ids dictionary
def process_log_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            match = re.search(r'MATCHED Event ID:\s*(\d+)', line)
            if match:
                event_id = int(match.group(1))
                if event_id in event_ids:
                    event_ids[event_id] += 1

# Function to save the event_ids dictionary to a log file
def save_log_file():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_dir = "CI5235_K2365461_Lewis/CI5235_logs/"
    os.makedirs(log_dir, exist_ok=True)
    log_file_path = os.path.join(log_dir, f"visdata_log_{timestamp}.txt")
    
    with open(log_file_path, 'w') as log_file:
        for event_id, count in event_ids.items():
            log_file.write(f"Event ID {event_id}: {count}\n")
            print(f"Event count {count}")
            print (f"Event ID {event_id} \n")
            
    
    return log_file_path

# Function to read the log file and create lists for Event IDs and their counts
def read_log_file(log_file_path):
    event_id_list = []
    event_id_count_list = []
    
    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            match = re.search(r'Event ID (\d+): (\d+)', line)
            if match:
                event_id_list.append(int(match.group(1)))
                event_id_count_list.append(int(match.group(2)))
    
    return event_id_list, event_id_count_list

# Main function to execute the script
def main():
    log_file_path = "C:/Users/User/Desktop/analysis_log_02_Jan_2020.txt"
    
    print("Processing log file...")
    print(process_log_file(log_file_path))
    
    print("Saving log file...")
    saved_log_file_path = save_log_file()
    print(saved_log_file_path)
    
    print("Reading log file...")
    event_id_list, event_id_count_list = read_log_file(saved_log_file_path)

if __name__ == "__main__":
    main()
import matplotlib.pyplot as plt

# Data provided by the user
event_data = {
    "Event ID 1102": 15,
    "Event ID 4611": 2,
    "Event ID 4624": 46,
    "Event ID 4634": 1,
    "Event ID 4648": 6,
    "Event ID 4661": 19,
    "Event ID 4662": 33,
    "Event ID 4663": 114,
    "Event ID 4672": 12,
    "Event ID 4673": 2,
    "Event ID 4688": 35,
    "Event ID 4698": 2,
    "Event ID 4699": 2,
    "Event ID 4702": 4,
    "Event ID 4703": 1,
    "Event ID 4719": 8,
    "Event ID 4732": 2,
    "Event ID 4738": 5,
    "Event ID 4742": 4,
    "Event ID 4776": 7,
    "Event ID 4798": 2,
    "Event ID 4799": 1,
    "Event ID 4985": 2,
    "Event ID 5136": 42,
    "Event ID 5140": 6,
    "Event ID 5142": 1,
    "Event ID 5156": 92,
    "Event ID 5158": 14
}

# Extracting keys and values from the dictionary
event_ids = list(event_data.keys())
event_counts = list(event_data.values())

# Plotting the horizontal bar graph
plt.figure(figsize=(10,8))
plt.barh(event_ids, event_counts, color='red')
plt.xlabel('Event Count')
plt.ylabel('Event IDs')
plt.title('Horizontal Bar Graph of Event Counts')
plt.tight_layout()

# Save the plot as a PNG file
plt.savefig("event_counts_horizontal_bar_graph.png")

# Display the plot
plt.show()