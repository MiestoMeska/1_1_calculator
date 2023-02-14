from setuptools import setup
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(name="rounded_calculate",
        version="0.3.1",
        description="Calculator package with history of calculations.",
        author="Vytautas Ruzgaila",
        packages=["rounded_calculate"],
        zip_safe=False,
        license="MIT",
        author_email="DoNotContactMe@Please.com",
        long_description=long_description,
        long_description_content_type='text/markdown')