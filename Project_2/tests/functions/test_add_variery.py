from _pytest.cacheprovider import NFPlugin
from _pytest.capture import TeeCaptureIO
import pytest
import tasks
from tasks import Task


def test_add1():
    task = Task('run', 'JAMES', True)
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)


def equivalent(t1, t2):
    return ((t1.summary == t2.summary) and
            (t1.owner == t2.owner) and
            (t1.done == t2.donw))


@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    tasks.start_tasks_db(str(tmpdir), 'tiny')
    yield
    tasks.stop_tasks_db()


@pytest.mark.parametrize('task',
                         [Task('left', done=True),
                          Task('swim', 'james'),
                          Task('run', 'JAMES', True),
                          Task('play', 'JaMeS', False)])
def test_add_2(task):
    task_id = tasks.add(tasks)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)


@pytest.mark.parametrize('summary', 'owner', 'done',
                         [('left', None, False),
                          ('swim', 'james', False),
                          ('exercise', 'JaMeS', False)])
def test_add_3(summary, owner, done):
    task = Task(summary, owner, done)
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)
