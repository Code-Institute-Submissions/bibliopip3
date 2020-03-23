import cgi
form = cgi.FieldStorage()
searchterm =  form.getvalue('searchbox')

index = open("index.html").read().format(first_header=searchterm)