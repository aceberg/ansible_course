#!/usr/bin/python
import re

from ansible.errors import (
    AnsibleFilterTypeError
)

def string_to_mac(macstring):
    '''
        Convert string to mac address
    '''
    if not isinstance(macstring, str):
        raise AnsibleFilterTypeError("String type is expected, "
                                     "got type %s instead" % type(macstring))
    
    if not re.match(r"^[0-9A-Fa-f]{12}$", macstring):
        raise AnsibleFilterTypeError("Wrong length or characters")

    return re.sub(r'(\w\w)', r'\1:', macstring, 5)


class FilterModule(object):
    def filters(self):
        return {
            'string_to_mac': string_to_mac
        }
