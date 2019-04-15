from jinja2 import Environment, FileSystemLoader

#This line uses the current directory
file_loader = FileSystemLoader('.')

env = Environment(loader=file_loader)
template = env.get_template('hello_world.j2')
output = template.render()
#Print the output
print(output)
