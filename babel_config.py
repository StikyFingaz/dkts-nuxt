from pathlib import Path
from fastapi_babel import Babel
from fastapi_babel import BabelConfigs
# from main import app

# Commands to update message catalogues. Run from root directory in the terminal.
# pybabel init -i messages.pot -d translations -l bg
# python3 ./babel_config.py extract --dir .
# pybabel update -i messages.pot -d ./translations

LANGUAGES = ['en', 'bg']

translations_dir = Path(__file__).parent.resolve() / 'translations'
configs = BabelConfigs(
    ROOT_DIR=__file__,
    BABEL_DEFAULT_LOCALE="en",
    BABEL_TRANSLATION_DIRECTORY=str(translations_dir),
)

babel = Babel(configs=configs)

if __name__ == "__main__":
    babel.run_cli()
