from pathlib import Path

def test_css_exists():
    assert Path("styles.css").exists()

def test_video_exists():
    assert Path(
        "PixVerse_V6_Image_Text_360P_Create_self_intro_.mp4"
    ).exists()

def test_image_exists():
    assert Path("1000687159.png").exists()
