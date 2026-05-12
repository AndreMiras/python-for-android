from typing import Any

from pythonforandroid.archs import Arch
from pythonforandroid.recipe import PyProjectRecipe


class YarlRecipe(PyProjectRecipe):
    name = 'yarl'
    version = '1.18.3'
    url = 'https://files.pythonhosted.org/packages/source/y/yarl/yarl-{version}.tar.gz'
    depends = ['python3', 'setuptools', 'multidict', 'propcache']
    python_depends = ['idna']

    def get_recipe_env(self, arch: Arch, **kwargs) -> dict[str, Any]:
        env: dict[str, Any] = super().get_recipe_env(arch, **kwargs)
        env['YARL_NO_EXTENSIONS'] = '1'
        return env


recipe = YarlRecipe()
