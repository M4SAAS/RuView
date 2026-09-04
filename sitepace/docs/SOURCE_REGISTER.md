# Source Register

## Selected sources for current scope

### 1. M4SAAS/RuView
- Role: SitePace working fork and implementation base.
- Repository: `M4SAAS/RuView`
- Branch used for foundation: `sitepace/rf-foundation`
- Baseline before SitePace changes: `de099c1f2d2725d4b189fb3a405aff185df71fb3`
- Verification date: 2026-09-04
- Status: fork verified against upstream at the same commit before SitePace edits.

### 2. ruvnet/RuView
- Role: upstream source of RuView RF/CSI sensing, tracking, firmware, replay and supporting research/ADRs.
- Repository: `ruvnet/RuView`
- Verified upstream commit: `de099c1f2d2725d4b189fb3a405aff185df71fb3`
- Verification date: 2026-09-04
- License: MIT per upstream repository.

### 3. RuView repository instructions
- File: `AGENTS.md`
- Revision: `de099c1f2d2725d4b189fb3a405aff185df71fb3`
- Why selected: defines authoritative repository map, safety/evidence rules, validation commands, and hardware-validation requirements.

### 4. RuView persistent tracker
- File: `v2/crates/ruview-track/src/manager.rs`
- Revision: `de099c1f2d2725d4b189fb3a405aff185df71fb3`
- Why selected: existing anonymous persistent tracking, ambiguity handling, topology gates, and pseudonymous person/track lifecycle are directly relevant to worker movement continuity.

### 5. RuView session/replay design
- File: `docs/adr/ADR-003-rvf-cognitive-containers-csi.md`
- Revision: `de099c1f2d2725d4b189fb3a405aff185df71fb3`
- Why selected: defines session recording/replay concept for CSI time series, detections, poses, timestamps and integrity metadata.
- Status note: ADR is marked Proposed; use as design input, not as proof of production completion.

### 6. Dholera source package
- Role: geometry, site constraints, floor plans, network conditions, construction sequence and hygiene-monitoring problem definition.
- Source: existing L&T Dholera Drive package supplied in this chat.
- Use: Dholera remains the first evaluation environment; source files are not copied into Git.

## Candidate supporting open-source sources

Not yet adopted. Each candidate must be evaluated for maintenance, license, hardware requirements, reproducibility and measurable lift before it becomes a dependency.

Priority search areas:

- ESP32 CSI capture and synchronization
- WiFi CSI human activity recognition
- multi-person RF tracking
- RF tomography/localization
- passive RFID/UHF reader integration
- RFID/CSI identity association
- time-series representation learning
- self-supervised CSI embeddings
- change-point/event segmentation
- uncertainty calibration / abstention
- RF simulation and multipath modeling
- mesh / multi-AP time synchronization

## Excluded from current model scope

- CCTV/video analytics as a runtime dependency
- SitePace Checklist/BOQ/Progress model integrations
- production client deployment
- disciplinary automation
- claims of verified urination/spitting detection before controlled validation
