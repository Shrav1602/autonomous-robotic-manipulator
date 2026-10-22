import math


def calculate_endpoint(link_length, angle_degrees):
    angle_rad = math.radians(angle_degrees)

    x = link_length * math.cos(angle_rad)
    y = link_length * math.sin(angle_rad)

    return (x, y)

def calculate_two_link_endpoint(link1_length, link2_length, angle1_degrees, angle2_degrees):

    joint1 = calculate_endpoint(link1_length, angle1_degrees)
    link2_displacement = calculate_endpoint(link2_length, angle1_degrees + angle2_degrees)
    final_endpoint = (joint1[0] + link2_displacement[0], joint1[1] + link2_displacement[1])

    return (joint1, final_endpoint)



if __name__ == "__main__":
    test_configurations = [
        (10, 0),
        (10, 90),
        (10, 180)
    ]

    for length, angle in test_configurations:
        endpoint = calculate_endpoint(length, angle)
        print(f"Length: {length}, Angle: {angle}° -> Endpoint: {endpoint}")


if __name__ == "__main__":
    test_configurations = [
        (10, 5, 0, 0),
        (10, 5, 90, 0),
        (10, 5, 30, 0),
        (10, 5, 45, 30),
        (10, 5, 90, -45)

    ]

    for link1_length, link2_length, angle1, angle2 in test_configurations:
        joint1, final_endpoint = calculate_two_link_endpoint(link1_length, link2_length, angle1, angle2)
        print(f"Link1: {link1_length}, Link2: {link2_length}, Angle1: {angle1}°, Angle2: {angle2}° -> Joint1: {joint1}, Final Endpoint: {final_endpoint}")