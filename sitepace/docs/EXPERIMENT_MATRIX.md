# Dholera RF Experiment Matrix

## Objective

Determine the practical sensing depth, spatial coverage, tracking stability, identity continuity and behavior separability achievable with a RuView-based camera-free system under representative Dholera construction conditions.

## Geometry tests

| Test | Geometry | Variable | Primary measurement |
|---|---|---|---|
| G01 | Open 7.2 m bay | 1 person | occupancy recall, CSI quality |
| G02 | Open 14.4 m / two bays | 1 person | usable sensing depth, localization stability |
| G03 | Column between person and node | concrete obstruction | track continuity, RF attenuation |
| G04 | Future blockwork between nodes/person | masonry obstruction | through-wall performance and recalibration |
| G05 | Moving scaffold | metallic multipath change | false positives, drift |
| G06 | Rebar/material stack introduced | static environment change | recalibration need |
| G07 | Material trolley/machinery movement | non-human moving mass | false-human detections |
| G08 | 2 people crossing | multi-person | ID swaps, UNKNOWN rate |
| G09 | 5 people crossing | multi-person | track continuity and capacity |
| G10 | 10 people in one cell | crowd | count error, identity ambiguity |

## Infrastructure tests

Compare local RF architectures without requiring internet:

1. one dedicated AP + 4 RuView nodes
2. one dedicated AP + 6 RuView nodes
3. two AP cells with overlap
4. ceiling AP + floor nodes
5. mesh APs
6. wireless bridge/backhaul
7. extender/repeater-assisted local cell
8. wired/fiber backhaul between cells

Measure packet loss, CSI frame rate, timing drift, node synchronization, RF interference, coverage, recovery after node/AP move, and configuration effort.

## Identity tests

First passive identity candidate: UHF RFID.

| Test | Scenario | Expected safe behavior |
|---|---|---|
| I01 | one worker / one credential / one track | bind if unambiguous |
| I02 | credential not read | continue anonymous track; never mark absent |
| I03 | two workers cross after one checkpoint | retain IDs only if continuity remains unambiguous |
| I04 | conflicting credential and track | identity = AMBIGUOUS |
| I05 | track lost then credential reread | rebind as new auditable association |
| I06 | two credentials read in one RF zone | do not force one-to-one association without evidence |

## Behavior discovery tests

Every positive behavior must be paired with visually/sensor-ground-truthed controlled trials during R&D only. The production model remains camera-free.

Hard negatives include:

- drilling/hammering/fixing a nail
- wall marking and measuring
- tying wire/rebar
- painting
- accessing a tool belt
- accessing a trouser pocket
- adjusting clothing
- cleaning
- pouring water
- drinking
- crouching
- resting/leaning on a column
- phone use
- low-level electrical/plumbing work
- lifting/carrying material

Candidate target episodes:

- urination-like action
- actual controlled liquid urination proxy during lab validation where ethically/operationally acceptable
- spit-like head/hand sequence
- controlled spit proxy / liquid droplet event where suitable for lab research
- litter drop and leave

## Sequence windows

For each episode retain and evaluate:

- T-30s to T-10s: context
- T-10s to onset: pre-event
- onset to end: during
- end to T+10s: immediate post-event
- T+10s to T+60s: environmental aftermath

Train/evaluate in this order:

1. retrospective full-window separability
2. shorter retrospective window
3. during-event detection
4. onset/early-event detection

Do not attempt prediction until retrospective separability is measured.

## Acceptance metrics

The primary safety metric is false attribution, not overall accuracy.

Record:

- false accusations per worker-hour
- false verified incidents per 1,000 hard-negative episodes
- identity swap rate
- UNKNOWN/abstention rate
- event precision
- event recall
- localization error
- track fragmentation
- recalibration frequency
- node/AP downtime and recovery

No production claim is allowed without target-hardware and representative-environment evidence.