from io import StringIO
from sylk_parser import SylkParser

parser = SylkParser("randogps38.slk")

fbuf = StringIO()
parser.to_csv(fbuf)

test_results = fbuf.getvalue()

print(test_results)
        
        