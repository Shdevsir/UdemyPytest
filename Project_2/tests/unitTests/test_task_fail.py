from tasks import Task


def test_task_equality():
    t1 = Task('sit there', 'james')
    t2 = Task('do something', 'smith')
    assert t1 == t2


def test_dict_equality():
    t1_dict = Task('make sandwitch', 'smith')._asdict()
    t2_dict = Task('make sandwithc', 'smit')._asdict()
    assert t1_dict == t2_dict
