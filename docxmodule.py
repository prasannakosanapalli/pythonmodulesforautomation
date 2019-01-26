#-*- coding: utf-8 -*-

import docx

a=docx.document(filename or variable)
a.paragraphs()
a.paragraph[0].text
a.paragraph[1].runs[1].text
a.add_paraagraph("content or varaible")
a.save("file name to save")
a.add_heading("heading name",0)
a.add_pactures()