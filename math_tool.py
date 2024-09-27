from langchain_core.tools import tool

@tool
def add(a: int, b: int) -> int:
    """Add two integers.

    Args:
        a: First integer
        b: Second integer
    """
    return a + b

@tool
def multiply(a: int, b: int) -> int:
    """Multiplicação de dois numeros

    Args:
        a: First integer
        b: Second integer
    """
    result = a * b
    return result