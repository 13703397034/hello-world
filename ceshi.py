#coding: utf-8
import barcode

Code = barcode.get_barcode_class('code39')

bar = Code("123456",barcode.writer.ImageWriter(),False)
bar.save("image")
#code = Code(u'123456789')


