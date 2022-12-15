from inventory_client import InventoryClient


def get_book_titles(client, ISBNS):
    # Create an empty list to store the book titles
    titles = []

    # Loop through the list of ISBNs
    for ISBN in ISBNS:
        # Call the GetBook RPC using the client object and the current ISBN
        response = client.get_books(ISBN)

        titles.append(response.title)

    return titles


if __name__ == '__main__':
    # Create an instance of the client API object with reasonable defaults
    client = InventoryClient()

    # Call the get_book_titles function with two hardcoded ISBNs
    titles = get_book_titles(client, ['12345', '23456'])

    for title in titles:
        print(title)