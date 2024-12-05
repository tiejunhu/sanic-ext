from importlib.metadata import version

from sanic_ext.bootstrap import Extend
from sanic_ext.config import Config
from sanic_ext.extensions.base import Extension
from sanic_ext.extensions.http.cors import cors
from sanic_ext.extensions.openapi import openapi
from sanic_ext.extensions.templating.render import render
from sanic_ext.extras.request import CountedRequest
from sanic_ext.extras.serializer.decorator import serializer
from sanic_ext.extras.validation.decorator import validate


__version__ = version("sanic-ext-fork")

__all__ = [
    "Config",
    "CountedRequest",
    "Extend",
    "Extension",
    "cors",
    "openapi",
    "render",
    "serializer",
    "validate",
]
