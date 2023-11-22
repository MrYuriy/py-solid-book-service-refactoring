from app.book import Book
from app.display import ConsoleDisplayBook, ReverseDisplayBook
from app.printer import ConsolePrintBook, ReversePrintBook
from app.serializers import JsonSerializer, SerializerXML


def display(book: Book, display_type: str) -> None:
    displaying = {
        "console": ConsoleDisplayBook,
        "reverse": ReverseDisplayBook,
    }
    display_action = displaying[display_type]
    if display_action:
        display_action(book).display()
    else:
        raise ValueError(f"Unknown display type: {display_type}")


def print_book(book: Book, print_type: str) -> None:
    printing = {
        "console": ConsolePrintBook,
        "reverse": ReversePrintBook,
    }
    print_action = printing[print_type]
    if print_action:
        print_action(book).print_book()
    else:
        raise ValueError(f"Unknown print type: {print_type}")


def serialize(book: Book, serialize_type: str) -> str:
    serialization = {
        "json": JsonSerializer,
        "xml": SerializerXML,
    }
    serialize_action = serialization[serialize_type]
    if serialize_action:
        return serialize_action(book).serialize()
    else:
        raise ValueError(f"Unknown serialize type: {serialize_type}")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            display(book, method_type)
        elif cmd == "print":
            print_book(book, method_type)
        elif cmd == "serialize":
            return serialize(book, method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))