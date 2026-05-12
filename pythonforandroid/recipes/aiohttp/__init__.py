from typing import Any

from pythonforandroid.archs import Arch
from pythonforandroid.recipe import PyProjectRecipe


class AIOHTTPRecipe(PyProjectRecipe):
    name = 'aiohttp'
    version = '3.13.5'
    url = 'https://files.pythonhosted.org/packages/source/a/aiohttp/aiohttp-{version}.tar.gz'
    depends = ['python3', 'setuptools', 'multidict', 'yarl', 'frozenlist', 'propcache']
    python_depends = ['aiohappyeyeballs', 'aiosignal']

    def get_recipe_env(self, arch: Arch, **kwargs) -> dict[str, Any]:
        env: dict[str, Any] = super().get_recipe_env(arch, **kwargs)
        env['AIOHTTP_NO_EXTENSIONS'] = '1'
        return env


recipe = AIOHTTPRecipe()
