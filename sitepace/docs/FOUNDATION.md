# SitePace RF Behavior & Workforce Intelligence — Foundation

## Goal

Build a camera-free, construction-ready RF sensing model beginning with L&T Dholera and reusable across SitePace clients.

The foundation must answer, with evidence:

1. What spatial scale can RuView-class CSI sensing reliably cover in open construction and after blockwork?
2. How many movable/fixed RF nodes, APs/routers, and repeaters are needed for stable sensing and local transport?
3. Can continuous CSI sessions be recorded and replayed without internet?
4. Can anonymous tracks remain continuous through changing construction geometry?
5. Can passive credentials bind anonymous tracks to worker UIDs without battery dependency?
6. Which behaviors are separable from ordinary construction tasks using retrospective before/during/after analysis?
7. What evidence threshold is required before any incident can be attributed to a specific worker?

## Dholera-first strategy

### Phase 0 — Foundation and reproducibility

- Pin RuView revision and preserve upstream history.
- Use a SitePace-specific branch/directory rather than rewriting upstream core prematurely.
- Define hardware inventory and topology schema.
- Define session format for raw CSI, node geometry, timestamps, derived detections, and replay metadata.
- Define explicit evidence states: `UNKNOWN`, `CANDIDATE`, `SUPPORTED`, `VERIFIED`.
- Define privacy/data-retention boundaries before collecting worker-linked data.

### Phase 1 — RF field characterization

Create repeatable experiments across representative geometries:

- open 7.2 m structural bay
- two-bay 14.4 m separation
- column shadowing
- future blockwork between nodes
- moving scaffolding
- steel/rebar/material stacks
- single person
- multiple people crossing
- static construction work
- moving machinery

Record packet/CSI quality, occupancy recall, localization consistency, track continuity, and recalibration requirements.

### Phase 2 — Continuous recording and replay

Build an always-on local recorder so events can be analyzed retrospectively.

Required outputs:

- raw CSI or validated source frames
- amplitude/phase/SNR metadata
- node/AP geometry
- synchronized timestamps
- anonymous track IDs
- zone transitions
- derived motion/activity features
- configuration/version hashes
- replay command and deterministic result summary

No internet dependency for capture or replay.

### Phase 3 — Identity binding without worker charging

First candidate: passive UHF RFID credentials.

Identity is separate from RuView tracking:

`WorkerUID <- CredentialUID <- observation checkpoint/zone <- RuView PersonID/TrackID`

Rules:

- missing credential read does not mean absent/non-compliant
- ambiguous binding returns UNKNOWN
- identity binding must be auditable and confidence-scored
- no disciplinary output if identity continuity is unresolved

Other candidate identity methods may be tested only if they improve accuracy/cost/operability.

### Phase 4 — Behavior discovery from complete episodes

Do not begin with a binary 'urination' model.

First determine whether the signal contains separable information using controlled episodes and hard negatives.

Window structure:

- pre-event
- onset
- during
- post-event
- persistent environmental change, if any

Hard negatives must include real construction actions such as drilling, tying, painting, measuring, tool-belt access, pocket access, adjusting clothing, cleaning, pouring water, resting, crouching, and wall-facing work.

### Phase 5 — Event models

Only after separability is demonstrated:

- retrospective completed-event classifier
- during-event classifier
- early-event detector
- event localization
- identity association
- evidence package generation

## Hardware architecture to evaluate

### Sensing nodes

- ESP32-S3 and/or ESP32-C6 CSI nodes supported by RuView
- movable protected enclosures
- ceiling/column temporary mounts
- local mains/PoE-powered infrastructure preferred over worker-carried batteries

### RF infrastructure

Compare:

- dedicated WiFi AP per sensing cell
- multiple APs per floor
- ceiling-mounted APs
- mesh WiFi
- wireless bridges
- extenders/repeaters
- wired/fiber backhaul with local WiFi sensing cells

Internet access is optional. Local WiFi and local LAN transport are independent requirements.

### Passive identity

Compare:

- UHF RFID card
- UHF RFID helmet tag
- UHF RFID wristband
- NFC/HF RFID checkpoints

Reader placement must be engineered separately from CSI placement.

## Acceptance philosophy

This model is high-consequence because a false attribution can accuse a worker incorrectly.

Therefore:

- optimize precision before recall
- measure false accusations per worker-hour/event opportunity
- use hard-negative adversarial testing
- require reproducible evidence for every promoted model
- prefer missed events to unsupported accusations
- keep raw/derived evidence replayable for review

## Initial repository deliverables

- foundation scope
- source register
- hardware evaluation matrix
- Dholera experiment matrix
- session/replay schema
- identity binding schema
- event/evidence schema
- first runnable recorder/replayer adapter
- tests for UNKNOWN/ambiguity handling
- deployment notes for movable construction-site RF cells
