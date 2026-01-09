import httpx


def fetch_html(url: str, timeout: float = 10.0) -> str:
    headers = {
        "User-Agent": "ProcessMinerBot/0.1"
    }

    with httpx.Client(follow_redirects=True, timeout=timeout) as client:
        response = client.get(url, headers=headers)
        response.raise_for_status()
        return response.text
