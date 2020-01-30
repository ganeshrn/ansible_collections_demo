#!/usr/bin/python
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.rainbow.test.plugins.module_utils.sharedstuff import sharedthing


def main():
	module = AnsibleModule(argument_spec={})
	result = {'changed': False, 'msg': sharedthing()}
	module.exit_json(**result)

if __name__ == '__main__':
	main()
