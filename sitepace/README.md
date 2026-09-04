# SitePace RF Behavior Foundation

This directory is the SitePace-specific development layer on top of the RuView fork.

## Scope

Primary initial problem: determine how far camera-free RF sensing can solve the L&T Dholera construction-site hygiene monitoring problem using RuView and compatible low-cost/open technologies.

The first target is not a finished urination/spitting classifier. The first target is a reproducible sensing, recording, identity, replay, and evaluation foundation that lets us measure what information is actually present in the RF signal under Dholera-like conditions.

## Hard constraints

- No CCTV dependency in this model.
- No accusation from an ambiguous classification or identity association.
- UNKNOWN is a valid and preferred outcome over a wrong attribution.
- Worker identity mechanisms should avoid worker-maintained charging wherever practical.
- Internet connectivity must not be required for local sensing or recording.
- Architecture must support movable/temporary RF nodes as the construction layout changes.
- All performance claims must be labelled MEASURED, CLAIMED, SYNTHETIC, or UNKNOWN.
- Raw CSI, worker identifiers, and personal data must not be committed to Git.

## Foundation layers

1. RF capture and multi-node geometry
2. Continuous session recording and deterministic replay
3. Anonymous person tracking and zone continuity
4. Passive worker identity binding (RFID first; other methods evaluated empirically)
5. Temporal event segmentation (before/during/after)
6. Behaviour classifiers with hard-negative construction tasks
7. Evidence fusion and false-accusation gates
8. Dholera floor/zone deployment planning
9. Site-independent configuration for reuse across SitePace clients

## Upstream baseline

Fork: `M4SAAS/RuView`
Upstream: `ruvnet/RuView`
Pinned foundation baseline: `de099c1f2d2725d4b189fb3a405aff185df71fb3`
Verified aligned on 2026-09-04 before SitePace changes.

See `sitepace/docs/FOUNDATION.md` and `sitepace/docs/SOURCE_REGISTER.md`.