#Using unicodedata module to list smileys in HTML in a tabular format
import unicodedata


all_emoji = ["\U0001F600", "\U0001F601", "\U0001F602", "\U0001F603", "\U0001F601", "\U0001F60F"]

columns = ["#", "Emoji", "Name"]

table_head = f"<thead>\n<tr><th>{'</th><th>'.join(columns)}</th></tr>\n</thead>"
table_body = "\n<tbody>\n"

for i, emoji in enumerate(all_emoji, start=1):
    emoji_data = [f"{i}.", emoji, unicodedata.name(emoji).title()]
    table_body = table_body+ f"<tr><td>{'</td><td>'.join(map(str, emoji_data))}</td></tr>\n"

table_body += "</tbody>\n"
print(f"<table>\n{table_head}{table_body}</table>")
