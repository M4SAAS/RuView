# Hardware Strategy — Dholera First

## Objective

Find the cheapest, fastest and most reliable hardware topology that preserves useful CSI sensing across a changing construction floor without requiring worker-carried batteries or continuous internet.

## Fixed/mobile sensing infrastructure

### Preferred first sensing family

ESP32-S3 / ESP32-C6 class nodes, because the RuView fork already supports this family and Espressif's official `esp-csi` project provides reference CSI collection patterns.

Official Espressif reference patterns to benchmark:

1. **Router CSI** — one ESP32 receives CSI from router ping replies. Lowest hardware count, but depends on router position/protocol.
2. **Device-to-device CSI through router** — two or more ESP32 devices create more useful paths while still using an AP.
3. **Dedicated broadcast packet source + multiple ESP32 receivers** — more hardware, but Espressif documents this as the highest-accuracy/reliability reference among its three basic modes for multi-device positioning/sensing.

For Dholera, do not choose the topology from theory. Benchmark all three against the actual bay/blockwork/scaffolding tests.

## AP/router strategy

Internet and sensing transport are separate design concerns.

Candidate deployment patterns:

- portable local AP + 4–6 sensing nodes per test cell
- multiple overlapping AP cells
- ceiling-mounted APs where final overhead installation is stable
- movable AP stands during active construction
- WiFi mesh only where its channel management does not destabilize CSI collection
- wireless bridge for backhaul between isolated cells
- wired/fiber backbone with local APs where available
- extenders only after measuring their effect on CSI timing/channel stability

A router or extender is not automatically useful just because it increases internet coverage. The sensing evaluation must record channel, bandwidth, packet source, timing, link geometry and interference for each cell.

## Antenna strategy

Espressif's reference notes that external IPEX antennas generally perform better than PCB antennas and that PCB antennas are directional. Therefore the foundation experiment should compare:

- stock PCB antenna node
- external omnidirectional antenna node
- fixed antenna orientation
- rotated antenna orientation
- node height and mounting face

Do not standardize enclosure or antenna until these measurements are available.

## Power strategy

Preferred for infrastructure nodes:

- mains adapter where protected supply exists
- PoE-to-DC splitter where Ethernet/PoE infrastructure is practical
- protected low-voltage distribution for temporary clusters
- UPS/power-bank only as test/temporary fallback

Worker identity must not depend on worker charging.

## Passive identity strategy

First implementation candidate: passive UHF RFID credential.

Forms to evaluate:

- ID card
- helmet tag/sticker
- reusable wristband

Fixed/mobile RFID readers provide observations to the identity-binding service; no worker-carried battery is required.

RFID observations are not presence truth. A missed read remains `UNKNOWN` and does not mark the worker absent or inactive.

## First pilot BOM class

Quantity ranges are experiment quantities, not a deployment BOQ:

- 6–12 ESP32-S3/C6 CSI nodes
- 2 configurable WiFi APs/routers
- 1 dedicated packet-source ESP32 for broadcast-mode tests
- 1 local edge laptop/mini-PC
- 1 UHF RFID reader with 2–4 antennas for checkpoint/portal tests
- 20–50 passive UHF credentials in mixed card/tag/wristband form
- protected mounts, enclosures, power supplies and network cabling

## Selection gates

Hardware is promoted only after measuring:

- CSI frame continuity
- signal-to-noise / usable subcarrier fraction
- range and obstruction performance
- multi-person tracking stability
- recovery after node/AP relocation
- recalibration time
- construction-interference sensitivity
- BOM cost per reliably covered m² / zone
- setup time per sensing cell

## External source selected

`espressif/esp-csi` — official Espressif CSI reference implementation, Apache-2.0 licensed. Use as a supporting hardware/capture reference, not as a silent runtime dependency until sample-based evaluation shows a benefit over the RuView firmware path.
