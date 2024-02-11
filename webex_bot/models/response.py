from __future__ import annotations

import json
from typing import Any, Dict, List, Optional

from webexteamssdk.models.cards import AdaptiveCard


def response_from_adaptive_card(adaptive_card: AdaptiveCard) -> Response:
    """
    Convenience method for generating a Response from an AdaptiveCard.

    @param adaptive_card: AdaptiveCard object
    @return: Response object
    """

    response = Response()
    response.text = "This bot requires a client which can render cards."
    response.markdown = "This bot requires a client which can render cards."
    response.attachments = {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content": adaptive_card.to_dict()
    }

    return response


def response_custom_format(text: str,
                           markdown: str,
                           files: List[str] = None,
                           attachments: List[Dict[str, str]] = None
                           ) -> Response:
    """
    Convenience method for generating a Response from a custom format.

    @param text: The text content of the response.
    @param markdown: The response content in markdown format.
    @param files: A list of file attachments associated with the response.
    @param attachments: A list of additional attachments associated with the response.
    @return: Response object
    """
    response = Response()
    response.text = text
    response.markdown = markdown

    if files:
        response.files = files
    if attachments:
        response.attachments = attachments

    return response


class Response(object):
    """
    Represents a response object. This object is used to send a response to a message in a room.

    :param attributes: Optional dictionary of attributes
    """

    def __init__(self, attributes: Optional[Dict[str, Any]] = None) -> None:
        """
        Initializes a new Response object.

        :param attributes: Optional dictionary containing the attributes of the response.
        :type attributes: dict, optional

        :ivar text: The text content of the response.
        :vartype text: str
        :ivar roomId: The ID of the room associated with the response.
        :vartype roomId: str
        :ivar parentId: The ID of the parent response, if applicable.
        :vartype parentId: str
        :ivar markdown: The response content in markdown format.
        :vartype markdown: str
        :ivar html: The response content in HTML format.
        :vartype html: str
        :ivar files: A list of file attachments associated with the response.
        :vartype files: list
        :ivar attachments: A list of additional attachments associated with the response.
        :vartype attachments: list
        """
        if attributes:
            self.attributes = attributes
        else:
            self.attributes = dict()
            self.attributes["text"] = None
            self.attributes["roomId"] = None
            self.attributes["parentId"] = None
            self.attributes["markdown"] = None
            self.attributes["html"] = None
            self.attributes["files"] = list()
            self.attributes["attachments"] = list()

    @property
    def text(self) -> str:
        """
        Get the text attribute of the response.

        :return: The text attribute
        """
        return self.attributes["text"]

    @text.setter
    def text(self, val):
        """
        Set the text attribute of the response.

        :param val: The value to set
        """
        self.attributes["text"] = val

    @property
    def files(self) -> List[str]:
        """
        Get the files attribute of the response.

        :return: The files attribute
        """
        return self.attributes["files"]

    @files.setter
    def files(self, val):
        """
        Set the files attribute of the response.

        :param val: The value to set
        """
        self.attributes["files"].append(val)

    @property
    def attachments(self) -> List[str]:
        """
        Get the attachments attribute of the response.

        :return: The attachments attribute
        """
        return self.attributes["attachments"]

    @attachments.setter
    def attachments(self, val):
        """
        Set the attachments attribute of the response.

        :param val: The value to set
        """
        self.attributes["attachments"].append(val)

    @property
    def roomId(self) -> str:
        """
        Get the roomId attribute of the response.

        :return: The roomId attribute
        """
        return self.attributes["roomId"]

    @roomId.setter
    def roomId(self, val):
        """
        Set the roomId attribute of the response.

        :param val: The value to set
        """
        self.attributes["roomId"] = val

    @property
    def parentId(self) -> str:
        """
        Get the parentId attribute of the response.

        :return: The parentId attribute
        """
        return self.attributes["parentId"]

    @parentId.setter
    def parentId(self, val):
        """
        Set the parentId attribute of the response.
        :param val: The value to set
        """
        self.attributes["parentId"] = val

    @property
    def markdown(self) -> str:
        """
        Get the markdown attribute of the response.
        :return: The markdown attribute
        """
        return self.attributes["markdown"]

    @markdown.setter
    def markdown(self, val):
        """
        Set the markdown attribute of the response. Use this to send markdown content in the response.

        :param val: The value to set
        """
        self.attributes["markdown"] = val

    @property
    def html(self) -> str:
        """
        Get the html attribute of the response.

        :return: The html attribute
        """
        return self.attributes["html"]

    @html.setter
    def html(self, val):
        """
        Set the html attribute of the response. Use this to send HTML content in the response.

        :param val: The value to set
        """
        self.attributes["html"] = val

    def as_dict(self) -> Dict[str, Any]:
        """
        Convert the response object to a dictionary.

        :return: The response as a dictionary
        """
        ret = dict()
        for k, v in self.attributes.items():
            if v:
                ret[k] = v
        return ret

    def json(self) -> str:
        """
        Convert the response object to a JSON string.

        :return: The response as a JSON string
        """
        return json.dumps(self.attributes)
