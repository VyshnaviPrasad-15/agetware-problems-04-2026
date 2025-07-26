def format_indian_currency(number):
    num_str = f"{number}"
    if '.' in num_str:
        integer_part, fractional_part = num_str.split('.')
        fractional_part = '.' + fractional_part
    else:
        integer_part = num_str
        fractional_part = ''
    
    n = len(integer_part)
    if n <= 3:
        return integer_part + fractional_part

 
    main_part = integer_part[-3:]
    rest = integer_part[:-3]

    result = []
    while len(rest) > 2:
        result.append(rest[-2:])
        rest = rest[:-2]
    if rest:
        result.append(rest)
    
    formatted = ','.join(result[::-1]) + ',' + main_part + fractional_part
    return formatted



if __name__ == "__main__":
    while(True):
        try:
            print("Enter the number:")
            num = float(input())
            print("Input:", num)
            print("Formatted:", format_indian_currency(num))
            cont = input("\nDo you want to continue? (yes/no): ").strip().lower()
            if cont not in ['yes', 'y']:
                print("Goodbye!")
                break
        except Exception:
            print("Invalid input! Please enter a valid number (digits and decimal point).")
