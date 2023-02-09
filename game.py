from random import randint

if __name__ == "__main__":
    right = 0
    list_s = []
    for i in range(1, 11):
        first = randint(1, 10)
        second = randint(1, 10)
        result = first * second
        print(f'{i} question: {first} * {second} = ? ')

        try:
            answer = int(input('Enter your answer: '))
        except ValueError:
            answer = int(input('Enter your answer: '))

        if answer == result:
            right += 1
            status = "Correct"
            print('Right')
        else:
            print(f'Wrong! Answer:{result}')
            status = "Wrong"

        list_s.append((f'Q{i}: {first} * {second} = ?; '
                       f'Student Answer: {answer}; '
                       f'Answer: {result}; Status: {status} '))

    if right >= 7:
        print(f'The test is passed. Correct answers: {right}. Wrong answers: {10 - right}.')
    else:
        print(f'The test is not passed. Correct answers: {right}. Wrong answers: {10 - right}.')

    word = '** *SUMMARY* **'

    print(f'{word}')

    for element in list_s:
        print(f'{element}')