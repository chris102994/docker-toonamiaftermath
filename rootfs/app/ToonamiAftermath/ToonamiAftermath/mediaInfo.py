from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlDateTime


@dataclass
class V:
    class Meta:
        name = "__v"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Id:
    class Meta:
        name = "_id"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class AirDate:
    class Meta:
        name = "airDate"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Aka:
    class Meta:
        name = "aka"

    value: Optional[str] = field(
        default=None,
    )
    null: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class ContentRating:
    class Meta:
        name = "contentRating"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class CreatedAt:
    class Meta:
        name = "createdAt"

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Creators:
    class Meta:
        name = "creators"

    creator: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class EpNum:
    class Meta:
        name = "epNum"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Episode:
    class Meta:
        name = "episode"

    airDate: Optional[str] = field(
        default=None,
        metadata={
            "name": "airDate",
            "type": "Element",
            "required": True,
        }
    )
    epNum: Optional[int] = field(
        default=None,
        metadata={
            "name": "epNum",
            "type": "Element",
            "required": True,
        }
    )
    image: Optional[str] = field(
        default=None,
        metadata={
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
    season: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    summary: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Genres:
    class Meta:
        name = "genres"

    genre: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
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
class ImdbId:
    class Meta:
        name = "imdbId"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


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
class ProductionCo:
    class Meta:
        name = "productionCo"

    productionCo: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Rating:
    class Meta:
        name = "rating"

    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Release:
    class Meta:
        name = "release"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class ReleaseDate:
    class Meta:
        name = "releaseDate"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class SearchedName:
    class Meta:
        name = "searchedName"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Season:
    class Meta:
        name = "season"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Series:
    class Meta:
        name = "series"

    value: Optional["Series.Value"] = field(
        default=None,
    )

    class Value(Enum):
        FALSE_VALUE = "False"
        TRUE_VALUE = "True"


@dataclass
class Storyline:
    class Meta:
        name = "storyline"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Summary:
    class Meta:
        name = "summary"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Tagline:
    class Meta:
        name = "tagline"

    value: Optional[str] = field(
        default=None,
    )
    null: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class UpdatedAt:
    class Meta:
        name = "updatedAt"

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

    v: Optional[int] = field(
        default=None,
        metadata={
            "name": "__v",
            "type": "Element",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "_id",
            "type": "Element",
        }
    )
    aka: Optional[Aka] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    contentRating: Optional[str] = field(
        default=None,
        metadata={
            "name": "contentRating",
            "type": "Element",
        }
    )
    createdAt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "createdAt",
            "type": "Element",
        }
    )
    creators: Optional[Creators] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    episode: Optional[Episode] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    genres: Optional[Genres] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    image: Optional[str] = field(
        default=None,
        metadata={
            "name": "image",
            "type": "Element",
        }
    )
    imdbId: Optional[str] = field(
        default=None,
        metadata={
            "name": "imdbId",
            "type": "Element",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    productionCo: Optional[ProductionCo] = field(
        default=None,
        metadata={
            "name": "productionCo",
            "type": "Element",
        }
    )
    rating: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    release: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    releaseDate: Optional[str] = field(
        default=None,
        metadata={
            "name": "releaseDate",
            "type": "Element",
        }
    )
    searchedName: Optional[str] = field(
        default=None,
        metadata={
            "name": "searchedName",
            "type": "Element",
        }
    )
    searchedYear: Optional[str] = field(
        default=None,
        metadata={
            "name": "searchedYear",
            "type": "Element",
        }
    )
    series: Optional["Element.Value"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    storyline: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    summary: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    tagline: Optional[Tagline] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    updatedAt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "updatedAt",
            "type": "Element",
        }
    )
    queryUrl: Optional[str] = field(
        default=None,
        metadata={
            "name": "queryUrl",
            "type": "Element",
        }
    )

    class Value(Enum):
        FALSE_VALUE = "False"
        TRUE_VALUE = "True"


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