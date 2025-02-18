from sys import exit
import sympy
from word2number import w2n


def main() -> None:
    greeting: str = """Welcome to The Limit 🖩!
Enter 'inf' or 'infinity' for an infinite limit when prompted to enter a limit."""
    print(greeting)
    exit_message: str = 'Exiting program...'
    while True:
        try:
            user_input: str = input('Enter a symbol: ')

            if user_input.isalpha() and len(user_input) == 1:
                symbol: sympy.core.symbol.Symbol = sympy.symbols(user_input)
            else:
                print('Please enter a valid symbol...')
                continue

            math_expr: str = input('Enter a mathematical expression: ')

            user_input: str = input('Enter a limit: ')

            if user_input.isalpha() and user_input != 'inf' and user_input != 'infinity':
                lim: float = w2n.word_to_num(user_input)
            else:
                lim: float = float(user_input)

        except ValueError:
            print('Please enter valid input...')
            continue

        except KeyboardInterrupt:
            print(exit_message)
            exit()

        result = sympy.limit(math_expr, symbol, lim)

        if type(result) == sympy.core.numbers.Integer:
            print(f'{result}')
        elif type(result) == sympy.core.numbers.Float:
            print(f'{result:.3f}')
        else:
            print(f'{result}')


if __name__ == '__main__':
    main()
