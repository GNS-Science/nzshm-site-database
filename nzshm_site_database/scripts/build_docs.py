from pathlib import Path
from typing import Generator, Tuple
import git

# update version
docs_dir = Path("nzshm_site_database/docs")
VERSION_STR = "####VERSION####"
repo_path = Path(__file__).parent.parent.parent

def find_docs(docs_dir: Path) -> Generator[Path, None, None]:
    for child in docs_dir.iterdir():
        if child.is_dir():
            yield from find_docs(child)
        elif child.suffix == ".md":
            yield child

def get_version() -> Tuple[str, str]:
    repo = git.Repo(repo_path)
    head = repo.head.commit
    for tag in repo.tags:
        if repo.head.commit == tag.commit:
            return tag.name, tag.commit.hexsha

def update_docs_with_version(doc_filepath: Path, version_name: str):
    with doc_filepath.open() as doc_file:
        contents = doc_file.read()
        contents = contents.replace(VERSION_STR, version_name)
    with doc_filepath.open('w') as doc_file:
        doc_file.write(contents)


if __name__ == "__main__":
    version_name, version_sha = get_version()
    for file_path in find_docs(docs_dir):
        update_docs_with_version(file_path, version_name)