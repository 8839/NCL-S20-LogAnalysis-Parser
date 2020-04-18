
import os

def main():
    f = open("test.txt", "r")
    log = f.readlines()



    output = []
    array_pos = -1
    is_array = False
    for line_num in range(0, len(log)):
        line = log[line_num].strip()
        if is_array:
            if line is ")":
                is_array = False
            else:
                entry = line.split(" ")
                id = entry[0].replace("[","").replace("]","")
                if len(entry) == 3:
                    data = entry[2] 
                else:
                    data = "-"
                print(id + " " + data)
                output[array_pos] += line + ","
        else:
            if line is "(":
                is_array = True
            elif line is "":
                continue
            else:
                output.append(line.replace(" | ", ",") + ",")
                array_pos += 1

    #print(output)

    return

main()