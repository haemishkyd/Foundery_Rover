import sys
import os
import matplotlib.pyplot as plt

GridSizeX = 0
GridSizeY = 0
global_script_verbosity = 0
RoverArray = []
PossibleDirections=['N','S','E','W']
AllTheLines=[]

class Rover:

    def __init__ (self,x,y,o):
        self.x = x
        self.y = y
        self.o = o
        self.array_of_x=[]
        self.array_of_y=[]
        self.array_of_x.append(self.x+0.5)
        self.array_of_y.append(self.y+0.5)
        if ((x<=GridSizeX) and (y<=GridSizeY) and (self.o in PossibleDirections)):
            self.valid_start = True
        else:
            self.valid_start = False
        self.instruction_pointer = 0


    def store_instructions(self,instruction_string):
        self.instruction_string = instruction_string


    def number_of_instructions(self):
        return len(self.instruction_string)


    def print_current_coordinates(self):
        if (self.valid_start):
            smart_print((str(self.x) + " " + str(self.y) + " " + self.o),0)
        else:
            smart_print(("This rover did not land on the plateau and is now damaged."),0)


    def step_instruction(self):
        if (self.valid_start):
            current_instruction = self.instruction_string[self.instruction_pointer]
            self.instruction_pointer = self.instruction_pointer + 1
            if (current_instruction == 'L'):
                self.instruction_L()
            if (current_instruction == 'R'):
                self.instruction_R() 
            if (current_instruction == 'M'):
                self.instruction_M()
        

    def instruction_L(self):
        if (self.o == 'N'):
            self.o = 'W'
        elif (self.o == 'E'):
            self.o = 'N'
        elif (self.o == 'S'):
            self.o = 'E'
        elif (self.o == 'W'):
            self.o = 'S'
        
    def instruction_R(self):
        if (self.o == 'N'):
            self.o = 'E'
        elif (self.o == 'E'):
            self.o = 'S'
        elif (self.o == 'S'):
            self.o = 'W'
        elif (self.o == 'W'):
            self.o = 'N'

    def instruction_M(self):
        if (self.o == 'N'):
            self.y = self.y + 1
        elif (self.o == 'E'):
            self.x = self.x + 1
        elif (self.o == 'S'):
            self.y = self.y - 1
        elif (self.o == 'W'):
            self.x = self.x -1
        if (self.x < 0):
            self.x = 0
        if (self.y < 0):
            self.y = 0
        if (self.x > GridSizeX):
            self.x = GridSizeX
        if (self.y > GridSizeY):
            self.y = GridSizeY
        self.array_of_x.append(self.x+0.5)
        self.array_of_y.append(self.y+0.5)
        


def smart_print(string_to_print, string_verbosity_level):
    if (string_verbosity_level <= global_script_verbosity):
        output_fh = open("merchant_guide_output.txt", 'a')
        output_fh.write(string_to_print)
        output_fh.write("\n\r")
        output_fh.close()
        print (string_to_print)


def create_rovers(start_pos,instructions):
    # Extract all the data and create the rover object with all of that data
    for rover_idx in range(0,len(start_pos)):
        start_pos_split = start_pos[rover_idx].split()
        temp_rover = Rover(int(start_pos_split[0]),int(start_pos_split[1]),start_pos_split[2])
        temp_rover.store_instructions(instructions[rover_idx])
        RoverArray.append(temp_rover)


if __name__ == "__main__":
    start_pos_array = []
    instructions_array = []
    # Check the inputs
    if (len(sys.argv) == 1):
        smart_print("You need to specify an input file.",0)
    else:
        output_fh = open("merchant_guide_output.txt", 'w')
        output_fh.close()
        if not os.path.exists(sys.argv[1]):
            smart_print("Much like life on mars, I can't find "+sys.argv[1], 0)
        else:
            # Get the file that contains the instructions
            fh = open(sys.argv[1], 'r')
            for line in fh:
                if line.startswith('#'):
                    pass
                else:
                    AllTheLines.append(line)
            # Extract the size of the grid and set it as global
            size_of_grid = AllTheLines[0]
            split_sog = size_of_grid.split()
            GridSizeX = int(split_sog[0])
            GridSizeY = int(split_sog[1])    
            smart_print("Grid Size X: "+str(GridSizeX)+ " Y: "+str(GridSizeY),0)
            # Extract the data from the file in order to create the rovers
            for line_idx in range(0,len(AllTheLines)):            
                # We have already pulled out the grid size.
                if line_idx == 0:
                    continue
                if line_idx % 2 == 0:
                    continue 
                start_pos_array.append(AllTheLines[line_idx])
                instructions_array.append(AllTheLines[line_idx+1])            
            # Now create the rovers with the data extracted in the last step
            create_rovers (start_pos_array,instructions_array)
            # Intialise the graphing system
            fig, ax = plt.subplots()
            # Each rover object contains its own instructions so just execute them 
            for each_rover in RoverArray:  
                plt.scatter(each_rover.array_of_x[0],each_rover.array_of_y[0],c='g')
                for instr_idx in range(0, each_rover.number_of_instructions()):
                    each_rover.step_instruction()
                    plt.plot(each_rover.array_of_x,each_rover.array_of_y)         
                plt.scatter(each_rover.array_of_x[len(each_rover.array_of_x)-1],each_rover.array_of_y[len(each_rover.array_of_y)-1],c='r')
                # Print the final result for each rover
                each_rover.print_current_coordinates()
            plt.axis([0,GridSizeX+1,0,GridSizeY+1])
            plt.grid(True)
            plt.show()
            
