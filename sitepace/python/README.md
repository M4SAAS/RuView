# SitePace RF Python Foundation

The first adapter implements conservative binding between an anonymous RuView track and passive credential observations.

Run the focused tests from this directory:

```bash
PYTHONPATH=. python -m unittest discover -s tests -v
```

The binder intentionally abstains:

- no credential read -> `UNKNOWN`
- more than one credential/worker candidate -> `AMBIGUOUS`
- exactly one same-zone, in-window credential/worker pair -> `CONFIRMED`

A missed credential read must never be interpreted as worker absence or non-compliance.
