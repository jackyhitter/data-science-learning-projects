import time

# TODO update the decorator from problem 2
def mission_timer(func):
    def enhanced(*args, **kwargs):
        for i in range(3, 0, -1):
            print(f"{i}...")
            time.sleep(1)
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Mission duration: {end - start} seconds")
        print()
        return result
    return enhanced

@mission_timer
def launch_probe(target):
    print(f"Launching probe toward {target}...")
    time.sleep(1)
    return f"Probe successfully en route to {target}."

@mission_timer
def deploy_satellite(orbit_type, altitude_km):
    print(f"Deploying satellite into {orbit_type} orbit at {altitude_km} km...")
    time.sleep(2)

deploy_satellite("polar", 800)

result = launch_probe("Europa")
print("Stored mission result:", result)