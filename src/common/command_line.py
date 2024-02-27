from inspect import getmembers, signature, isfunction, getfullargspec
import importlib

def dispatch(config, options, actions, targets):
    """ 分发命令行 action """
    action_len = len(actions)
    print(action_len)

    if action_len < 2:
        if targets.get('run') is not None:
            print("[命令路由执行]:", '->'.join(actions))
            targets['run']()
        else:
            print('action not found')
        return

    index = 1
    next = targets
    action = actions[index]
    print(f"[命令路由中..]: {actions[0]}")

    while action_len >= index:
        if type(next) == type({}):
            if index == action_len:
                if next.get('run') is not None:
                    print("[命令路由执行]:", '->'.join(actions))
                    next['run']()
                    break
                else:
                    print('not found')

            action = actions[index]
            if next.get(action) is not None:
                print(f"[命令路由中..]: {action}")
                next = next[action]
                index += 1
            else:
                print("[命令路由错误]: 未找到支持的命令行路由：", '->'.join(actions), ", obj:", next)
                index += 1
        else:
            print("[命令路由执行]:", '->'.join(actions))

            print(next)
            next()
            index += 1
            break


def dispatch_runner(config, options, actions, targets):
    """ 分发命令行 action """
    action_len = len(actions)
    action_len = len(actions)
    if action_len < 2:
        return

    def load_and_run(target):
        modules = target.split('.')
        class_pos = len(modules)-2
        path_pos = len(modules)-1

        if class_pos >= 0 and modules[class_pos][0].isupper():
            constructor = modules[class_pos]
            runner = modules[path_pos]
            module_path = '.'.join(modules[:class_pos])
            importlib.import_module(module_path).__getattribute__(
                constructor)(config, options).__getattribute__(runner)()
        else:
            runner = modules[path_pos]

            module_path = '.'.join(modules[:path_pos])
            importlib.import_module(module_path).__getattribute__(
                runner)(config, options)

    index = 1
    next = targets
    while action_len >= index:
        if type(next) == type({}):
            if index == action_len:
                if next.get('run') is not None:
                    load_and_run(next['run'])
                    break

            action = actions[index]
            if next.get(action) is not None:
                next = next[action]
                index += 1
        else:
            load_and_run(next)
            index += 1
            break


def mount_test_module(config, options, module):
    test_group = {}
    for test_func_name, test_func in getmembers(module):
        if isfunction(test_func):
            if test_func_name.startswith('test_'):
                info = signature(test_func)
                info_args = list(info.parameters.keys())
                if len(info_args) == 2 and info_args[0] == 'config' and info_args[1] == 'options':
                    def get(test_func):
                        return lambda: test_func(config, options)
                    test_group[test_func_name] = get(test_func)
    return test_group


def mount_test_modulelist(config, options, modulelist):
    print('zzz')
    test_group = {}
    for module in modulelist:
        for test_func_name, test_func in getmembers(module):
            if isfunction(test_func):
                if test_func_name.startswith('test_'):
                    info = getfullargspec(test_func)
                    if len(info.args) == 2 and info.args[0] == 'config' and info.args[1] == 'options':
                        def get(test_func):
                            return lambda: test_func(config, options)
                        if test_group.get(test_func_name) is not None:
                            print(f'测试函数名重复：{test_func_name}')
                        assert test_group.get(test_func_name) is None
                        print(test_func_name)
                        test_group[test_func_name] = get(test_func)
    print('xx')
    return test_group


def mount_func(config, options, func):
    return lambda: func(config, options)


def mount_class(config, options, mountable_class):
    # 创建一个lambda函数，调用 instance()
    # 会触发  mountable_class 的 __call__ 方法被调用
    return lambda: mountable_class(config, options)()
