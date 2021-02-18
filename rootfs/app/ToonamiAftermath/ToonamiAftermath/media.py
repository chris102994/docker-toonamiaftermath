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
class Channel:
    class Meta:
        name = "channel"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class ChannelUrl:
    class Meta:
        name = "channelUrl"

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
        }
    )
    year: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Lang:
    class Meta:
        name = "lang"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
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
class QueryUrl:
    class Meta:
        name = "queryUrl"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class StartDate:
    class Meta:
        name = "startDate"

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class StopDate:
    class Meta:
        name = "stopDate"

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Year:
    class Meta:
        name = "year"

    value: Optional[int] = field(
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
            "type": "Element",
        }
    )
    channel: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    channelUrl: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    episodeNumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    info: Optional[Info] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    mediaType: Optional["Element.Value"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    queryUrl: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    startDate: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    stopDate: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
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
