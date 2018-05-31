# Mars Rover
This project has been assigned in completion of an assessment to ascertain technical ability.

The language chosen is *Python*. The version of Python tested against is version 3.6.4 but the code should be backwards compatible to all versions of Python 3.

Other than **sys** (in order to extract argument parameters) and **os** (for file manipulation) no packages have been used.

For the visual version of this excercise, the package **Matplotlib** has been used. This is however not essential and was done merely as a way to visualise the rover movements.

In all instances the output is displayed on the screen and written to a file. The file is named *merchant_guide_output.txt* - because apparently copy paste errors are still a thing after you check your code 4 times.

## Executing
To execute the script type: *python mars_rover.py <test_script>*

A further piece of work executes the script but gives a visual representation of the progress of the various rovers. This can be executed by typing: *python mars_rover_visual.py <test_script>*

In the event that a Python interpreter is not available, an executable built from the script has been provided. 

This can be executed by running: *mars_rover.exe <test_script>*

An executable has not been provided for the visual option since the *inefficient* way Python creates executables means this is a **very** large executable.

## Visualisation
The visualisation script does *exactly* what the normal script does except that at the end it plots the movement that the rover took. It places a green dot at the start point and a red dot at the end point.
All rovers that are in the file will be shown in one image as different colours.

## Assumptions
None
