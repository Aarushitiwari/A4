from concurrent.futures import ThreadPoolExecutor

import grpc

import book_pb2
import service_pb2
import service_pb2_grpc


# Hardcoded "database" of books
books = {
    "12345": book_pb2.Book(
        ISBN="12345",
        title="Book 1",
        author="Author 1",
        genre=1,
        publishing_year=2010,
    ),
    "23456": book_pb2.Book(
        ISBN="23456",
        title="Book 2",
        author="Author 2",
        genre=2,
        publishing_year=2015,
    ),
    "34567": book_pb2.Book(
        ISBN="34567",
        title="Book 3",
        author="Author 3",
        genre=3,
        publishing_year=2020,
    ),
}


class InventoryServiceServicer(service_pb2_grpc.InventoryServiceServicer):

    def CreateBook(self, request, context):
        # Add the book to the inventory
        ISBN = request.ISBN
        books[ISBN] = request

        # Return a response indicating success
        return service_pb2.CreateBookResponse(success=True)

    def GetBook(self, request, context):
        # Retrieve the book from the inventory
        ISBN = request.ISBN
        book = books.get(ISBN)

        # Return the book if it exists, otherwise return None
        return book if book else None


def main():
    # Create a gRPC server
    server = grpc.server(ThreadPoolExecutor(max_workers=10))

    # Add the InventoryServiceServicer to the server
    service_pb2_grpc.add_InventoryServiceServicer_to_server(
        InventoryServiceServicer(), server
    )

    # Start the server
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Server started, listening on 50051")
    server.wait_for_termination()


if __name__ == '__main__':
    main()
