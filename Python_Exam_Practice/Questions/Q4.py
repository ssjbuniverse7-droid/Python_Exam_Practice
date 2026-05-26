def collector(file_name):
    try:
        # Variables
        binaries = []

        # Iterate through the lines
        with open(file_name,"r") as file:
            for line in file:
                # take binaries
                for char in line:
                    if char == "0" or char == "1":
                        binaries.append(char)
                        # convert list to string
                        binaryString = "".join(binaries)

    except FileNotFoundError:
        print("Coudn't find file:",file_name)

    return binaryString

print(collector("Questions/exampleFile.txt"))

def consec_sequence(binaryString):
    # Return empty list if string is empty
    if binaryString == "":
        return []
    
    # Variables
    lengths = []
    current_count = 1

    # Iterate through string
    for i in range(1, len(binaryString)):

        # If the current character is the same as the previous one
        if binaryString[i] == binaryString[i - 1]:
            current_count += 1
        
        else:
            # Store the completed sequence length
            lengths.append(current_count)
            current_count = 1

    # Add the final sequence length
    lengths.append(current_count)

    return lengths

print(consec_sequence(collector("Questions/exampleFile.txt")))

def visualisor(sequence, max_width):
    # Variables
    bar_chart = []

    # Iterate through the list
    for i in range(len(sequence)):
        bar = ""
        for num in range(sequence[i]):
            bar += "#"
            # check if max width is reached
            if num > int(max_width):
                bar += ">"
                break
        # add finished bar to chart and reset
        bar_chart.append(bar)
       
            
    
    # convert list to string
    bar_string = "\n".join(bar_chart)

    # Save to file
    with open ("output.txt","a") as file:
        file.write(bar_string)
    
visualisor(consec_sequence(collector("Questions/exampleFile.txt")),7)
