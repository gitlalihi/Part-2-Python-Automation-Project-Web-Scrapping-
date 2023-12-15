from html.parser import HTMLParser

class ImageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.image_sources = []

    def handle_starttag(self, tag, attrs):
        for attr, value in attrs:
            if attr == "src" and tag == "img":
                self.image_sources.append(value)

with open(file="gallery.html", mode="r", encoding="utf-8") as html_file:
    content = html_file.read()

parser = ImageParser()
parser.feed(content)

image_sources_list = parser.image_sources
print("List of Image Sources:")
for source in image_sources_list:
    print(source)
