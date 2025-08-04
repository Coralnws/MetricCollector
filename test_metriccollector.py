# test_metriccollector.py
"""
Tests for MetricCollector module.
"""

import unittest
from metriccollector import MetricCollector

class TestMetricCollector(unittest.TestCase):
    """Test cases for MetricCollector class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MetricCollector()
        self.assertIsInstance(instance, MetricCollector)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MetricCollector()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
