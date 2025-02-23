from pathlib import Path
from typing import Generator, Tuple
import git

VERSION_STR = "####VERSION####"

REPO_PATH = Path(__file__).parent.parent.parent
ROOT_DIR = REPO_PATH / "nzshm_site_database"
DOCS_DIR = ROOT_DIR / "docs"
DATA_DIR = ROOT_DIR / "data"
SITES_DIR = DATA_DIR / "sites"
SITES_DOC_FILEPATH = DOCS_DIR / "sites.md"
REPO_URL = "github.com/GNS-Science/nzshm-site-database"

def find_docs(docs_dir: Path) -> Generator[Path, None, None]:
    """Walk the documents directory to find all files with .md extension"""
    for child in docs_dir.iterdir():
        if child.is_dir():
            yield from find_docs(child)
        elif child.suffix == ".md":
            yield child

def get_version() -> Tuple[str, str]:
    """Find the version tag that matches the current commit. Raise exception if there is no tag for the commit."""
    repo = git.Repo(REPO_PATH)
    for tag in repo.tags:
        if repo.head.commit == tag.commit:
            return tag.name, tag.commit.hexsha
    raise Exception("no tags found at the current commit")

def update_docs_with_version(doc_filepath: Path, version_name: str):
    with doc_filepath.open() as doc_file:
        contents = doc_file.read()
        contents = contents.replace(VERSION_STR, version_name)
    with doc_filepath.open('w') as doc_file:
        doc_file.write(contents)
    
def get_sites(sites_dir: Path) -> Generator[Tuple[str, str], None, None]:
    """Find all directories under the sites_dir directory. These are assumed to be sites in the database.

    Returns:
        site: tuple of str, first is the site name (final dir name), second is the path to the
        directory relative to the REPO_PATH 
    """
    for child in sites_dir.iterdir():
        yield str(child.name), str(child.relative_to(REPO_PATH))

def site_text(site_name: str, site_path: str, version: str, repo_url: str) -> str:
    """Return markdown string for a site entry in the sites.md document file.

    Includes the name of the site and a link to the GitHub location using the path to the
    specified version tag (can be a tag or commit hash).
    """
    url = f"https://{repo_url}/tree/{version}/{site_path}"
    return f"## [{site_name}]({url})\n"



def update_sites_file(sites_doc_filepath: Path, sites_dir: Path, version: str):
    file_str = sites_doc_filepath.read_text()
    file_str = file_str[0:file_str.find("####")] + "\n"
    for site_name, site_path in get_sites(sites_dir):
        file_str += site_text(site_name, site_path, version, REPO_URL)
    sites_doc_filepath.write_text(file_str)


if __name__ == "__main__":
    version_name, version_sha = get_version()
    for file_path in find_docs(DOCS_DIR):
        update_docs_with_version(file_path, version_name)

    update_sites_file(SITES_DOC_FILEPATH, SITES_DIR, version_name)
