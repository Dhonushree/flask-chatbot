"""Test for NLP processing."""
from app.nlp_processor import process_query

def test_process_query():
    assert process_query("HW") == "homework"