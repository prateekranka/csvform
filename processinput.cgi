#!/Users/USER/PycharmProjects/ritproject/venv/Scripts/python.exe
import cgi

def getData():
    formData = cgi.FieldStorage()
    print formData

def htmlTop():
    print("""Content-type:text/html\n\n
            <!DOCTYPE html>
            <html lang="en">
                <head>
                    <meta charset= "utf-8">/)
                    <title>Form input</title>
                </head>
                <body>""")

def htmlTail():
    print("""</body>
            </html>""")

if __name__= "__main__":
    try:
        htmlTop()
        getdata()
        print("Hello!")
        htmlTail()
    except:
        cgi.print_exception()