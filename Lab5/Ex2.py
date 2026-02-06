trip_durations = [1.1, 0.8, 2.5, 2.6]
trip_fares = (6.25, 5.25, 10.50, 8.05)

taxiTrips = {
    "miles": trip_durations,
    "fares": trip_fares    
}

print(taxiTrips)

print(f"The third trip was {taxiTrips['miles'][2]} miles long.")
print(f"The fare for the first trip was ${taxiTrips['fares'][0]:.2f}.")

