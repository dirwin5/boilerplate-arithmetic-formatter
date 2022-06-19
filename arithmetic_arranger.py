def arithmetic_arranger(problems, print_answers=False):

    #check no more than 5 problems
    if len(problems) > 5:
        return "Error: Too many problems."
    
    operand1_l = []
    operator_l = []
    operand2_l = []
    
    #put values into lists
    for problem in problems:
        problem_split = problem.split()
        operand1_l.append(problem_split[0])
        operator_l.append(problem_split[1])
        operand2_l.append(problem_split[2])
        
    #check operators don't include * or /
    if "*" in operator_l or "/" in operator_l:
        return "Error: Operator must be '+' or '-'."
    
    #check operands only contain numbers and are no more than 4 digits
    for operand1 in operand1_l:
        try:
            int(operand1)
        except ValueError:
            return "Error: Numbers must only contain digits."
        if len(operand1) > 4:
            return "Error: Numbers cannot be more than four digits."
        
    for operand2 in operand2_l:
        try:
            int(operand2)
        except ValueError:
            return "Error: Numbers must only contain digits."
        if len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."
        
    #get required output length for each problem
    problem_len_l = []    
    for i, operand1 in enumerate(operand1_l):
        if len(operand1) > len(operand2_l[i]):
            problem_len_l.append(len(operand1) + 2)
        else:
            problem_len_l.append(len(operand2_l[i]) + 2)
            
    #get list of strings for line 1
    line1_l = []
    for i, operand1 in enumerate(operand1_l):
        whitespace_len = problem_len_l[i] - len(operand1)
        working_list = []
        #preceeding whitespace
        for ws in range(whitespace_len):
            working_list.append(' ')
        #operand
        working_list.append(operand1)
        #end whitespace
        working_list.append('    ')
        line1_l.append(''.join(working_list))
        
    #trim end whitespace on last entry
    line1_l[len(line1_l) - 1] = line1_l[len(line1_l) - 1].rstrip()
    line1_l.append('\n')
    line1 = ''.join(line1_l)
    
    #get list of strings for line 2
    line2_l = []
    for i, operand2 in enumerate(operand2_l):
        whitespace_len = problem_len_l[i] - len(operand2) - 1
        working_list = []
        #operator
        line2_l.append(operator_l[i])
        #whitespace
        for ws in range(whitespace_len):
            working_list.append(' ')
        #operand
        working_list.append(operand2)
        #end whitespace
        working_list.append('    ')
        line2_l.append(''.join(working_list))
        
    #trim end whitespace on last entry
    line2_l[len(line2_l) - 1] = line2_l[len(line2_l) - 1].rstrip()
    line2_l.append('\n')
    line2 = ''.join(line2_l)
    
    
    #get list of strings for line 3
    line3_l = []
    for problem_len in problem_len_l:
        working_list = []
        #dashes
        for char in range(problem_len):
            working_list.append('-')
        #end whitespace
        working_list.append('    ')
        line3_l.append(''.join(working_list))
        
    #trim end whitespace on last entry
    line3_l[len(line3_l) - 1] = line3_l[len(line3_l) - 1].rstrip()
    if print_answers is True:
        line3_l.append('\n')
    line3 = ''.join(line3_l)
    
    
    #get answers list
    answers_l = []
    for i, operand1 in enumerate(operand1_l):
        if operator_l[i] == '+':
            answer = int(operand1) + int(operand2_l[i])
        else:
            answer = int(operand1) - int(operand2_l[i])
        answers_l.append(str(answer))
        
    #get list of strings for line 4
    line4_l = []
    for i, answer in enumerate(answers_l):
        whitespace_len = problem_len_l[i] - len(answer)
        working_list = []
        #whitespace
        for ws in range(whitespace_len):
            working_list.append(' ')
        #answer
        working_list.append(answer)
        #end whitespace
        working_list.append('    ')
        line4_l.append(''.join(working_list))
        
    #trim end whitespace on last entry
    line4_l[len(line4_l) - 1] = line4_l[len(line4_l) - 1].rstrip()
    line4 = ''.join(line4_l)
        
    
    #return
    if print_answers is True:
        return line1 + line2 + line3 + line4
    else:
        return line1 + line2 + line3
    
