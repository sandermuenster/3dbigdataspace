import xml.etree.ElementTree as ET

from heritage3d.sources.europeana import map_item
from heritage3d.sources.oai_pmh import map_record


def test_europeana_mapping_collapses_lists():
    item = {
        "id": "/123/abc",
        "title": ["A building"],
        "edmIsShownBy": ["http://img/1.jpg"],
        "rights": ["http://rights/cc0"],
        "edmConceptPrefLabelLangAware": {"en": ["Architecture"]},
    }
    row = map_item(item)
    assert row["uid"] == "123/abc"
    assert row["source"] == "Europeana"
    assert row["uri"] == "http://img/1.jpg"
    assert row["name"] == "A building"
    assert row["edmConceptPrefLabelLangAware"] == "Architecture"


def test_oai_mapping_reads_dublin_core():
    xml = """
    <record xmlns="http://www.openarchives.org/OAI/2.0/">
      <header><identifier>oai:test:1</identifier></header>
      <metadata>
        <dc xmlns:dc="http://purl.org/dc/elements/1.1/">
          <dc:title>Sample</dc:title>
          <dc:description>A description</dc:description>
        </dc>
      </metadata>
    </record>
    """
    rec = ET.fromstring(xml)
    row = map_record(rec, source="test")
    assert row["uid"] == "oai:test:1"
    assert row["name"] == "Sample"
    assert row["description"] == "A description"
