def tasks(config,options, actions):
    import tasks as tasks
    tasks.dispatch(config,options, actions)

def run(options):
    from gevent import monkey
    from options import show_help
    from config.config import load_config
    # 操作入口
    if options.action is not None:
        actions = options.action.split(".")
        if len(actions) == 0:
            return
        
        root_action = actions[0]
        monkey.patch_all(ssl=False, thread=False, socket=False)
        config = load_config(options, args)
        print("@init config...")

        print("@dispatch action:{}...".format(options.action))
        dispatch = {
            "tasks":lambda: tasks(config,options, actions)
        }
        dispatch[root_action]()
    else:
        show_help()

if __name__ == "__main__":
    from options import parse_options
    [options, args] = parse_options()
    run(options)