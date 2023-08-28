from jinja2 import Environment, FileSystemLoader
import os
import pathlib
import shutil
from pathlib import Path
import markdown
from datetime import datetime
import re


# Filepath
source = 'pages'
dest = 'web'

# Check and create web directory
if pathlib.Path(dest).exists():
    print("exist")
    shutil.rmtree(dest)
else:
    print("NOT exist")
    os.mkdir(dest)

if not pathlib.Path(dest).exists():
    os.mkdir(dest)

environment = Environment(loader=FileSystemLoader("./templates/"))
home_template = environment.get_template("home.html")
article_template = environment.get_template('article.html')


# Generate timestamp
now = datetime.now()
stamp = now.strftime("%Y-%m-%d %H:%M")

### HTML Header
###header = ""

### back = "<a href=\"index.html\">back</a>"

### footer = "\n<body>\n</html>"

# Web directory remove and creation



# Generate html files from markdown files
mdowns = Path(source).glob('*')
for file in mdowns:
    with open(file, 'r') as f:
        text = f.read()
        html = markdown.markdown(text)
        print("read", file)

        newfile = os.path.split(file)[1]
        newfile = os.path.splitext(newfile)[0]
        newfile = newfile + ".html"
        newfile = os.path.join(dest, newfile)
        with open(newfile, 'w') as f:
            print("write", newfile)

            f.close()






# for file in mdowns:
#     with open(file, 'r') as f:
#         text = f.read()
#         html = markdown.markdown(text)
#         print("read", file)
#
#         newfile = os.path.split(file)[1]
#         newfile = os.path.splitext(newfile)[0]
#         newfile = newfile + ".html"
#         newfile = os.path.join(dest, newfile)
#         with open(newfile, 'w') as f:
#             print("write", newfile)
#             f.write(header)
#             f.write(back)
#             f.write(html)
#             f.write(footer)
#             f.close()







# Generate File-index / Homepage
home = os.path.join(dest, "index.html")
path = sorted(os.listdir(dest))

homepage = ""

with open(home, 'w') as f:
    f.write(header)
    f.write(homepage)
    for page in path:
        newpage = os.path.splitext(page)[0]
        newpage = newpage.replace("-", " ")
        print("title:", newpage)
        f.write("<a href=\"{0}\">{1}</a><br>".format(page, newpage))
    f.write("<br><br><div id=\"stamp\">Last generated: {}</div>".format(stamp))
    f.write(footer)

    for page in sorted(Path(source).glob('*')):
        with open(page, "r") as file:
            patrn = "category"
            for line in file:
                if re.findall(patrn, line):
                    cat = line.split()[2]
                    print("Category:", cat)
                    #f.write("<b>{0}</b><br>".format(cat))