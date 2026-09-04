from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Iterable, Optional


class IdentityState(str, Enum):
    UNKNOWN = "UNKNOWN"
    CONFIRMED = "CONFIRMED"
    AMBIGUOUS = "AMBIGUOUS"


@dataclass(frozen=True)
class CredentialObservation:
    credential_uid: str
    worker_uid: str
    zone_id: str
    timestamp_ms: int


@dataclass(frozen=True)
class TrackObservation:
    track_id: str
    person_id: str
    zone_id: str
    timestamp_ms: int


@dataclass(frozen=True)
class IdentityBinding:
    state: IdentityState
    track_id: str
    person_id: str
    worker_uid: Optional[str] = None
    credential_uid: Optional[str] = None
    reason: str = ""


def bind_identity(
    track: TrackObservation,
    credentials: Iterable[CredentialObservation],
    *,
    time_window_ms: int = 3000,
) -> IdentityBinding:
    """Bind a RuView track to a passive credential without guessing.

    A binding is CONFIRMED only when exactly one unique credential/worker pair
    is observed in the same zone within the configured time window. Missing or
    conflicting reads abstain instead of producing a worker attribution.
    """
    if time_window_ms < 0:
        raise ValueError("time_window_ms must be non-negative")

    matches = [
        c
        for c in credentials
        if c.zone_id == track.zone_id
        and abs(c.timestamp_ms - track.timestamp_ms) <= time_window_ms
    ]

    unique_pairs = {(m.credential_uid, m.worker_uid) for m in matches}

    if not unique_pairs:
        return IdentityBinding(
            state=IdentityState.UNKNOWN,
            track_id=track.track_id,
            person_id=track.person_id,
            reason="no credential observation in zone/time window",
        )

    if len(unique_pairs) > 1:
        return IdentityBinding(
            state=IdentityState.AMBIGUOUS,
            track_id=track.track_id,
            person_id=track.person_id,
            reason="multiple credential/worker candidates in zone/time window",
        )

    credential_uid, worker_uid = next(iter(unique_pairs))
    return IdentityBinding(
        state=IdentityState.CONFIRMED,
        track_id=track.track_id,
        person_id=track.person_id,
        worker_uid=worker_uid,
        credential_uid=credential_uid,
        reason="single unambiguous credential/worker candidate",
    )
