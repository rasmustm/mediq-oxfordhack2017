from crossref.restful import Works
import signal, time
from multiprocessing import Process, Value, Array, Manager

array = []

def cross(L):
	works = Works()
	print("no")
	for e in works.query("cancer"):
		print("yes")
		print(e["DOI"])
		L.append(e["DOI"])

m = []

if __name__ == "__main__":
	with Manager() as manager:
		l = manager.list()
		l.append("test")
		p = Process(target=cross, name="Cross", args=(l,))
		p.start()
		time.sleep(4)
		for e in l:
			m.append(l)
		p.terminate()
		p.join()

for element in l:
	print(element)
