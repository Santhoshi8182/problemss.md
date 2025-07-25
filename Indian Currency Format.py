def format_indian_currency(number):
    parts = str(number).split('.')
    integer_part = parts[0]
    decimal_part = '.' + parts[1] if len(parts) > 1 else ''
    
    if len(integer_part) <= 3:
        return integer_part + decimal_part
    
    # First group (last 3 digits)
    result = integer_part[-3:]
    integer_part = integer_part[:-3]
    
    # Rest groups (2 digits)
    while len(integer_part) > 0:
        result = integer_part[-2:] + ',' + result
        integer_part = integer_part[:-2]
    
    return result + decimal_part

# Example usage:
print(format_indian_currency(123456.7891))  # Output: 1,23,456.7891
