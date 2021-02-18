from dataclasses import dataclass, field
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
        metadata={
            "required": True,
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

    creators: List[str] = field(
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
            "type": "Element",
            "required": True,
        }
    )
    epNum: Optional[int] = field(
        default=None,
        metadata={
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

    genres: List[str] = field(
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
class SearchedYear:
    class Meta:
        name = "searchedYear"

    value: Optional[int] = field(
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

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


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
        metadata={
            "required": True,
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

    aka: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    contentRating: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    createdAt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    creators: Optional[Creators] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
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
    imdbId: Optional[str] = field(
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
    productionCo: Optional[ProductionCo] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    queryUrl: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    rating: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    release: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    releaseDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    searchedName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    searchedYear: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    series: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    storyline: Optional[str] = field(
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
    tagline: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    updatedAt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "_id",
            "type": "Element",
            "required": True,
        }
    )
    v: Optional[int] = field(
        default=None,
        metadata={
            "name": "__v",
            "type": "Element",
            "required": True,
        }
    )


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
