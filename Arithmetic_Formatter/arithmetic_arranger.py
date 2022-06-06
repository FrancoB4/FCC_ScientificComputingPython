def arithmetic_arranger(problems, display_answer=False):
    problems_data = []
    problems_count = 0

    for problem in problems:
        problems_count += 1

        if problem.split(' ')[1] not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if len(problem.split(' ')[0]) > 4 or len(problem.split(' ')[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        for char in problem.split()[0]:
            if not char.isnumeric():
                return 'Error: Numbers must only contain digits.'

        for char in problem.split()[2]:
            if not char.isnumeric():
                return 'Error: Numbers must only contain digits.'

        max_digits = max(len(problem.split(' ')[0]), len(problem.split(' ')[2]))
        max_digits += 2

        first = ' ' * (max_digits - len(problem.split(' ')[0])) + problem.split(' ')[0]
        second = problem.split(' ')[1] + (' ' * (max_digits - 1 - len(problem.split(' ')[2])) + problem.split(' ')[2])

        separator = '-' * max_digits

        if second.split()[0] == '+':
            result = str(int(first) + int(second.split()[1]))
        else:
            result = str(int(first) - int(second.split()[1]))

        result = ' ' * (max_digits - len(result)) + result

        problems_data.append({'first': first, 'second': second, 'separator': separator, 'result': result})

    if problems_count > 5:
        return 'Error: Too many problems.'

    first_row = '    '.join([problem['first'] for problem in problems_data])
    second_row = '    '.join([problem['second'] for problem in problems_data])
    separator_row = '    '.join([problem['separator'] for problem in problems_data])
    results_row = '    '.join([problem['result'] for problem in problems_data])

    if display_answer:
        arranged_problems = first_row + '\n' + second_row + '\n' + separator_row + '\n' + results_row
    else:
        arranged_problems = first_row + '\n' + second_row + '\n' + separator_row

    return arranged_problems
