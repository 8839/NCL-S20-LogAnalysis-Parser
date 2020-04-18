
import os

def main():
    f = open("test.txt", "r")
    log = f.readlines()

    data_order = ['from','to','uuid','conversation_uuid','status','direction','timestamp',
            'start_time','end_time','duration','rate','price','network','timed_out','dtmf']

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
                else:
                    data = "-EMPTY-"
                data_line[data_order.index(id)] = data
        else:
            if line is "(":
                is_array = True
                data_line = ["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"]
            elif line is "":
                continue
            else:
                output.append(line.replace(" | ", ",") + ",")
                array_pos += 1

    for line in output:
        print(line)

    return

main()