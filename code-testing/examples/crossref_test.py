from crossref.restful import Works
import signal, time

works = Works()

class Timeout(Exception):
	pass

def raiseTimeout(sig, frame):
	raise Timeout

signal.signal(signal.SIGALRM, raiseTimeout)
signal.alarm(2)

array = []

try:
	for e in works.query("cancer"):
		array.add(e["DOI"])
except Timeout:
	print("took too long")

print(array)
