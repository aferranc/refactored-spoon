"""
This module defines the command-line interface (CLI) commands for translation and localization.

It includes commands to initialize, update, and compile translations using Flask-Babel and Click.

Modules:
    os: Provides a way of using operating system dependent functionality.
    click: A package for creating command-line interfaces.
    Blueprint: Flask class for creating blueprints.
"""

import os

import click
from flask import Blueprint

bp = Blueprint("cli", __name__, cli_group=None)


@bp.cli.group()
def translate():
    """
    Translation and localization commands.

    This group contains commands for managing translations.
    """
    pass


@translate.command()
@click.argument("lang")
def init(lang):
    """
    Initialize a new language.

    Extracts messages and initializes a new language for translation.

    Args:
        lang (str): The language code to initialize.
    """
    if os.system("pybabel extract -F babel.cfg -k _l -o messages.pot ."):
        raise RuntimeError("extract command failed")
    if os.system("pybabel init -i messages.pot -d app/translations -l " + lang):
        raise RuntimeError("init command failed")
    os.remove("messages.pot")


@translate.command()
def update():
    """
    Update all languages.

    Extracts messages and updates all existing languages for translation.
    """
    if os.system("pybabel extract -F babel.cfg -k _l -o messages.pot ."):
        raise RuntimeError("extract command failed")
    if os.system("pybabel update -i messages.pot -d app/translations"):
        raise RuntimeError("update command failed")
    os.remove("messages.pot")


@translate.command()
def compile():
    """
    Compile all languages.

    Compiles all translations into binary format.
    """
    if os.system("pybabel compile -d app/translations"):
        raise RuntimeError("compile command failed")
