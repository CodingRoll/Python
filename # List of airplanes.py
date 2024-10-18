import random
initial_fuel = 36  
MAX_CARGO_WEIGHT = 870  
initial_fuel2 = 26400 
MAX_CARGO_WEIGHT2 = 2950 
initial_fuel3 = 27200
MAX_CARGO_WEIGHT3 = 16203 
cessna_172_specifications = {
    "Empty weight": 1205,  
    "Gross weight": 2200, 
}
Concorde_specifications = {
    "Empty weight": 203000,   
    "Gross weight": 173500,  
}
AIRBUS_A320_specifications = {
"Empty weight": 169756,  
    "Gross weight": 1421982,  
}
def calculate_fuel_usage(passenger_weight, taxiing_time, aircraft_age, weather_conditions, altitude_changes, aircraft_type, icing=False, turbulence="Light", bird_strikes=0):
    FUEL_PER_PASSENGER = 0.5  
    FUEL_PER_MINUTE_TAXIING = 0.2  
    FUEL_PER_YEAR_OLD_AGE = 2.0  
    FUEL_RAIN = 1.0 
    FUEL_SNOW = 2.0  
    FUEL_WIND = 1.5  
    FUEL_ALTITUDE_CHANGE = 0.1  
    FUEL_ICING = 3.0  
    fuel_usage = initial_fuel  
    fuel_usage += passenger_weight * FUEL_PER_PASSENGER
    fuel_usage += taxiing_time * FUEL_PER_MINUTE_TAXIING
    fuel_usage += aircraft_age * FUEL_PER_YEAR_OLD_AGE
    if weather_conditions == "rain":
        fuel_usage += FUEL_RAIN
    elif weather_conditions == "snow":
        fuel_usage += FUEL_SNOW
    elif weather_conditions == "wind":
        fuel_usage += FUEL_WIND
    elif weather_conditions == "winter" and icing:
        fuel_usage += FUEL_ICING  
    fuel_usage += altitude_changes / 1000 * FUEL_ALTITUDE_CHANGE
    if aircraft_type == "Cessna 172 Skyhawk":
        empty_weight = cessna_172_specifications["Empty weight"]
        gross_weight = cessna_172_specifications["Gross weight"]
        weight_difference = gross_weight - empty_weight
        additional_fuel = weight_difference / 303.4
        fuel_usage += additional_fuel
    
    if  aircraft_type == "Concorde":
        empty_weight = Concorde_specifications["Empty weight"]
        gross_weight = Concorde_specifications["Gross weight"]
        weight_difference = gross_weight - empty_weight
        additional_fuel = weight_difference / 9568
        fuel_usage += additional_fuel

    if  aircraft_type == "AIRBUS_A320": 
        empty_weight = Concorde_specifications["Empty weight"]
        gross_weight = Concorde_specifications["Gross weight"]
        weight_difference = gross_weight - empty_weight
        additional_fuel = weight_difference / 2720
        fuel_usage += additional_fuel
    if turbulence == "Moderate":
        fuel_usage += 2.0
    elif turbulence == "Severe":
        fuel_usage += 4.0
    fuel_usage += bird_strikes * 0.5  
    return fuel_usage
airplanes = ["Cessna 172 Skyhawk", "Concorde" , "AIRBUS_A320"]
while True:
    print("Choose an airplane:")
    for i, airplane in enumerate(airplanes, 1):
        print(f"{i}. {airplane}")
    while True:
        try:
            airplane_choice = int(input("Enter the number of your chosen airplane (1 or 2 or 3): "))
            if 1 <= airplane_choice <= 3:
                selected_airplane = airplanes[airplane_choice - 1]
                break
            else:
                print("Invalid input. Please enter 1 or 2 or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            if selected_airplane == "Cessna 172 Skyhawk":
                passenger_weight = int(input("Enter passenger and cargo weight (in pounds): "))
                if passenger_weight > MAX_CARGO_WEIGHT:
                    print("Error: Passenger and cargo weight exceeds the limit for Cessna 172 Skyhawk.")
                else:
                    break
            elif selected_airplane == "Concorde":
                passenger_weight = int(input("Enter passenger and cargo weight (in pounds): "))
                if passenger_weight > MAX_CARGO_WEIGHT2:
                    print("Error: Passenger and cargo weight exceeds the limit for Concorde.")
                else:
                    break
            elif selected_airplane == "AIRBUS_A320":
                passenger_weight = int(input("Enter passenger and cargo weight (in pounds): "))
                if passenger_weight > MAX_CARGO_WEIGHT3:
                    print("Error: Passenger and cargo weight exceeds the limit for Concorde.")
                else:
                    break
        except ValueError:
            print("Invalid input. Please enter a number.")
    taxiing_time = float(input("Enter taxiing time (in minutes): "))
    aircraft_age = int(input("Enter aircraft age (in years): "))
    weather_conditions = input("Enter weather conditions (sunny, rain, snow, wind): ").lower()
    altitude_changes = int(input("Enter altitude changes (in feet): "))
    distances = [
        "Abbotsford Airport to Price George Airport: 336.29 miles",
        "Abbotsford Airport to Wrigley Airport: 981.29 miles",
        "Abbotsford Airport to Vancouver Harbour Flight Center: 38.74 miles"
    ]
    print("\nChoose a distance option:")
    for i, distance in enumerate(distances, 1):
        print(f"{i}. {distance}")
    while True:
        try:
            distance_choice = int(input("Enter the number of your chosen distance (1, 2, or 3): "))
            if 1 <= distance_choice <= 3:
                selected_distance = distances[distance_choice - 1]
                break
            else:
                print("Invalid input. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    turbulence = random.choice(["Light", "Moderate", "Severe"])
    bird_strikes = random.randint(0, 1)  
    print(f"Turbulence: {turbulence}")
    print(f"Bird Strikes: {bird_strikes}")
    used_fuel = calculate_fuel_usage(passenger_weight, taxiing_time, aircraft_age, weather_conditions, altitude_changes, selected_airplane, False, turbulence, bird_strikes)
    if selected_airplane == "Cessna 172 Skyhawk" and used_fuel > initial_fuel:
        print("Error: Not enough fuel for this flight.")
    elif selected_airplane == "Concorde" and used_fuel > initial_fuel2:
        print("Error: Not enough fuel for this flight.")
    elif selected_airplane == "AIRBUS_A320" and used_fuel > initial_fuel3:
        print("Error: Not enough fuel for this flight.")
    else:
        print(f"\nYou selected the {selected_airplane}")
    print(f"Fuel used for the flight: {used_fuel:.2f} gallons")
    choice = input("Do you want to choose another airplane (y/n)? ").strip().lower()
    if choice != "y":
        break