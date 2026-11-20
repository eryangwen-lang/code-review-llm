import importlib

import code_review_llm


def test_package_version():
    """Check that the package version is correctly defined."""
    assert code_review_llm.__version__ == "0.1.0"


def test_subpackages_import():
    """Check that all core subpackages can be imported."""
    modules = [
        "data",
        "models",
        "train",
        "evaluation",
        "preference",
        "sandbox",
        "serving",
    ]

    for module in modules:
        importlib.import_module(f"code_review_llm.{module}")
