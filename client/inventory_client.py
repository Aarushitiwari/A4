import grpc
import sys
sys.path.append('./service')
import service_pb2 as pb2
import service_pb2_grpc as pb2_grpc

class InventoryClient:
    """
    Client for gRPC functionality
    """

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = pb2_grpc.InventoryServiceStub(self.channel)

    def get_books(self, ISBN):
        """
        Client function to call the rpc for GetServerResponse
        """
        books = pb2.GetBookRequest(ISBN=ISBN)
        print(f'{books}')
        return self.stub.GetBook(books)