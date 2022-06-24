from intro.test_one import Dinner
import time


def test_asdict():
    t_Dinner = Dinner('potatoes', 'Peter', True, 34)
    t_dict = t_Dinner._asdict()
    excepted = {'food': 'potatoes',
                'cook': 'Peter',
                'ready': True,
                'id': 34}
    assert t_dict == excepted


# @pytest.mark.run_first
def test_replace():
    time.sleep(1)
    t_before = Dinner('meat', 'Sam', False)
    t_after = t_before._replace(id=10, ready=True)
    t_expected = Dinner('meat', 'Sam', True, 10)
    assert t_after == t_expected
