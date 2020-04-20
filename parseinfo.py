#!/usr/bin/env 

# File: parseinfo.py
# Author: Patrick Perrine | Team: Midgard @ SDSU
# Function: Call Log Parser for NCL Spring 2020 Team Game

def main():
    input_file = open("Call.log", "r")
    log_lines = input_file.readlines()

    # All labels for each field, aside from date and request message
    data_order = ['from','to','uuid','conversation_uuid','status',
            'direction','timestamp','start_time','end_time','duration',
            'rate','price','network','timed_out','dtmf','press1_message_sent',
            'intro_sent_datetime','last_response_sent','encoded_id']

    output = [] # List for all information to be outputted
    data_line = []  # List for for call-specific data to be parsed 
    array_pos = -1  # Counter for iterating through call-specific data
    is_call_data = False # Flag to track if iterating through call data

    # Strip newlines, parse each line into output array
    for line_num in range(0, len(log_lines)):
        line = log[line_num].strip()

        # If not parsing through call-specific data, check if 
        # it has began or format the date and request line
        if not is_call_data:
            # If call data has began, initialize data_line and set flag
            if line is "(":
                is_call_data = True
                data_line = ["-","-","-","-","-","-","-","-","-",
                            "-","-","-","-","-","-","-","-","-","-"]
            # Checks for empty strings that trickled through
            elif line is "":
                continue
            # Format the date and request message, add to output array
            else:
                output.append(line.replace(" | ", ",") + ",")
                array_pos += 1

        # If parsing through call data, format data and add to data_line    
        else:
            # If call data isn't finished, extract label and format
            if line is not ")":
                entry = line.split(" ")
                id = entry[0].replace("[","").replace("]","")

                # If there are three tokens, there is normal data present
                if len(entry) == 3:
                    data = entry[2]
                # If there are four tokens, it is a timestamp 
                elif len(entry) == 4:
                    data = entry[2] + "T" + entry[3]
                # Otherwise, it is a field without accompanying data
                else:
                    data = "Missing"

                data_line[data_order.index(id)] = data

            # If call data ended, parse data_line to output, reset flag   
            else:
                is_call_data = False
                for item in data_line:
                    output[array_pos] += item + ","

    # Begin parsing output array into output file
    output_file = open("Call_Formatted.csv","a")

    # Add columns for each data label
    output_file.write("date,requestMessage,")
    for item in data_order:
        output_file.write(item + ",")

    # Write to file
    for line in output:
        output_file.write("\n" + line)

    # End program
    return

# Run program
if __name__ == "__main__":
    main()