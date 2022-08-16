def arithmetic_arranger(problems, add=False):
    first = []
    operat = []
    second = []
    sum = []
    first_line = ""
    second_line = ""
    third_line = ""
    fourth_line = ""
    if len(problems) > 5:
        return "Error: Too many problems."
    else:
        for math in problems:
            question = math.split()
            first.append(question[0])
            operat.append(question[1])
            second.append(question[2])
            if (question[0].isdigit() and question[2].isdigit()):
                result = eval(f'{question[0]} {question[1]} {question[2]}')
                sum.append(result)

            else:
                return 'Error: Numbers must only contain digits.'

        #error checking
        for i in range(len(operat)):
            if operat[i] not in ["-", "+"]:
                return "Error: Operator must be '+' or '-'."
        for i in range(len(first)):
            if len(str(first[i])) > 4 or len(str(second[i])) > 4:
                return "Error: Numbers cannot be more than four digits."

        for i in range(len(first)):
            if len(str(first[i])) > len(str(second[i])):
                longest = len(str(first[i]))
            else:
                longest = len(str(second[i]))
            if (len(first) - i) > 1:
                addedSpace = "    "
            else:
                addedSpace = ""
            first_line += (first[i].rjust(longest + 2, " ")) + addedSpace
            mix = second[i].rjust(longest + 1, " ")
            secondLine = f'{operat[i]}{mix}'
            second_line += secondLine + addedSpace
            third_line += ("-" * (longest + 2)) + addedSpace
            fourth_line += (str(sum[i]).rjust(longest + 2, " ")) + addedSpace
        if add:
            solution = first_line + "\n" + second_line + "\n" + third_line + "\n" + fourth_line
        else:
            solution = first_line + "\n" + second_line + "\n" + third_line
        return solution


#return arranged_problem
