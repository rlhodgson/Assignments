def get_circumference():
    """Gets circum"""
    circumference = float(input("Circumference (m)? "))
    return circumference

def get_times():
    """Gets time"""
    times_string = input("Times (msecs, space separated)? ")
    times_list = times_string.split()
    times = [] # In seconds
    for time_string in times_list:
        times.append(int(time_string) / 1000)
    return times

def get_speed(circum, times):
    """Gets speeds"""
    speeds = []
    for i in range(len(times) - 1):
        speed_m_per_s = circum / ((times[i + 1] - times[i]))
        speeds.append(speed_m_per_s)
    return speeds

def print_info(speeds, times):
    """Prints stuff"""
    print("Time (s)  Speed (m/s)")
    for i in range(0, len(speeds)):
        print("{:6.2f}  {:9.2f}".format(times[i], speeds[i]))
    
def main():
    """Runs the program"""
    circum = get_circumference()
    times = get_times()
    speeds = get_speed(circum, times)
    print_info(speeds, times)
    
main()