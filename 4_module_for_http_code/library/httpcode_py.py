#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.module_utils.basic import (
    AnsibleModule
)
import requests

def example_function(str1):
    failed = False
    # Формируем конечную строку
    try:
        result = requests.get(str1)
    except requests.exceptions.RequestException:
        raise SystemExit("Wrong address!")
        # failed = True
        # msg = "Wrong address!"
    else:
        result = result.status_code
        if result == 200:
            msg = "Success"
        else:
            msg = "Got HTTP error responce"
    return(failed, result, msg)


def main():
    # Задаем аргументы модуля
    module_args = dict(
        address=dict(required=True, type='str')
    )
    # Создаем объект - модуль
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )
    # Получаем из модуля аргументы
    address = module.params["address"]
    # Вызываем нашу функцию
    lc_return = example_function(address)
    # Если задача зафейлилась
    if lc_return[0]:
        module.fail_json(changed=True,
                         failed=lc_return[0],
                         http_response=lc_return[1],
                         msg=lc_return[3])
    # Если задача успешно завершилась
    else:
        module.exit_json(changed=True,
                         failed=lc_return[0],
                         http_response=lc_return[1],
                         msg=lc_return[2])


if __name__ == "__main__":
    main()
