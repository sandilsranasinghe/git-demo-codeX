
# TODO make it possible to greet multiple users
def greet(name):
    """Greets the user with their name.

    This is a simple Python script that defines a function to greet a user.

    Args:
        name (str): The name of the user.
    Raises:
        ValueError: If the name is not a string.
    Returns:
        str: A greeting message.
    """

    if not isinstance(name, str):
        raise ValueError("Name must be a string")
    return f"Greetings, {name}!"


if __name__ == "__main__":
    print("Starting the program...")
    print(greet("World"))
    print("Ending the program...")
