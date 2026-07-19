import json
from pathlib import Path


def load_report():
    report_path = Path("/app/report.json")
    assert report_path.exists(), "report.json not found"

    with report_path.open() as f:
        return json.load(f)


def test_total_requests():
    """Success Criterion 2: Total request count is correct."""
    report = load_report()
    assert report["total_requests"] == 6


def test_unique_ips():
    """Success Criterion 3: Unique IP count is correct."""
    report = load_report()
    assert report["unique_ips"] == 3


def test_top_path():
    """Success Criterion 4: Most requested path is correct."""
    report = load_report()
    assert report["top_path"] == "/index.html"