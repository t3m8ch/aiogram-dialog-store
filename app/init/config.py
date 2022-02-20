from dataclasses import dataclass

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

    @classmethod
    def from_toml(cls, path: str = "config.app.toml") -> "AppConfig":
        toml_dict = _load_toml(path)
        return dataclass_factory.load(toml_dict, cls)


@dataclass(frozen=True, slots=True)
class UnitTestsConfig:
    db: DBConfig

    @classmethod
    def from_toml(cls, path: str = "config.tests.toml") -> "UnitTestsConfig":
        toml_dict = _load_toml(path)
        return dataclass_factory.load(toml_dict, cls)


def _load_toml(path: str) -> dict:
    with open(path, "rb") as f:
        return tomli.load(f)
