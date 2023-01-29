"""Endpoints module."""
from fastapi import APIRouter, Depends, HTTPException
from dependency_injector.wiring import inject, Provide
from .api_services.api_scraper import ApiScraper

import ipaddress
from .containers import Container

router = APIRouter()


@router.get("/{ip_address}")
@inject
async def get_ip_data(
        ip_address: str,
        api_scraper: ApiScraper = Depends(Provide[Container.api_scraper]),
):
    if is_valid_ipv4(ip_address):
        return await api_scraper.get_data(ip_address)
    else:
        raise HTTPException(status_code=500, detail="Invalid Input")


def is_valid_ipv4(address):
    try:
        ipaddress.IPv4Address(address)
        return True
    except ValueError:
        return False


