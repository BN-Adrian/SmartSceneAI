from flask import Flask, render_template, request, jsonify
import os
from deepface import DeepFace
import uuid

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
FACES_DIR = os.path.join(BASE_DIR, "faces")

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files.get('fileUpload')
        search_query = request.form.get('searchInput')
        result = None

        if uploaded_file:
            # creează un nume temporar unic
            temp_path = os.path.join(BASE_DIR, f"temp_{uuid.uuid4().hex}.jpg")
            uploaded_file.save(temp_path)

            try:
                df_list = DeepFace.find(img_path=temp_path, db_path=FACES_DIR, enforce_detection=False)
                result = []
                for df in df_list:
                    if not df.empty:
                        result.extend(df.to_dict(orient="records"))

                if not result:
                    result = {"message": "no match"}

            except Exception as e:
                result = {"error": str(e)}
            finally:
                if os.path.exists(temp_path):
                    os.remove(temp_path)

        print("File:", uploaded_file, "search:", search_query)
        return jsonify(result)

    return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)
