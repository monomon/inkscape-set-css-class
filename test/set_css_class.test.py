import sys
sys.path.append('../')

import unittest
import inkex
from set_css_class import SetCSSClass

testdoc = 'svg/set_css_class.test.svg'

def get_rect(doc):
    return doc.xpath('//*[@id="rect"]')[0]

class SetCSSClassBasicTest(unittest.TestCase):
    def test_not_clearing_styles(self):
        args = ['--name=rect', '--id=rect', '--clear_styles=False', testdoc]
        e = SetCSSClass()
        e.affect(args, False)

        rect = get_rect(e.document)
        self.assertEqual(rect.get('class'), 'rect')
        self.assertEqual(rect.get('style'), 'fill:#000000')

    def test_clearing_styles(self):
        args = ['--name=rect', '--id=rect', '--clear_styles=True', testdoc]
        e = SetCSSClass()
        e.affect(args, False)

        rect = get_rect(e.document)
        self.assertEqual(rect.get('class'), 'rect')
        self.assertEqual(rect.get('style'), '')


if __name__ == '__main__':
    unittest.main()
