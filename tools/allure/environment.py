import platform
import sys

from config import settings


def create_allure_env_file():
    """
    Создает файл `environment.properties` в директории результатов Allure.

    Файл содержит информацию об окружении, необходимую для тестирования. Значения берутся
    из метода `get_env_properties()` объекта `settings`. Каждая строка файла соответствует
    паре "ключ=значение".
    """
    plfm = ("os_info", f"{platform.system()}, {platform.release()}")
    python_v = ("python_version", sys.version)
    env_items = list(settings.get_env_properties().items())
    env_items.extend((plfm, python_v))
    env_list = [f"{key}={value}" for key, value in env_items]
    with open(
        settings.ALLURE_RESULTS_PATH.joinpath("environment.properties"), "w+"
    ) as f:
        f.write("\n".join(env_list))
