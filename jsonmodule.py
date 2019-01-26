
import json

a={'a':'prasanna','b':'siva'}
b=json.dump(a)
print(b)
b=json.dumps(a)
d=json.load(b)
d=json.loads(b)
print(d)