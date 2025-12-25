from visualizer import app
from dash import html, dcc

def test_header_exists():
    layout = app.layout

    # Ensure layout is a Div
    assert isinstance(layout, html.Div)

    # Extract children
    children = layout.children

    # Normalize to list
    if not isinstance(children, list):
        children = [children]

    # Check if any H1 exists with expected text
    header_exists = any(
        isinstance(child, html.H1) and child.children == "Soul Foods Visualiser"
        for child in children
    )

    assert header_exists, "Header 'Pink Morsel Performance' not found in layout"

# test_header_exists()



def test_visualisation_present():
    layout = app.layout

    #Ensure it is the object of the html.Div class
    assert isinstance(layout, html.Div)

    children = layout.children

    if not isinstance(children, list):
        children = [children]

    visualiser_exists = any(
        isinstance(child, dcc.Graph) and child.id == "pink_morsel_graph" for child in children
    )

    assert visualiser_exists, "Sorry! Visualiser doesn't exist."



def test_region_picker():
    layout = app.layout

    assert isinstance(layout, html.Div)

    children = layout.children
    if not isinstance(children, list):
        children = [children]

    region_picker_exist = any(
        isinstance(child, html.Div) and isinstance(child.children, dcc.RadioItems) and child.children.id == "my-input" for child in children
    )
    assert region_picker_exist, "No region picker exist in this page"