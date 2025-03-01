#স্বাভাবিক ক্রমিক সংখ্যার যোগফল নির্ণয়

def sum_of_natural_numbers(n):
    """
    1 theke n porjonto shadharon kromik shongkhar jogfol ber kore.

    Args:
        n: shesh shongkha.

    Returns:
        jogfol.
    """

    if n < 1:
        return "n obboshyoi 1 ba tar beshi hote hobe."

    return n * (n + 1) // 2

# User theke input neoar jonno
try:
    n_input = int(input("shesh shongkhata likhun: "))
    result_input = sum_of_natural_numbers(n_input)
    print(f"1 theke {n_input} porjonto shadharon kromik shongkhar jogfol: {result_input}")
except ValueError:
    print("onugroho kore ekta purno shongkha likhun.")