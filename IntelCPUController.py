import os, time

def average_clock_speed(settingsHZ):
    Core_Clocks = os.popen("cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_cur_freq").read().split("\n")
    Core_Clocks.pop()
    Core_Clocks = list(map(int, Core_Clocks))
    Core_Count = len(Core_Clocks)
    if settingsHZ == "MHz":
        print("Current average clock speed is: " + str(round(sum(Core_Clocks) / int(Core_Count) / 1000)) + " MHz")
    elif settingsHZ == "GHz":
        print("Current average clock speed is: " + str(round(sum(Core_Clocks) / int(Core_Count) / 1000000, 2)) + " GHz")
    else:
        print("unexpected error!")

def check_intel_turbo_boost():
    if os.popen('cat /sys/devices/system/cpu/intel_pstate/no_turbo').read().split("\n").pop(0) == "0":
        print("intel ")
    

def clock_speed_control(clockpercent):
    os.popen('echo 1 | sudo tee /sys/devices/system/cpu/intel_pstate/no_turbo').read()

while True:
    os.system("sudo clear")
    print("Choose between 1-3:\n1. CPU Watchtower\n2. Change Clock Speed")
    if os.popen('cat /sys/devices/system/cpu/intel_pstate/no_turbo').read().split("\n").pop(0) == "0":
        print("3. Toggle Intel Turbo Boost - [Enabled]")
        itb_enabled = 1
    elif os.popen('cat /sys/devices/system/cpu/intel_pstate/no_turbo').read().split("\n").pop(0) == "1":
        itb_enabled = 0
        print("3. Toggle Intel Turbo Boost - [Disabled]")
    choice = int(input())
    if choice == 1:
        while True:
            os.system("clear")
            average_clock_speed("GHz")
            time.sleep(3)
    if choice == 2:
        os.popen('echo '+ input("Enter maximum allowed CPU frequency (in percent, between 0-100)\n") +' | sudo tee /sys/devices/system/cpu/intel_pstate/max_perf_pct').read()
    if choice == 3:
        if itb_enabled == 1:
            os.popen('echo "1" | sudo tee /sys/devices/system/cpu/intel_pstate/no_turbo').read()
        elif itb_enabled == 0:
            os.popen('echo "0" | sudo tee /sys/devices/system/cpu/intel_pstate/no_turbo').read()
        else:
            print("Unexpected error!")