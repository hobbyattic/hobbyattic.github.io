from pathlib import Path
import json
root=Path(__file__).resolve().parent
items=json.loads((root/'products.json').read_text())
(root/'catalog.js').write_text('window.PRODUCTS = '+json.dumps(items,ensure_ascii=False,indent=2)+';',encoding='utf-8')
for p in items:
 d=root/'products'/p['id']; d.mkdir(parents=True,exist_ok=True)
 if not (d/'index.html').exists():
  import html
  template=next((root/'products').glob('*/index.html')).read_text()
  import re
  template=re.sub(r'data-product="[^"]*"',lambda m:'data-product="'+html.escape(p['id'],quote=True)+'"',template)
  template=re.sub(r'<title>.*?</title>',lambda m:'<title>'+html.escape(p['name'])+' | Suraj 3D Prints</title>',template)
  template=re.sub(r'<h1>.*?</h1>',lambda m:'<h1>'+html.escape(p['name'])+'</h1>',template)
  (d/'index.html').write_text(template)
print('Catalogue updated:',len(items),'products')
