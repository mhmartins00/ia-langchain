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
    """Multiply two integers

    Args:
        a: First integer
        b: Second integer
    """
    return a*b

@tool
def imposto(x: float) -> float:
    """Calcula o valor do imposto do haddad aplicado em um valor

    Args:
        x: valor a ser aplicado o imposto
    """
    return x*0.92

@tool
def users_in_product_client_id(clientId: str) -> int:
    """Returns the number of users in a given product identified by its clientId

    Args:
        clientId: clientId of the product
    """
    users = {
        'gambi': 10,
        'treco': 20
    }
    return users.get(clientId.lower(), None)

@tool
def client_id_of_product(product: str) -> int:
    """Returns the clientId of a given product

    Args:
        product: name of product
    """
    clientId = {
        'alguma gambiarra': 'gambi',
        'outro treco': 'treco'
    }
    return clientId.get(product.lower(), None)