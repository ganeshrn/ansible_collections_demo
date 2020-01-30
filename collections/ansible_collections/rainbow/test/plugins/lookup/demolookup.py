from ansible.plugins.lookup import LookupBase
from ansible_collections.rainbow.test.plugins.module_utils.sharedstuff import sharedthing

class LookupModule(LookupBase):
	def run(self, terms, variables, **kwargs):
		return [sharedthing()]
