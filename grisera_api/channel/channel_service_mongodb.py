from typing import Union
from channel.channel_service import ChannelService
from channel.channel_model import ChannelIn, ChannelOut, ChannelsOut, BasicChannelOut
from grisera_api.mongo_service.service_mixins import (
    GenericMongoServiceMixin,
    ModelClasses,
)


class ChannelServiceMongoDB(ChannelService, GenericMongoServiceMixin):
    """
    Object to handle logic of channel requests

    Attributes:
    registered_channel_service (RegisteredChannelService): Service to send registered channel requests
    """

    def __init__(self, registered_channel_service):
        self.model_classes = ModelClasses(
            basic_out_class=BasicChannelOut, out_class=ChannelOut
        )
        self.registered_channel_service = registered_channel_service

    def save_channel(self, channel: ChannelIn):
        """
        Send request to mongo api to create new channel. This method uses mixin get implementation.

        Args:
            channel (ChannelIn): Channel to be added

        Returns:
            Result of request as channel object
        """
        return self.create(channel)

    def get_channels(self):
        """
        Send request to mongo api to get all channels. This method uses mixin get implementation.

        Returns:
            Result of request as ChannelsOut object
        """
        result_dicts = self.get_many_dict()
        return ChannelsOut(channels=result_dicts)

    def get_channel(self, channel_id: Union[str, int]):
        """
        Send request to mongo api to get given channel. This method uses mixin get implementation.

        Args:
            channel_id (int): Id of channel

        Returns:
            Result of request as channel object
        """
        return self.get_single(channel_id)

    def get_channel_traverse(
        self, channel_id: Union[str, int], depth: int, source: str
    ):
        """
        Send request to mongo api to get given channel with related models. This method uses mixin get implementation.

        Args:
            channel_id (int): Id of channel
            depth (int): this attribute specifies how many models will be traversed to create the response.
                         for depth=0, only no further models will be travesed.
            source (str): internal argument for mongo services, used to tell the direction of model fetching.

        Returns:
            Result of request as channel dictionary
        """
        return self.get_single_traverse(channel_id, depth, source)

    def _add_related_documents(self, channel: dict, depth: int, source: str):
        if source != "recording" and depth > 0:
            channel[
                "registered_channels"
            ] = self.registered_channel_service.get_registered_channels_traverse(
                {"channel_id": channel["id"]},
                depth=depth - 1,
                source="channel",
            )
