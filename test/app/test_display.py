import sys
sys.path.append('D:/python/python101')
from src.app.app import display



def test_display_output(capsys):
    display()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Welcome to Python101"
