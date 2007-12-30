import yaml

def load_config_by_url(url = None):
    #TODO: Choose file.
    default = yaml.load(file('bugzdefs/landfill-2.22.yml', 'r'))
    #new     = yaml.load(file('gentoo.yml',  'r'))
    #for key in new.keys():
    #    if key in default:
    #        default[key].update(new[key])
    #    else:
    #        default[key] = new[key]
    return default
