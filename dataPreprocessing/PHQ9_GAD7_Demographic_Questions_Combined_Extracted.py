from typing import TextIO

Max_Number_Of_Questions         = 10
Alpha_Numeric_Char_Field_Size   = 9

Results_dictionary = {}

class Result:
    def __init__(self, session_id, alpha_numeric,phone_id):
        self.session_id             = session_id
        self.alpha_numeric          = alpha_numeric
        self.Phone_ID               = phone_id
        self.version                = ""
        self.questions_PHQ          = list()
        self.questions_GAD          = list()
        self.questions_demographic  = list()
        self.date_time              = 'None'

    def Write_Questions_PHQ(self,file):
        if len(self.questions_PHQ) == 0:
            for i in range(0,10):
                file.write(",-")
        else:
            sum = 0
            for i in range(0,9):
                file.write(","+ self.questions_PHQ[i])
                sum += int(self.questions_PHQ[i])
            file.write("," + str(sum))

    def Write_Questions_GAD(self,file):
        if len(self.questions_GAD) == 0:
            for i in range(0,8):
                file.write(",-")
        else:
            sum = 0
            for i in range(0,7):
                file.write(","+ self.questions_GAD[i])
                sum += int(self.questions_GAD[i])
            file.write("," + str(sum))

    def Write_Questions_Demographic(self,file):
        if len(self.questions_demographic) == 0:
            for i in range(0,7):
                file.write(",-")
        else:
            for i in range(0,7):
                file.write(","+ self.questions_demographic[i])


    def Write_To_CSV_Line(self,file):
        if len(self.questions_PHQ) == 0:
            return
        if len(self.questions_GAD) == 0:
            return
        file.write(self.session_id)
        file.write("," + self.Phone_ID)
        file.write("," + self.alpha_numeric)
        file.write("," + self.version)
        self.Write_Questions_PHQ(file)
        self.Write_Questions_GAD(file)
        self.Write_Questions_Demographic(file)
        file.write("," + '"' + self.date_time)
        file.write("\n")


#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================

def Exract_Session_ID(line):
    return line.split(',',1)[0]

# =======================================================================================================================
# =======================================================================================================================
# =======================================================================================================================

def Extract_Phone_id(line):
    temp =  line.split(',')[0].strip('"') #Splits on first comma, removes "
    number_of_chars_to_keep = len(temp) - Alpha_Numeric_Char_Field_Size
    return temp[0:number_of_chars_to_keep] #Returns phone ID

#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================

def Extract_Alpha_Numeric_Number(line):
    temp  =  line.split(',')[0].strip('"')#Splits on first comma, removes "
    return temp[-Alpha_Numeric_Char_Field_Size:]

#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================

def Extract_Type(line):
    return line.split('""type"":""',1)[1].split('"',1)[0] #Splits after ""type"":"" and splits at follwing ".  Take first part.

#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================

def Extract_Content(line):
    return line.split('""content"":""',1)[1].split('"',1)[0] #Splits after ""type"":"" and splits at follwing ".  Take first part.

#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================
def Extract_Date_Time(line):
    return line.split(',')[-1].strip('\n') #Split at all commas. Take last piece. Remove end of line charactor

#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================

def Extract_Version(line):
    spliter = '""version"",""content"":""'
    if spliter in line:
        return line.split('""version"",""content"":""', 1)[1].split('"', 1)[0]
    else:
        return ""

#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================

def Exstract_Answers(line):
    question_str    = '\\""Q%d\\"":\\""'  #question header templete
    question_number = 0; #Start at quesion 0
    answers         = [] #No answer initially

    while True:
        question_header = question_str % question_number
        if question_header in line: #Verifies question number X is in line
            result = line.split(question_header, 1) #Split after question header
            result = result[1].split('\\""', 1) #Split items after question answer
            answer = result[0]
            answer = answer.replace(","," &",10)
            answers.append(answer) #Append the answer to answers
            line = result[1] #Take rest of line
            question_number += 1 #Incroment question number, check again for answer.
        else:
            return answers

