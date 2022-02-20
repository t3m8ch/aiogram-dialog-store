from dataclasses import dataclass
from typing import Any

import dataclass_factory
import tomli

dataclass_factory = dataclass_factory.Factory()


@dataclass(frozen=True, slots=True)
class TgBotConfig:
    token: str


@dataclass(frozen=True, slots=True)
class DBConfig:
    url: str


@dataclass(frozen=True, slots=True)
class AppConfig:
    tgbot: TgBotConfig
    db: DBConfig


@dataclass(frozen=True, slots=True)
class UnitTestsConfig:
    db: DBConfig


@dataclass(frozen=True, slots=True)
class DBScriptsConfig:
    db: DBConfig


def load_config(type_=AppConfig, path: str = None):
    default_paths: dict[Any, str] = {
        UnitTestsConfig: "config.tests.toml",
    }
    if path is None:
        path = default_paths.get(type_) or "config.app.toml"

    toml_dict = _load_toml(path)
    return dataclass_factory.load(toml_dict, type_)


def _load_toml(path: str) -> dict:
    with open(path, "rb") as f:
        return tomli.load(f)
