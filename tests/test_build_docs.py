from nzshm_site_database.scripts.build_docs import update_docs_with_version

DOC_STRING = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. In vel vestibulum arcu. Integer pulvinar enim
pharetra ante vehicula, vel hendrerit massa convallis. Praesent vitae dolor a nulla pellentesque semper. Maecenas
lacinia fringilla dui ac accumsan. Ut tristique justo tempor ultrices feugiat. Donec et leo at nisi laoreet aliquet
vel lacinia metus. Sed posuere quis mauris ut malesuada. 

Donec eu sapien sit amet ipsum cursus gravida sed a dui. Ut ac arcu id lectus varius facilisis. Ut congue laoreet dui
nec semper. Sed ####VERSION#### accumsan blandit mauris sed ultrices. Fusce commodo efficitur nisi, a gravida augue tristique gravida.
Pellentesque vestibulum, leo in dictum convallis, lectus sapien interdum ligula, id posuere felis dolor vitae metus. 
"""

VERSION_STR = "####VERSION####"

def test_update_version(tmp_path):
    doc_filepath = tmp_path / "doc.md"
    doc_filepath.write_text(DOC_STRING)

    version_name = "v1.0.0"
    update_docs_with_version(doc_filepath, version_name)
    out_text = doc_filepath.read_text()

    assert VERSION_STR not in out_text
    assert version_name in out_text


    

    
