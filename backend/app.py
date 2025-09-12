from flask import Flask, render_template,request
import os

BASE_DIR=os.path.abspath(os.path.join(os.path.dirname(__file__),".."))

app= Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR,"templates"),
    static_folder=os.path.join(BASE_DIR,"static")
)

@app.route('/',methods=['GET','POST'])

def index():
    if request.method=='POST':
        uploaded_file=request.files.get('fileUpload')
        search_query=request.form.get('searchInput')
        print(uploaded_file,search_query)
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)