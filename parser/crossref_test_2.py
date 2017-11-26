from crossref.restful import Works
import signal, time
from multiprocessing import Process, Value, Array

array = []

def cross(array):
	works = Works()
	print("no")
	for e in works.query("cancer"):
		print("yes")
		print(e["DOI"])
		array.append(e["DOI"])

if __name__ == "__main__":
	array = Array("i", [])	

	p = Process(target=cross, name="Cross", args=(array,))
	p.start()
	time.sleep(4)
	p.terminate()
	p.join()

print(array[:])
