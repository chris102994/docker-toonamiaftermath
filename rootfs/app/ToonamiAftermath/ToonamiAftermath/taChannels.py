from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Country:
    class Meta:
        name = "country"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class DisplayName:
    class Meta:
        name = "display-name"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Element:
    class Meta:
        name = "element"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    displayName: Optional[str] = field(
        default=None,
        metadata={
            "name": "display-name",
            "type": "Element",
            "required": True,
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    country: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    icon: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    scheduleUrl: Optional[str] = field(
        default=None,
        metadata={
            "name": "schedule_url",
            "type": "Element",
        }
    )
    episodeQueryUrl: Optional[str] = field(
        default=None,
        metadata={
            "name": "episode_query_url",
            "type": "Element",
        }
    )
    group: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    offset: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class EpisodeQueryUrl:
    class Meta:
        name = "episode_query_url"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Group:
    class Meta:
        name = "group"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Icon:
    class Meta:
        name = "icon"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Id:
    class Meta:
        name = "id"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
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
class Offset:
    class Meta:
        name = "offset"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class ScheduleUrl:
    class Meta:
        name = "schedule_url"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Url:
    class Meta:
        name = "url"

    value: Optional[str] = field(
        default=None,
        metadata={
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
