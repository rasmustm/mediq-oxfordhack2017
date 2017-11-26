from correlationDB import mergeWords

terms_and_frequency = {
	"psychology" : 6,
	"exercise" : 5,
	"aerobic" : 5,
	"anaerobic" : 4,
	"string theory" : 3
}

merge = mergeWords(terms_and_frequency)

print(merge)
