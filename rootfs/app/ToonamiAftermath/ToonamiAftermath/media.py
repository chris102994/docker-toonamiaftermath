from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlDateTime


@dataclass
class BlockName:
    class Meta:
        name = "blockName"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Episode:
    class Meta:
        name = "episode"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class EpisodeNumber:
    class Meta:
        name = "episodeNumber"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Fullname:
    class Meta:
        name = "fullname"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Image:
    class Meta:
        name = "image"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Info:
    class Meta:
        name = "info"

    episode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fullname: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    image: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    year: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class MediaType:
    class Meta:
        name = "mediaType"

    value: Optional["MediaType.Value"] = field(
        default=None,
    )

    class Value(Enum):
        SERIES = "series"
        SHORT = "short"
        MOVIE = "movie"


@dataclass
class Name:
    class Meta:
        name = "name"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )

@dataclass
class Year:
    class Meta:
        name = "year"

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Element:
    class Meta:
        name = "element"

    blockName: Optional[str] = field(
        default=None,
        metadata={
            "name": "blockName",
            "type": "Element",
            "required": True,
        }
    )
    episodeNumber: Optional[int] = field(
        default=None,
        metadata={
            "name": "episodeNumber",
            "type": "Element",
        }
    )
    info: Optional[Info] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    mediaType: Optional["Element.Value"] = field(
        default=None,
        metadata={
            "name": "mediaType",
            "type": "Element",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )

    startDate: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "startDate",
            "type": "Element",
            "required": True,
        }
    )

    stopDate: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "stopDate",
            "type": "Element",
            "required": True,
        }
    )

    queryUrl: Optional[str] = field(
        default=None,
        metadata={
            "name": "queryUrl",
            "type": "Element",
            "required": True,
        }
    )

    channelUrl: Optional[str] = field(
        default=None,
        metadata={
            "name": "channelUrl",
            "type": "Element",
            "required": True,
        }
    )

    lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "lang",
            "type": "Element",
            "required": True,
        }
    )

    channel: Optional[str] = field(
        default=None,
        metadata={
            "name": "channel",
            "type": "Element",
            "required": True,
        }
    )

    class Value(Enum):
        SERIES = "series"
        SHORT = "short"
        MOVIE = "movie"


@dataclass
class Root:
    class Meta:
        name = "root"

    element: List[Element] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
