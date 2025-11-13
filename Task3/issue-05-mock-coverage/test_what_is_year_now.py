import unittest
import json
from unittest.mock import patch, MagicMock
from io import BytesIO

from what_is_year_now import what_is_year_now


class TestWhatIsYearNow(unittest.TestCase):

    @patch('urllib.request.urlopen')
    def test_ymd_format(self, mock_urlopen):
        """Тест для формата YYYY-MM-DD."""
        mock_response_data = json.dumps({
            "currentDateTime": "2024-03-01T12:00Z"
        }).encode('utf-8')
        mock_resp = MagicMock()
        mock_resp.read.return_value = mock_response_data
        mock_resp.__enter__.return_value = mock_resp

        mock_urlopen.return_value = mock_resp

        self.assertEqual(what_is_year_now(), 2024)

    @patch('urllib.request.urlopen')
    def test_dmy_format(self, mock_urlopen):
        """Тест для формата DD.MM.YYYY."""
        mock_file = BytesIO(json.dumps({
            "currentDateTime": "01.03.2025"
        }).encode('utf-8'))
        mock_urlopen.return_value.__enter__.return_value = mock_file

        self.assertEqual(what_is_year_now(), 2025)

    @patch('urllib.request.urlopen')
    def test_invalid_format(self, mock_urlopen):
        """Тест для неверного формата даты."""
        mock_file = BytesIO(json.dumps({
            "currentDateTime": "01/03/2025"
        }).encode('utf-8'))
        mock_urlopen.return_value.__enter__.return_value = mock_file

        with self.assertRaises(ValueError):
            what_is_year_now()
