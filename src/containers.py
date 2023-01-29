"""Containers module."""

from dependency_injector import containers, providers
from .api_services.api_scraper import ApiScraper
from .api_services.cache_service import CacheService
from .config_source import ConfigSource


class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(modules=[".endpoints"])

    config_source = providers.Singleton(
        ConfigSource
    )

    cache_service = providers.Singleton(
        CacheService
    )

    api_scraper = providers.Singleton(
        ApiScraper,
        config_source=config_source,
        cache_service=cache_service
    )
