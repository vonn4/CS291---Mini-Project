import pandas as pd
import random

# Load the CSV file into a DataFrame
file_path = r"C:\Users\ethan\Downloads\archive (4)\flights.csv"
df = pd.read_csv(file_path)

# Filter for the specified year/month
filtered_df = df[df['Fly Date'] == 200912] 

# Verify columns for connections
if 'Origin' not in filtered_df.columns or 'Destination' not in filtered_df.columns:
    raise ValueError("The dataset must have 'Origin' and 'Destination' columns for flight connections.")

# Start with a random initial flight
initial_flight = filtered_df.sample(n=1, random_state=42)
connected_flights = [initial_flight.iloc[0]]  # Initialize with the first flight
visited_destinations = {initial_flight.iloc[0]['Destination']}  # Track visited destinations

# Build a densely connected network
while len(connected_flights) < 50:
    # Get all potential flights that connect from any destination in visited destinations
    next_flight_options = filtered_df[filtered_df['Origin'].isin(visited_destinations)]
    
    # Remove flights that are already included in the connected flights to avoid cycles
    #next_flight_options = next_flight_options[~next_flight_options.index.isin([f.name for f in connected_flights])]

    # If no options remain, stop
    if next_flight_options.empty:
        print("No further connecting flights found, stopping early.")
        break

    # Randomly select the next flight to add variety
    next_flight = next_flight_options.sample(n=1, random_state=random.randint(1, 100))
    connected_flights.append(next_flight.iloc[0])

    # Update visited destinations to include this new flight's destination
    visited_destinations.add(next_flight.iloc[0]['Destination'])

# Convert to DataFrame
sample_connected_df = pd.DataFrame(connected_flights)

# Save the sample to a new CSV file
output_file_path = r"C:\Users\ethan\Downloads\archive (4)\sampleflights3.csv"
sample_connected_df.to_csv(output_file_path, encoding='utf-8', index=False)

print("Sample of densely connected flights saved to:", output_file_path)
