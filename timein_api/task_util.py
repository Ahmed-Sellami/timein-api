from timein_api.models import Task, Comment, Period


class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

    def __str__(self):
        return "{} with {} children".format(self.data, len(self.children))


def get_all_tasks(id_project, parent_task) -> Node:
    subtasks = Task.objects.filter(project=id_project, parent_task=parent_task)
    node = Node(parent_task)
    for s in subtasks:
        node.add_child(get_all_tasks(id_project, s))
    return node


def get_comments(task):
    result = []
    for c in Comment.objects.filter(task=task.id):
        result.append({'period': c.period, 'content': c.content})
    return result


def get_periods(task):
    result = []
    for p in Period.objects.filter(task=task.id):
        result.append({'start_time': str(p.start_time), 'end_time': str(p.end_time)})
    return result

def get_all_tasks_dict(node):
    t_dict = get_task_dict(node.data)
    t_dict['comments'] = get_comments(node.data)
    t_dict['periods'] = get_periods(node.data)
    for c in node.children:
        t_dict['subtasks'].append(get_all_tasks_dict(c))
    return t_dict


def get_task_dict(task):
    return {'title': task.title,
            'desc': task.desc,
            'time_spent': task.time_spent,
            'is_done': task.is_done,
            'category': task.category.id if task.category else task.category,
            'lock_task': task.lock_task,
            'subtasks': [],
            'comments': [],
            'periods': []}
