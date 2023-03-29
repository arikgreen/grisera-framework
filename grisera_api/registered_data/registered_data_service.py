from graph_api_service import GraphApiService
from registered_data.registered_data_model import (
    RegisteredDataIn,
    RegisteredDataNodesOut,
    BasicRegisteredDataOut,
    RegisteredDataOut,
)
from models.not_found_model import NotFoundByIdModel
from models.relation_information_model import RelationInformation


class RegisteredDataService:
    """
    Abstract class to handle logic of registered data requests

    """

    def save_registered_data(self, registered_data: RegisteredDataIn):
        """
        Send request to graph api to create new registered data node

        Args:
            registered_data (RegisteredDataIn): Registered data to be added

        Returns:
            Result of request as registered data object
        """
        raise Exception("save_registered_data not implemented yet")

    def get_registered_data_nodes(self):
        """
        Send request to graph api to get registered_data_nodes

        Returns:
            Result of request as list of registered_data_nodes objects
        """
        raise Exception("get_registered_data_nodes not implemented yet")

    def get_registered_data(self, registered_data_id: Union[int, str]):
        """
        Send request to graph api to get given registered data

        Args:
        registered_data_id (int): Id of registered data

        Returns:
            Result of request as registered data object
        """
        raise Exception("get_registered_data not implemented yet")

    def delete_registered_data(self, registered_data_id: Union[int, str]):
        """
        Send request to graph api to delete given registered data

        Args:
        registered_data_id (int): Id of registered data

        Returns:
            Result of request as registered data object
        """
        raise Exception("delete_registered_data not implemented yet")

    def update_registered_data(
        self, registered_data_id: Union[int, str], registered_data: RegisteredDataIn
    ):
        """
        Send request to graph api to update given registered data

        Args:
        registered_data_id (int): Id of registered data
        registered_data (RegisteredDataIn): Properties to update

        Returns:
            Result of request as registered data object
        """
        raise Exception("update_registered_data not implemented yet")
