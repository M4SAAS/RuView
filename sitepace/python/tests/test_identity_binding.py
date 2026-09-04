import unittest

from sitepace_rf.identity_binding import (
    CredentialObservation,
    IdentityState,
    TrackObservation,
    bind_identity,
)


class IdentityBindingTests(unittest.TestCase):
    def setUp(self):
        self.track = TrackObservation("track_1", "person_7", "zone_A", 10_000)

    def test_one_matching_credential_confirms(self):
        result = bind_identity(
            self.track,
            [CredentialObservation("cred_1", "worker_1", "zone_A", 9_000)],
        )
        self.assertEqual(result.state, IdentityState.CONFIRMED)
        self.assertEqual(result.worker_uid, "worker_1")

    def test_missing_read_is_unknown_not_absent(self):
        result = bind_identity(self.track, [])
        self.assertEqual(result.state, IdentityState.UNKNOWN)
        self.assertIsNone(result.worker_uid)

    def test_different_zone_is_unknown(self):
        result = bind_identity(
            self.track,
            [CredentialObservation("cred_1", "worker_1", "zone_B", 10_000)],
        )
        self.assertEqual(result.state, IdentityState.UNKNOWN)

    def test_stale_read_is_unknown(self):
        result = bind_identity(
            self.track,
            [CredentialObservation("cred_1", "worker_1", "zone_A", 1_000)],
        )
        self.assertEqual(result.state, IdentityState.UNKNOWN)

    def test_multiple_workers_abstains_as_ambiguous(self):
        result = bind_identity(
            self.track,
            [
                CredentialObservation("cred_1", "worker_1", "zone_A", 9_500),
                CredentialObservation("cred_2", "worker_2", "zone_A", 9_700),
            ],
        )
        self.assertEqual(result.state, IdentityState.AMBIGUOUS)
        self.assertIsNone(result.worker_uid)

    def test_duplicate_reads_same_pair_still_confirm(self):
        result = bind_identity(
            self.track,
            [
                CredentialObservation("cred_1", "worker_1", "zone_A", 9_500),
                CredentialObservation("cred_1", "worker_1", "zone_A", 10_200),
            ],
        )
        self.assertEqual(result.state, IdentityState.CONFIRMED)

    def test_negative_window_rejected(self):
        with self.assertRaises(ValueError):
            bind_identity(self.track, [], time_window_ms=-1)


if __name__ == "__main__":
    unittest.main()
