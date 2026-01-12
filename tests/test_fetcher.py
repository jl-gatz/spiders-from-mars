from unittest.mock import Mock, patch

import pytest
from httpcore import NetworkError

from process_miner.core.crawler.fetcher import fetch_html


def test_fetch_html_success():
    mock_response = Mock()
    mock_response.text = '<html><body>Hello</body></html>'
    mock_response.raise_for_status = Mock()

    with patch('httpx.Client') as mock_client_class:
        mock_client = Mock()
        mock_client.get.return_value = mock_response
        mock_client_class.return_value.__enter__.return_value = mock_client

        result = fetch_html('https://example.com')
        assert result == '<html><body>Hello</body></html>'
        mock_client.get.assert_called_once_with(
            'https://example.com',
            headers={'User-Agent': 'ProcessMinerBot/0.1'},
        )


def test_fetch_html_failure():
    with patch('httpx.Client') as mock_client_class:
        mock_client = Mock()
        mock_client.get.side_effect = Exception('Network error')
        mock_client_class.return_value.__enter__.return_value = mock_client

        try:
            fetch_html('https://example.com')
            pytest.fail('Should have raised exception')
        except Exception:
            pytest.raises(NetworkError, match='Network error')
