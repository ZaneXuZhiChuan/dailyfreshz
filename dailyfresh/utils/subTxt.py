from django.conf import settings
import django

# 预编译 django 文件
import os
import re

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dailyfresh.settings")
django.setup()

'''将Index中固定的src地址更改为static形式'''
class changeIndexSrc:
    index_html = os.path.join(settings.BASE_DIR, 'templates/index.html')
    save_path = os.path.join(settings.BASE_DIR, 'templates/index.html')
    with open(index_html, 'r') as f:
        with open(save_path, 'w') as f2:
            for line in f:
                pat = re.compile(r'src="([\w/\.]*)">')
                res = pat.findall(line)
                if len(res) > 0:
                    for r in res:
                        rp = "{% static '" + r + "' %}"
                        f2.write(re.sub(r, rp, line))
                else:
                    f2.write(line)

if __name__ == '__main__':
    changeIndex = changeIndexSrc()
