from Basic import *

class Item(Basic):
	REQUIRED_ATTR = {"slot","trade","value","believed_value","price"}
	def __init__(self,data,required_attr=set()):
		"requires a dictionary of attributes and a set of required ones for this child"
		Basic.__init__(self,data,required_attr.union(Item.REQUIRED_ATTR))

if __name__ == "__main__":
	item_data = {
	"id":"1","name":"Sword","nickname":"pointy","desc":"metal death stick",
	"type":"Item","owner":"GM","inherit":None,"owneditems":None,
	"size":"tiny","weight":5,"health":100,"stamina":float("inf"),
	"attack":1,"anti-attack":1,"magic":0,"anti-magic":0,"acrobatics":0,"anti-acrobatics":0,
	"survival":0,"anti-survival":0,"perception":0,"anti-perception":0,"dipomacy":0,"anti-dipomacy":0,
	"knowledge":0,"anti-knowledge":0,"craft":0,"anti-craft":0,
	"slot":"hand","trade":False,"value":50,"believed_value":40,"price":10
	}
	assert Item(item_data).name=="Sword"
