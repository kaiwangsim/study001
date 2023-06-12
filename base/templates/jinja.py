from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader = FileSystemLoader("templates"),
    autoescape = select_autoescape()
)

template = env.get_template("11.html")

context = {"thing": "this is adfasdf"}

print(template.render(**context))




