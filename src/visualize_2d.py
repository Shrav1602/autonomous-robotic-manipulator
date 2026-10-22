import matplotlib.pyplot as plt
from src.geometry_2d import calculate_two_link_endpoint
joint1 = calculate_two_link_endpoint(10, 5, 30, 0)[0]
final_endpoint = calculate_two_link_endpoint(10, 5, 30, 0)[1]
plt.title("Two-Link Robotic Arm Visualization")
plt.scatter(0, 0, label='Base (0,0)', color='red')
plt.scatter(joint1[0], joint1[1], label= (joint1[0], joint1[1]), color='blue')
plt.plot([0, joint1[0]], [0, joint1[1]], label='Link 1')
plt.scatter(final_endpoint[0], final_endpoint[1], label= (final_endpoint[0], final_endpoint[1]), color='green')
plt.plot([joint1[0], final_endpoint[0]], [joint1[1], final_endpoint[1]], label='Link 2')
plt.ylabel('Y-axis')
plt.xlabel('X-axis')
plt.legend()
plt.axis('equal')
plt.grid(True)
plt.show()