import matplotlib.pyplot as plt
import os
import subprocess
from datetime import datetime
from pprint import pprint


# ----------------------------------------------------------------------------------------------------------------------

# Constants
PASSES = 5  # change to increase/decrease accuracy. 1 is minimum required to allow the program to function
SECONDS_CONVERTION = 100_000


# ----------------------------------------------------------------------------------------------------------------------


def time_algo(command, filename, passes):
    """
    Runs the C sort algorithms provided for X number of passes and returns an averaged time taken.
    """
    results = []

    for _ in range(passes):

        try:
            start_time = datetime.now()
            # Run the C commands from python and plugs in a file into the C program
            subprocess.run([f"./{command}", filename])
            end_time = datetime.now()
        except Exception as e:
            print(e)

        # Convert the time to seconds
        results.append(((end_time - start_time).microseconds) / SECONDS_CONVERTION)

    # Return the average time of the passes
    return {filename: sum(results) / passes}


# ----------------------------------------------------------------------------------------------------------------------


def print_results(raw_data):
    """
    Displays both raw data and graphed data.
    """
    # Raw data.
    for dictionary in raw_data:
        pprint(f"{dictionary}")
        print()

    # Create subplots and labels for each sorting algorithm
    fig, ax = plt.subplots(1, 3, figsize=(7, 7))
    fig.supylabel("Time to finish (seconds)")

    current_subplot = 0

    # Iterate over the raw data and plot the data
    for dictionary in raw_data:
        name = []
        values = []
        for value in dictionary:
            # Get the name and value of each data point
            for x in range(len(dictionary[value])):
                for item in dictionary[value][x]:
                    name.append(item)
                    values.append(dictionary[value][x][item])

            # Plot the data
            for x in range(len(name)):
                ax[current_subplot].bar(x + 1, values[x], label=name[x])
                ax[current_subplot].set_title(value)
        current_subplot += 1

    # Show the graph, legend and formatting.
    plt.legend(bbox_to_anchor=(1.25, 0.6), loc="center right")
    plt.tight_layout()
    plt.show()


# ----------------------------------------------------------------------------------------------------------------------


def main():
    # Get all the files in directory
    command_names = []

    files = os.listdir(os.getcwd())
    for file in files:
        if ".txt" not in file:
            if ".py" not in file:
                command_names.append(file)

    results = []

    # Get the time takento sort
    for command in command_names:
        command_results = []
        for file in files:
            if ".txt" in file:
                command_results.append(time_algo(command, file, PASSES))
        results.append({command: command_results})

    # Display results.
    print_results(raw_data=results)


if __name__ == "__main__":
    main()
