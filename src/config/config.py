def load_config(options, args):
    profile_path = "config/config/local/dev.json"
    config = None
    if options.cluster:
        pass
    else:
        import os
        import json
        if os.path.exists(profile_path):
            with open(profile_path, "r") as f:
                config = json.loads(f.read())
        else:
            config = {}
    return config


def load_local_config():
    import os
    import json
    profile_path = "config/config/local/dev.json"
    if os.path.exists(profile_path):
        with open(profile_path, "r") as f:
            config = json.loads(f.read())
    else:
        config = {}
    return config