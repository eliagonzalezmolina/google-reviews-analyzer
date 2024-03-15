import os
from typing import Any, Dict

import yaml
from dotenv import load_dotenv

from google_reviews_analyzer.paths import params_file


def load_env_variables() -> Dict[str, Any]:
    load_dotenv()
    d = {key: os.getenv(key) for key in os.environ}
    return d


def load_params() -> Dict[str, Any]:
    with open(params_file, "r") as file:
        d = yaml.safe_load(file)
    return d


def load_config() -> Dict[str, Any]:
    d1 = load_env_variables()
    d2 = load_params()
    return {**d1, **d2}
