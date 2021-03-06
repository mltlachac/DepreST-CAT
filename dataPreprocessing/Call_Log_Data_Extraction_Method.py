from typing import TextIO

sub_line_set = set()

Alpha_Numeric_Char_Field_Size    = 9

#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================

def Extract_Sub_Line(line):
    return line.split('sessionid"":""',1)[1]
#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================

def Extract_Session_ID(line):
    return line.split('sessionid"":""',1)[1].split('""',1)[0]

#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================

def Extract_Phone_id(line):
    temp =  line.split('"sessionid"":""',1)[1].split('"',1)[0]
    number_of_chars_to_keep = len(temp) - Alpha_Numeric_Char_Field_Size
    return temp[0:number_of_chars_to_keep] #Returns phone ID

#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================

def Extract_Alpha_Numeric_Number(line):
    temp =  line.split('"sessionid"":""',1)[1].split('"',1)[0]
    return temp[-Alpha_Numeric_Char_Field_Size:]

#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================

def Extract_Type(line):
    return line.split('"type\\\\"":\\\\""',1)[1].split('\\',1)[0]

#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================

def Extract_Duration(line):
    return line.split('duration\\\\"":\\\\""',1)[1].split('\\',1)[0]

#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================
def Extract_Date(line):
    value = line.replace("\\","_")
    value = value.replace('"',"_")
    value = value.split('date____:____',1)[1].split("_",1)[0]
    return value

#=======================================================================================================================
#=======================================================================================================================
#=====================================================================
def Extract_Number(line):
    value = line.replace("\\","_")
    value = value.replace('"',"_")
    return value.split('number____:____',1)[1].split('_',1)[0]

#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================


def Process_Call_Type(input_file_path, output_file_path):

    # Opens CSV file for read only
    input_file = open(input_file_path, 'r')

    #Opens the output file for write
    output_file: TextIO = open(output_file_path, "w")

    output_file.write("Session_ID,Phone_ID,Alpha_Numeric,Type_Value,Duration,Date,Number\n")

    remove_count = 0
    count        = 0

    # Skip the first line of the input file
    line = input_file.readline()

    while True:

        count += 1

        if (count % 500) == 0:
            print("count = " + str(count) + " remove_count = " + str(remove_count))

        line: str = input_file.readline()

        if not line:
            #End of file detected
            break

        # Was instructed to elimate these lines
        if "6a67befc231" in line or  "022b71d6cda" in line or "DOCTYPE" in line:
            continue

        Phone_ID         = Extract_Phone_id(line)
        alpha_numeric    = Extract_Alpha_Numeric_Number(line)
        session_id       = Extract_Session_ID(line)
        type_value       = Extract_Type(line)
        duration         = Extract_Duration(line)
        date             = Extract_Date(line)
        number           = Extract_Number(line)


        sub_line = Extract_Sub_Line(line)

        if sub_line in sub_line_set:
            remove_count += 1
            continue

        sub_line_set.add(sub_line)

        output_file.write(session_id)
        output_file.write("," + Phone_ID)
        output_file.write(","  + alpha_numeric)
        output_file.write(","  + type_value)
        output_file.write(","  + duration)
        output_file.write("," + date)
        output_file.write("," + number)

        output_file.write("\n")

    output_file.close()

    print("count = " + str(count) + " remove_count = " + str(remove_count))

    print("Process_Call_Type Done")

# =======================================================================================================================
# =======================================================================================================================
# =======================================================================================================================

Process_Call_Type("input_file.csv","created_output_file.csv")

print("All Done")
