import yaml

def load_config_by_url(url = None):
    """ Loads a configuration file for the given url
    """
    #TODO: Merge default configuration.

    if url is None:
        conf = 'default'
    elif 'bugs.gentoo.org' in url:
        conf = 'gentoo'
    elif 'landfill.bugzilla.org/bugzilla-2.22-branch' in url:
        conf = 'landfill-2.22'
    else:
        conf = 'default'

    return yaml.load(file('bugzdefs/%s.yml'%conf, 'r'))
