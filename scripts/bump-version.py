import re, time, pathlib
p = pathlib.Path(__file__).resolve().parent.parent / "index.html"
v = time.strftime("%Y%m%d%H%M")
s = p.read_text(encoding="utf-8")
s = re.sub(r'(href|src)="(design-system/tokens\.css|vendor/pinyin-pro\.js)(\?v=\w+)?"', lambda m: f'{m.group(1)}="{m.group(2)}?v={v}"', s)
p.write_text(s, encoding="utf-8")
print("version", v)
