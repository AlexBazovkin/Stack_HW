class Stack:

    def __init__(self):
        self.stack = []

    def is_empty(self):
        if not self.stack:
            return True
        return False

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        result = self.stack.pop()
        return result

    def peek(self):
        result = self.stack[-1]
        return result

    def size(self):
        result = len(self.stack)
        return result


stack = Stack()


def balanced_sequence_check(sequence):
    brackets = ['()', '[]', '{}']
    for element in sequence:
        if element in '([{':
            stack.push(element)
        elif element in ')]}':
            if stack.is_empty():
                return False
            else:
                if (stack.peek() + element) in brackets:
                    stack.pop()
                else:
                    return False
    if stack.is_empty():
        return True
    else:
        return False


def main(sequences):
    balanced = 'Ballanced sequence'
    unbalanced = 'Unbalanced sequence'
    [print(f'{sequence} - {balanced}') if balanced_sequence_check(sequence)
     else print(f'{sequence} - {unbalanced}') for sequence in sequences]


if __name__ == '__main__':
    examples = ['(((([{}]))))',
                '[([])((([[[]]])))]{()}',
                '{{[()]}}',
                '}{}',
                '{{[(])]}}',
                '[[{())}]']
    main(examples)
