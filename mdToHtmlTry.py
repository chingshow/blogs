#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 使用方法 python markdown_convert.py filename

import sys
import markdown
import codecs


css = '''
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<style type="text/css">
<!-- 此处省略掉markdown的css样式，因为太长了 -->
</style>
'''


def main(argv):
    name = argv[0]
    in_file = '%s.md' % (name)
    out_file = '%s.html' % (name)

    input_file = codecs.open(in_file, mode="r", encoding="utf-8")
    text = input_file.read()
    html = markdown.markdown(text)

    output_file = codecs.open(out_file, "w", encoding="utf-8", errors="xmlcharrefreplace")
    output_file.write(css+html)


if __name__ == "__main__":
    main(sys.argv[1:])

