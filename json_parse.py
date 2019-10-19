import json

    

def read_json(json_input):
    keys=list(json_input.keys())
    for i in keys:
        new_i=i.capitalize()
        json_input[new_i]=json_input.pop(i)
        #print(i)
        #print(type(json_input[i]))
        i=new_i
        if type(json_input[i])==type(dict()):
            read_json(json_input[i])
        elif type(json_input[i]) == type(list()):
            for items in json_input[i]:
                if type(items)==type(dict()):read_json(items)
                elif type(items) == type(list()):read_json(items)
                else: pass    


x="""{
	"test-123": {
		"abc xyz": "123",
		"my_array" : [
			{
				"nested key": "myvalue"
			}
		]
	},
	"anotherArray": [
		{
			"random": true
		}
	]
}"""
x=json.loads(x)
read_json(x)
print(x)
