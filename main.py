from sys import exit
import sympy


def main() -> None:
    print('Welcome to The Limit Calculator!')
    print("Enter 'inf' or 'infinity' for an infinite limit when prompted to enter a limit.")
    while True:
        try:
            symbol: sympy.core.symbol.Symbol = sympy.symbols(
                input('Enter a symbol: '))

            math_expr: str = input('Enter a mathematical expression: ')

            lim: float = float(input('Enter a limt: '))

            result = sympy.limit(math_expr, symbol, lim)

            if type(result) == sympy.core.numbers.Integer:
                print(f'{result}')
            elif type(result) == sympy.core.numbers.Float:
                print(f'{result:.3f}')
            else:
                print(f'{result}')

            choice: str = input(
                'Do you want to continue using the program? (Y/n) ')
            if choice.lower() == 'y':
                continue
            else:
                print('Thanks for trying my program!')
                exit()

        except ValueError:
            print('Invalid input...')
            continue
        except KeyboardInterrupt:
            print('Exiting...')
            exit()


if __name__ == '__main__':
    main()
