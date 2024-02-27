from optparse import OptionParser

def parse_action_options(parser):
    """
    ## 操作选项
    * -a 或 --action 指定了操作目标，多级目标用点号分割，例如:
        * -a tasks.test.test
    """
    parser.add_option(
        "-a", "--action",
        dest="action",
        help="action",
        metavar="ACTION"
    )

def parse_profile_options(parser):
    parser.add_option(
        "--cluster",
        dest="cluster",
        help="cluster",
        metavar="CLUSTER"
    )

def parse_options():
    parser = OptionParser()
    parse_profile_options(parser)
    parse_action_options(parser)
    (options, args) = parser.parse_args() 
    return [options, args]

def show_help():
    '''
    命令行选项说明
    '''
    
    help = '\n'.join([
        show_help.__doc__,
        parse_action_options.__doc__,
    ])

    print(help)
