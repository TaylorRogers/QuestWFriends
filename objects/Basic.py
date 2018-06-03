class Basic:
	"""
	Class Basic defines the basic attributes for all in game objects
	"""
	REQUIRED_ATTR = {
		"id","name","nickname","desc",
		"type","owner","inherit","owneditems",
		"size","weight","health","stamina",
		"attack","anti-attack","magic","anti-magic","acrobatics","anti-acrobatics",
		"survival","anti-survival","perception","anti-perception","dipomacy","anti-dipomacy",
		"knowledge","anti-knowledge","craft","anti-craft"
	}

	def __init__(self,dict,required_attr=set()):
		"""
		init takes a dictionary and creates self attributes out of each key value pair.
		init also checks that a set of basic requirements are in the dictionary's keys.
		"""
		required_attr = required_attr.union(Basic.REQUIRED_ATTR) 
		"Basic instead of self as it refers to this classess REQUIRED_ATTR"
		self.check_required_attr(set(dict.keys()),required_attr)

		for key in dict:
			setattr(self, key, dict[key])

	def check_required_attr(self,set_dict_keys,required_attr):
                if not required_attr.issubset(set_dict_keys):
                        complement = required_attr - set_dict_keys
                        raise ValueError("""
	Class {} failed to recieve all need attributes.
	Needed dictionary Attributes:{}""".format(self.__class__.__name__,repr(complement)))

