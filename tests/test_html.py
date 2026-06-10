from pathlib import Path

def test_index_exists():
    assert Path("index.html").exists()

def test_title_exists():
    content = Path("index.html").read_text(encoding="utf-8")

    assert "<title>" in content
    assert "</title>" in content
