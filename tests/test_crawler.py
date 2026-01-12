from http import HTTPStatus
from unittest.mock import patch

from fastapi.testclient import TestClient

from process_miner.api.main import app
from process_miner.models.core.core_models import CrawlResult, Page


def test_crawl_endpoint():
    # Mock the crawl_site function
    mock_result = CrawlResult(
        start_url='https://example.com',  # type: ignore
        pages=[
            Page(
                url='https://example.com',  # type: ignore
                title='Example Title',
                text='This is some example text that is longer than '
                '500 characters to test the excerpt functionality. ' * 10,
                headings=['Heading 1', 'Heading 2'],
                links=[],
            ),
            Page(
                url='https://example.com/page2',  # type: ignore
                title='Page 2',
                text='Short text',
                headings=[],
                links=[],
            ),
        ],
    )

    with patch(
        'process_miner.api.routers.crawler.crawl_site',
        return_value=mock_result,
    ):
        client = TestClient(app)
        payload = {'start_url': 'https://example.com', 'max_pages': 10}
        response = client.post('/crawl/', json=payload)
        assert response.status_code == HTTPStatus.OK
        data = response.json()
        assert 'pages' in data
        assert len(data['pages']) == 2  # noqa: PLR2004
        assert data['pages'][0]['url'] == 'https://example.com/'
        assert data['pages'][0]['title'] == 'Example Title'
        assert data['pages'][0]['text_excerpt'].startswith(
            'This is some example text'
        )
        assert len(data['pages'][0]['text_excerpt']) <= 500  # noqa: PLR2004
        assert data['pages'][0]['headings'] == ['Heading 1', 'Heading 2']
