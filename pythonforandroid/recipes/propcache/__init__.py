from typing import Any

from pythonforandroid.archs import Arch
from pythonforandroid.recipe import PyProjectRecipe


class PropcacheRecipe(PyProjectRecipe):
    name = 'propcache'
    version = '0.2.1'
    url = 'https://files.pythonhosted.org/packages/source/p/propcache/propcache-{version}.tar.gz'
    depends = ['python3', 'setuptools']

    def get_recipe_env(self, arch: Arch, **kwargs) -> dict[str, Any]:
        env: dict[str, Any] = super().get_recipe_env(arch, **kwargs)
        env['PROPCACHE_NO_EXTENSIONS'] = '1'
        return env


recipe = PropcacheRecipe()
