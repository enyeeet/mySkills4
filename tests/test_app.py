import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from dashapp import app

def test_header_present(dash_duo):
    dash_duo.start_server(app=app)

    header = dash_duo.find_element("h1")
    assert header is not None
    assert "Soul Foods Sales Visualiser" in header.text

def test_graph_present(dash_duo):
    dash_duo.start_server(app=app)

    graph = dash_duo.find_element("#sales-line-chart")
    assert graph is not None

def test_radio_present(dash_duo):
    dash_duo.start_server(app=app)

    radio = dash_duo.find_element("#region-filter")
    assert radio is not None