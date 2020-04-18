#!/usr/bin/env python

def main():
    input_file = open("Call.log", "r")
    log = input_file.readlines()

    data_order = ['from','to','uuid','conversation_uuid','status','direction','timestamp',
            'start_time','end_time','duration','rate','price','network','timed_out','dtmf',
            'press1_message_sent','intro_sent_datetime','last_response_sent','encoded_id']

    output = []
    data_line = []
    array_pos = -1
    is_array = False
    for line_num in range(0, len(log)):
        line = log[line_num].strip()
        if is_array:
            if line is ")":
                is_array = False
                for item in data_line:
                    output[array_pos] += item + ","
            else:
                entry = line.split(" ")
                id = entry[0].replace("[","").replace("]","")
                if len(entry) == 3:
                    data = entry[2]
                elif len(entry) == 4:
                    data = entry[2] + "T" + entry[3]
                else:
                    data = "Missing"
                data_line[data_order.index(id)] = data
        else:
            if line is "(":
                is_array = True
                data_line = ["-","-","-","-","-","-","-","-","-","-",
                             "-","-","-","-","-","-","-","-","-"]
            elif line is "":
                continue
            else:
                output.append(line.replace(" | ", ",") + ",")
                array_pos += 1

    output_file = open("Call_Formatted.csv","a")

    output_file.write("date,requestMessage,")
    for item in data_order:
        output_file.write(item + ",")

    for line in output:
        output_file.write("\n" + line)

    return

main()