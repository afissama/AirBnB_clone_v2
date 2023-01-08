#!usr/bin/python3
"""Unittest for console.py"""
from io import StringIO
import os
import unittest
from unittest.mock import patch

from console import HBNBCommand


class TestHBNBConsole(unittest.TestCase):
    """Unit test for testing the command line interpreter"""

    @classmethod
    def setUpClass(cls):
        """ Testing setup """
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        cls.HBNBCONSOLE = HBNBCommand()

    @classmethod
    def tearDownClass(cls):
        """HBNB After tests"""
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        del cls.HBNBCONSOLE

    def tearDown(self):
        """Delete any created file.json."""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_create(self):
        """Test create command."""
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNBCONSOLE.onecmd("create BaseModel")
            bm = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNBCONSOLE.onecmd("create User")
            us = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNBCONSOLE.onecmd("create State")
            st = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNBCONSOLE.onecmd("create Place")
            pl = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNBCONSOLE.onecmd("create City")
            ct = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNBCONSOLE.onecmd("create Review")
            rv = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNBCONSOLE.onecmd("create Amenity")
            am = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNBCONSOLE.onecmd("all BaseModel")
            self.assertIn(bm, f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNBCONSOLE.onecmd("all User")
            self.assertIn(us, f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNBCONSOLE.onecmd("all State")
            self.assertIn(st, f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNBCONSOLE.onecmd("all Place")
            self.assertIn(pl, f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNBCONSOLE.onecmd("all City")
            self.assertIn(ct, f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNBCONSOLE.onecmd("all Review")
            self.assertIn(rv, f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNBCONSOLE.onecmd("all Amenity")
            self.assertIn(am, f.getvalue())


    def test_create_with_params(self):
        """Test Console Improvement features"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNBCONSOLE.onecmd("create State name=\"COTONOU\"")
            st = f.getvalue().strip()
            self.assertIsNotNone(st)
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNBCONSOLE.onecmd("all State")
            self.assertIn(st, f.getvalue())
