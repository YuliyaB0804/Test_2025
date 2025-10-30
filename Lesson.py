import pytest

class TestMainPage():
    @pytest.mark.xfail
    @pytest.mark.smoke
    def test_1(self):
        assert True

    @pytest.mark.regression
    def test_2(self):
        assert True

class TestBasket():
    @pytest.mark.skip(reason="not implemented yet")
    @pytest.mark.smoke
    def test_3(self):
        assert True

    @pytest.mark.smoke
    def test_4(self):
        assert True

@pytest.mark.skip
class TestBookPage():
    @pytest.mark.smoke
    def test_5(self):
        assert True

    @pytest.mark.regression
    def test_6(self):
        assert True

@pytest.mark.beta_users
@pytest.mark.smoke
def test_7():
    assert True
# :thumbsup:
# Нажмите, чтобы отреагировать
# :grinning:
# Нажмите, чтобы отреагировать
# :rofl:
# Нажмите, чтобы отреагировать
# Добавить реакцию
# Ответить
# НОВОЕ
# Переслать
# Ещё
#
# Найдите тестовые методы, которые будут найдены и выполнены PyTest при запуске следующей команды:
# pytest -v -m "smoke and not beta_users" test_task_run_1.py
