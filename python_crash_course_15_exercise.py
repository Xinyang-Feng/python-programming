import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    """Run a random walk and generate a plot"""
    # Make a random walk and plot the points
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Set the size of the plotting window
    plt.figure(figsize=(10, 6))

    points_number = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=points_number, cmap=plt.cm.Blues, edgecolors='none', s=1)

    # Emphasize the first and end point
    plt.scatter(0, 0, c='red', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='green', edgecolors='none', s=100)

    # Show the plot
    plt.show()

    # Ask for further running of the loop
    message = input("Would you like to draw another plot? (y/n)")
    if message == 'n':
        break





