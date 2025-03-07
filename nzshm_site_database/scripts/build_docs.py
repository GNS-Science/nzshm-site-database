from pathlib import Path
from typing import Generator, Tuple
import git

from jinja2 import Environment, FileSystemLoader

REPO_PATH = Path(__file__).parent.parent.parent
ROOT_DIR = REPO_PATH / "nzshm_site_database"
DOCS_DIR = ROOT_DIR / "docs"
TEMPLATE_DIR = ROOT_DIR / "templates"
DATA_DIR = ROOT_DIR / "data"
SITES_DIR = DATA_DIR / "sites"
REPO_URL = "github.com/GNS-Science/nzshm-site-database"


def find_templates(templates_dir: Path) -> Generator[Path, None, None]:
    """Walk the templates directory to find all files with .md extension"""
    for child in templates_dir.iterdir():
        if child.is_dir():
            yield from find_templates(child)
        elif child.suffix == ".md":
            yield child.name

def get_version() -> Tuple[str, str]:
    """Find the version tag that matches the current commit. Raise exception if there is no tag for the commit."""
    repo = git.Repo(REPO_PATH)
    for tag in repo.tags:
        if repo.head.commit == tag.commit:
            return tag.name, tag.commit.hexsha
    raise Exception("no tags found at the current commit")

def get_sites(sites_dir: Path) -> list[dict]:
    """Find all directories under the sites_dir directory. These are assumed to be sites in the database.

    Returns:
        site: tuple of str, first is the site name (final dir name), second is the path to the
        directory relative to the REPO_PATH 
    """
    sites = []
    for child in sites_dir.iterdir():
        sites.append(
            {"name": str(child.name), "path": str(child.relative_to(REPO_PATH))}
        )
    return sites

if __name__ == "__main__":
    version_name, version_sha = get_version()
    DOCS_DIR.mkdir(exist_ok=True)
    environment = Environment(loader=FileSystemLoader(TEMPLATE_DIR))

    args = dict(
        version=version_name,
        repo_url=REPO_URL,
    )
    sites = get_sites(SITES_DIR)
    args['sites'] = sites

    for template_name in find_templates(TEMPLATE_DIR):
        template = environment.get_template(template_name)
        content = template.render(args)
        rendered_filepath = DOCS_DIR / template_name
        rendered_filepath.write_text(content)