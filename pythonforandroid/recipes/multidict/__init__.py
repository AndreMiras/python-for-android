from typing import Any

from pythonforandroid.archs import Arch
from pythonforandroid.recipe import PyProjectRecipe


class MultidictRecipe(PyProjectRecipe):
    name = 'multidict'
    version = '6.1.0'
    url = 'https://files.pythonhosted.org/packages/source/m/multidict/multidict-{version}.tar.gz'
    depends = ['python3', 'setuptools']

    def get_recipe_env(self, arch: Arch, **kwargs) -> dict[str, Any]:
        env: dict[str, Any] = super().get_recipe_env(arch, **kwargs)
        env['MULTIDICT_NO_EXTENSIONS'] = '1'
        return env


recipe = MultidictRecipe()
