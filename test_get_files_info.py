from functions import get_files_info as gfi


def test_get_files_info():
    try :
        gfi.get_files_info("calculator", ".")
    except Exception as e:
        print(e)
    
    try:    
        gfi.get_files_info("calculator", "pkg")
    except Exception as e:
        print(e)
    
    try:            
        gfi.get_files_info("calculator", "/bin")
    except Exception as e:
        print(e)
        
    try:
        gfi.get_files_info("calculator", "../")
    except Exception as e:
        print(e)

    return 0

if __name__ == "__main__":
    test_get_files_info()
