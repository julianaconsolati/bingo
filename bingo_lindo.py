from jinja2 import Template
from src.bingo import carton_valido

template = Template(open("template.j2").read())

file = open("bingo.html", "w")
file.write(template.render(carton = carton_valido()))
file.close()
print("Creado archivo bingo.html")
