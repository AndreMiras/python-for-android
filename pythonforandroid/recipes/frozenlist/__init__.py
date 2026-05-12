from typing import Any

from pythonforandroid.archs import Arch
from pythonforandroid.recipe import PyProjectRecipe


class FrozenlistRecipe(PyProjectRecipe):
    name = 'frozenlist'
    version = '1.5.0'
    url = 'https://files.pythonhosted.org/packages/source/f/frozenlist/frozenlist-{version}.tar.gz'
    depends = ['python3', 'setuptools']

    def get_recipe_env(self, arch: Arch, **kwargs) -> dict[str, Any]:
        env: dict[str, Any] = super().get_recipe_env(arch, **kwargs)
        env['FROZENLIST_NO_EXTENSIONS'] = '1'
        return env


recipe = FrozenlistRecipe()
