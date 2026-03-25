from functions import get_file_content as gfc

def test_get_file_content():

    try:
        gfc.get_file_content("calculator", "lorem.txt")
    except Exception as e:
        print(e)

    try:
        gfc.get_file_content("calculator", "main.py")
    except Exception as e:
        print(e)
    
    try:    
        gfc.get_file_content("calculator", "pkg/calculator.py")
    except Exception as e:
        print(e)
    
    try:            
        gfc.get_file_content("calculator", "/bin/cat")
    except Exception as e:
        print(e)
    
    try:
        gfc.get_file_content("calculator", "pkg/does_not_exist.py")
    except Exception as e:
        print(e)

    return 0

if __name__ == "__main__":
    test_get_file_content()