def arithmetic_arranger(problems, print_answers=False):

    class Problem:
        def __init__(self, problem_no, operand1, operator, operand2):
            self.problem_no = problem_no
            self.operand1 = operand1
            self.operator = operator
            self.operand2 = operand2
            
            if self.operator == '+':
                self.result = int(self.operand1) + int(self.operand2)
            else:
                self.result = int(self.operand1) - int(self.operand2)
                
            self.problem_length = max(len(self.operand1), len(self.operand2)) + 2
            self.line1_ws_len = self.problem_length - len(self.operand1)
            self.line2_ws_len = self.problem_length - len(self.operand2) - 1
            self.resultline_ws_len = self.problem_length - len(str(self.result))

    #check no more than 5 problems
    if len(problems) > 5:
        return "Error: Too many problems."
    
    problem_list = []
    for i, problem in enumerate(problems):
        operands = []
        operands = problem.split('+')
        operator = '+'
        if len(operands) != 2:
            operands = problem.split('-')
            operator = '-'
        if len(operands) != 2:
            return "Error: Operator must be '+' or '-'."
        #remove whitespace
        operands = [operand.strip() for operand in operands]
        #check operands only contain numbers and are no more than 4 digits
        for operand in operands:
            try:
                int(operand)
            except ValueError:
                return "Error: Numbers must only contain digits."
            if len(operand) > 4:
                return "Error: Numbers cannot be more than four digits."
        #append problem to problem list  
        problem_list.append(Problem(i, operands[0], operator, operands[1]))
    
       
    #get list of strings for line 1
    line1 = ''
    for problem in problem_list:
        #preceeding whitespace
        for ws in range(problem.line1_ws_len):
            line1 += ' '
        #operand
        line1 += problem.operand1
        #end whitespace
        line1 += '    '        
    #trim end whitespace on last entry
    line1 = line1[:-4]
    line1 += '\n'
    
    #get list of strings for line 2
    line2 = ''
    for problem in problem_list:
        #operator
        line2 += problem.operator
        #preceeding whitespace
        for ws in range(problem.line2_ws_len):
            line2 += ' '
        #operand
        line2 += problem.operand2
        #end whitespace
        line2 += '    '       
    #trim end whitespace on last entry
    line2 = line2[:-4]
    line2 += '\n'
    
    #get list of strings for line 3
    line3 = ''
    for problem in problem_list:
        for dash in range(problem.problem_length):
            line3 += '-'
        #end whitespace
        line3 += '    '
    #trim end whitespace on last entry
    line3 = line3[:-4]
    if print_answers is True:
        line3 += '\n'
        
    #get list of strings for line 4
    line4 = ''
    for problem in problem_list:
        #preceeding whitespace
        for ws in range(problem.resultline_ws_len):
            line4 += ' '
        #answer
        line4 += str(problem.result)
        #end whitespace
        line4 += '    '
    #trim end whitespace on last entry
    line4 = line4[:-4]
          
    
    #return
    if print_answers is True:
        return line1 + line2 + line3 + line4
    else:
        return line1 + line2 + line3
    
