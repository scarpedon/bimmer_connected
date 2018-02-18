"""Tests for ConnectedDriveVehicle."""
import unittest
from test import load_response_json

from bimmer_connected.vehicle import ConnectedDriveVehicle, DriveTrainType

G31_VEHICLE = load_response_json('vehicles.json')[0]


class TestVehicle(unittest.TestCase):
    """Tests for ConnectedDriveVehicle."""

    def test_has_rex(self):
        """Tests around hasRex attribute."""
        vehicle = ConnectedDriveVehicle(None, G31_VEHICLE)
        self.assertFalse(vehicle.has_rex)
        vehicle.attributes['hasRex'] = '1'
        self.assertTrue(vehicle.has_rex)

    def test_drive_train(self):
        """Tests around drive_train attribute."""
        vehicle = ConnectedDriveVehicle(None, G31_VEHICLE)
        self.assertEqual(DriveTrainType.CONVENTIONAL, vehicle.drive_train)