#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================

def Extract_Payment(line):
    payment_header = '"payment"",""content"":""'
    if payment_header in line:
        return line.split(payment_header,1)[1].split('"',1)[0] #Splits after payment_header and splits at follwing ".  Take first part.
    else:
        return ''

#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================

def Write_Answers_To_CSV(output_file,answers):
    number_of_answers = len(answers)
    if len(answers) > 0:
        for i in range(0, Max_Number_Of_Questions): #Loop through 10 questions
            if i < number_of_answers:
                if " " in answers[i] or "," in answers[i]: #Check for spaces and commas in answer
                    output_file.write('"' + answers[i] + '",') #Add quotes if present as this will cause error in CSV
                else:
                    output_file.write(answers[i] + ',') #Write out answer with comma after
            else:
                output_file.write(',') #If no answer, write comma (There is not nessisarily 10 questions)

#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================

def Process_Questions_2_File(input_file_path, Results_dictionary):

    #Opens CSV file for read only
    input_file = open(input_file_path, 'r')

    lines_processed = 0
    remove_count    = 0

    # Skip the first line of the input file
    line = input_file.readline()

    while True:
        line: str = input_file.readline()

        if not line:
            #End of file detected
            break

        lines_processed += 1 #Add one to line processed counter

        if (lines_processed % 500) == 0:
            print("lines_processed = " + str(lines_processed) + " remove_count = " + str(remove_count))

        # Was instructed to elimate these lines
        if "6a67befc231" in line or  "022b71d6cda" in line or "DOCTYPE" in line:
            continue

        session_id           = Exract_Session_ID(line)
        alpha_numeric        = Extract_Alpha_Numeric_Number(line)
        phone_id             = Extract_Phone_id(line)
        answers              = Exstract_Answers(line)
        version              = Extract_Version(line)
        type_value           = Extract_Type(line)
        date_time            = Extract_Date_Time(line)

        if session_id not in Results_dictionary:
            Results_dictionary[session_id] = Result(session_id,alpha_numeric,phone_id)

        if version != "":
            Results_dictionary[session_id].version = version

        if type_value == 'gad' and len(Results_dictionary[session_id].questions_GAD) == 0:
            Results_dictionary[session_id].questions_GAD = answers

        if type_value == 'phq' and len(Results_dictionary[session_id].questions_PHQ) == 0:
            Results_dictionary[session_id].questions_PHQ = answers
            Results_dictionary[session_id].date_time = date_time

        if type_value == 'demographic' and len(Results_dictionary[session_id].questions_demographic) == 0:
            Results_dictionary[session_id].questions_demographic = answers

    print("lines_processed = " + str(lines_processed) + " remove_count = " + str(remove_count))

#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================

def Write_Results_To_File(Results_dictionary, output_file_path):
    output_file: TextIO = open(output_file_path, "w")

    # write CSV header
    output_file.write("Session_ID,Phone_ID,Alpha_Numeric,prolificVersion");
    output_file.write(",PHQ - Q1,PHQ - Q2,PHQ - Q3,PHQ - Q4,PHQ - Q5,PHQ - Q6,PHQ - Q7,PHQ - Q8,PHQ - Q9,PHQ - Total")
    output_file.write(",GAD - Q1,GAD - Q2,GAD - Q3,GAD - Q4,GAD - Q5,GAD - Q6,GAD - Q7,GAD - Total")
    output_file.write(",D1,D2,D3,D4,D5,D6,D7,Date_Time \n")

    for result in Results_dictionary.items():
        result[1].Write_To_CSV_Line(output_file)

    output_file.close()

# =======================================================================================================================
# =======================================================================================================================
# =======================================================================================================================


Process_Questions_2_File("input_file.csv", Results_dictionary)

Write_Results_To_File(Results_dictionary,"output_file".csv)

print("End of Program")-
