from jinja2 import Environment, FileSystemLoader
#This line uses the current directory
file_loader = FileSystemLoader('.')
# Load the enviroment
env = Environment(loader=file_loader)
template = env.get_template('bgp_variables.j2')
#Add the varibles
output = template.render(local_asn='1111', bgp_neighbor='192.168.1.1', remote_asn='2222')
#Print the output
print(output)
