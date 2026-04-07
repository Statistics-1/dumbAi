from functions import write_file as wf

try:
    print(wf.write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
except Exception as e:
    print(e)

try:    print(wf.write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
except Exception as e:            
    print(e)

try:    print(wf.write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
except Exception as e:            
    print(e)