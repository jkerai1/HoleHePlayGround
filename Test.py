import subprocess

process = subprocess.check_output(['holehe', '--only-used','test@gmail.com'])
print(type(process))

my_json = process.decode('utf8').replace("'", '"')
print(my_json)#
print('- ' * 20)

# Load the JSON to a Python list & dump it back out as formatted JSON
data = json.loads(my_json)
s = json.dumps(data, indent=4, sort_keys=True)
print(s)
