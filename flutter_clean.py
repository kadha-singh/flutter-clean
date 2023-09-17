from os import chdir, system
from pathlib import Path


def main():
    print("\nproject cleaned => %d" % fluter_clean())


def fluter_clean() -> int:
    project_path = Path()

    project_cleaned = 0
    for item in project_path.iterdir():
        if item.is_dir() and is_project(item):
            item_path = item.absolute().__str__()
            chdir(item.name)
            try:
                if system("flutter clean") == 0:
                    print("cleaned -> %s" % item_path)
                    project_cleaned += 1
            except Exception as e:  # noqa: E722
                print(str(e))
            finally:
                chdir("..\\")
    return project_cleaned


def is_project(path: Path) -> bool:
    for item in path.iterdir():
        if item.is_file() and item.name.lower() == "pubspec.yaml":
            return True
    return False


if __name__ == "__main__":
    main()
