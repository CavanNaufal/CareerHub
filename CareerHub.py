from flask import Flask, request, jsonify, make_response, render_template
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)
# Konfigurasi koneksi database, nanti diganti
conn = psycopg2.connect(
    host="ep-sweet-tree-815718.ap-southeast-1.aws.neon.tech",  #neondb gw
    database="CareerHubDB", #
    user="ahmadgeneral86", #CareerHubDB
    password="eu6CwXJ9LRrB",
    port=5432 #
    #sslmode = True
)
cursor = conn.cursor()

@app.route('/',methods=['GET'])
def hello():
    response = make_response(jsonify({'message': 'Hello World'}))
    response.status_code=200
    return response
    

@app.route('/registerPelamar', methods=['GET'])
def show_registration_form():
    return render_template('index.html')

#Login dan register pelamar
@app.route('/registerPelamar', methods=['POST'])
def register():
    data = request.get_json()
    nama_pelamar = data.get('nama_pelamar')
    alamat_pelamar = data.get('alamat_pelamar')
    email_pelamar = data.get('email_pelamar')
    password = data.get('password')
    pengalaman = data.get('pengalaman')
    pendidikan = data.get('pendidikan')

    try:
        # Memasukkan data pengguna baru ke dalam database
        cursor.execute("INSERT INTO pelamar VALUES(DEFAULT,%s,%s,%s,%s,%s,%s)",
                        (nama_pelamar, email_pelamar, password, alamat_pelamar, pengalaman, pendidikan))

        conn.commit()  # Melakukan update database
        return jsonify({'message': 'Registration successful'})
    except Exception as e:
        return jsonify({'message': 'Registration failed', 'error': str(e)})

@app.route('/loginPelamar', methods=['GET'])
def show_login_form():
    return render_template('loginPelamar.html')

@app.route('/loginPelamar', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email_pelamar')
    password = data.get('password')
    #print(email)
    try:
        # Mengecek apakah pengguna dengan username dan password yang diberikan ada dalam database
        cursor.execute("SELECT * FROM pelamar WHERE email_pelamar = %s AND password = %s",
                        (email, password))
        print(email)
        user = cursor.fetchone()

        if user:
            dictio = {'message':'Login Successful','success':True}
            response = make_response(jsonify(dictio))
            response.status_code=200
            return response
        else:
            return jsonify({'message': 'Invalid username or password'})
    except Exception as e:
        return jsonify({'message': 'Login failed', 'error': str(e)})

#login dan registrasi perusahaan
@app.route('/registrasiPerusahaan',methods = ['POST'])
def registerPerusahaan():
    data = request.get_json()
    nama = data.get('nama_perusahaan')
    pswd = data.get('pswd_perusahaan')
    deskripsi = data.get('deskripsi_perusahaan')
    alamat = data.get('alamat_perusahaan')

    try:
        cursor.execute("INSERT INTO perusahaan VALUES(DEFAULT,%s,%s,%s,%s)",(nama,pswd,deskripsi,alamat))
        conn.commit()
        return jsonify({'message': 'Registration successful'})
    except psycopg2.IntegrityError as e:
        conn.rollback()
        return jsonify({'message': 'Username already exists'})
    except Exception as e:
        return jsonify({'message': 'Registration failed', 'error': str(e)})
    
@app.route('/loginPerusahaan', methods=['POST'])
def loginPerusahaan():
    data = request.get_json()
    nama = data.get('nama_perusahaan')
    pswd = data.get('pswd_perusahaan')

    try:
        cursor.execute("SELECT * FROM perusahaan WHERE nama_perusahaan = %s AND pswd_perusahaan = %s", (nama,pswd))
        company = cursor.fetchone()
        
        if company:
            response = make_response(jsonify({'message':'Login success'}))
            response.status_code=200
            return response
        else:
            response = make_response(jsonify({'message':'Login Failed'}))
            response.status_code=404
            return response
    except Exception as e:
        return jsonify({'message': 'Login failed', 'error': str(e)})
    

@app.route('/findbyPosition',methods =['GET'])
def findbyPosition():
    data = request.get_json()
    posisi = data.get('posisi')
    
    try:
        cursor.execute("SELECT pekerjaan.posisi,pekerjaan.gaji,perusahaan.nama_perusahaan,kategori.nama_kategori \
                            FROM pekerjaan INNER JOIN perusahaan \
                            ON pekerjaan.id_perusahaan = perusahaan.id_perusahaan \
                            INNER JOIN kategori \
                            ON pekerjaan.id_kategori = kategori.id_kategori \
                            WHERE pekerjaan.posisi = %s", (posisi,))       
        joblist = cursor.fetchall()
        if joblist:
            response = make_response(jsonify(joblist))
            response.status_code=200
            return response
        else:
            
            response = make_response(jsonify({'message': 'Pekerjaan dengan ' + posisi + ' sedang tidak tersedia'}))
            response.status_code=404
            return response
    except Exception as e:
        response = make_response(jsonify({'message': 'an error has ocuured', 'error': str(e)}))
        response.status_code=500
        return response
        


@app.route('/findbyCompany', methods=['GET'])
def findbyCompany():
    data = request.get_json()
    nama_perusahaan = data.get('nama_perusahaan')
    
    try:
        cursor.execute("SELECT pekerjaan.posisi,pekerjaan.gaji,perusahaan.nama_perusahaan,kategori.nama_kategori \
                            FROM pekerjaan INNER JOIN perusahaan \
                            ON pekerjaan.id_perusahaan = perusahaan.id_perusahaan \
                            INNER JOIN kategori \
                            ON pekerjaan.id_kategori = kategori.id_kategori \
                            WHERE nama_perusahaan = %s", (nama_perusahaan,))
       
        joblist = cursor.fetchall()
        
        if joblist:
            
            response = make_response(jsonify(joblist))
            response.status_code=200
            return response
        else:
            response = make_response(jsonify({'message': 'Perusahaan ' + nama_perusahaan + ' sedang tidak membuka lamaran'}))
            response.status_code=404
            return response
    except Exception as e:
        response = make_response(jsonify({'message': 'an error has ocuured', 'error': str(e)}))
        response.status_code=500
        return response

# def findbyCompany():
#     data = request.get_json()
#     nama_perusahaan = data.get('nama_perusahaan')

#     try:
#         cursor.execute("SELECT id_perusahaan FROM perusahaan WHERE nama_perusahaan = %s",(nama_perusahaan))
#         companyId = cursor.fetchone()
#         if companyId:
#             cursor.execute("SELECT * FROM pekerjaan WHERE id_perusahaan = %d",(companyId))
#             joblist = cursor.fetchall()
#             if joblist:
#                 response = make_response(jsonify(joblist))
#                 response.status_code=200
#                 return response
#             else:
#                 return jsonify({'message': 'Perusahaan ' + nama_perusahaan + ' sedang tidak membuka lamaran'})
#         else:
#            response = make_response(jsonify({'message': 'Perusahaan ' + nama_perusahaan + 'tidak ditemukan'}) )
#            response.status_code=404
#            return response 
#     except Exception as e:
#         return jsonify({'message': 'an error has ocuured', 'error': str(e)})


@app.route('/findbyCategory', methods=['GET'])
def findbyCategory():
    data = request.get_json()
    nama_kategori = data.get('nama_kategori')

    try:
        cursor.execute("SELECT pekerjaan.posisi,pekerjaan.gaji,perusahaan.nama_perusahaan,kategori.nama_kategori\
                            FROM pekerjaan INNER JOIN perusahaan\
                            ON pekerjaan.id_perusahaan = perusahaan.id_perusahaan\
                            INNER JOIN kategori\
                            ON pekerjaan.id_kategori = kategori.id_kategori\
                            WHERE nama_kategori = %s", (nama_kategori,))
        joblist = cursor.fetchall()
        if joblist:
            response = make_response(jsonify(joblist))
            response.status_code=200
            return response
        else:
            response = make_response(jsonify({'message': 'Pekerjaan kategori ' + nama_kategori + ' sedang tidak tersedia'}))
            response.status_code=404
            return response
        
    except Exception as e:
        response = make_response(jsonify({'message': 'an error has ocuured', 'error': str(e)}))
        response.status_code=500
        return response
# def findbyCategory():
#     data = request.get_json()
#     kategori = data.get('kategori')

#     try:
#         cursor.execute("SELECT id_category FROM kategori WHERE nama_kategori = %s", (kategori))
#         idCategory = cursor.fetchone()
#         if idCategory:
#             cursor.execute("SELECT * FROM pekerjaan WHERE id_kategori = %d", (idCategory))  #apa cuma posisi, gaji dan perusahaan berarti inner join
#             joblist = cursor.fetchall()
#             if joblist:
#                 response = make_response(jsonify(joblist))
#                 response.status_code=200
#                 return response
#             else:
#                  return jsonify({'message': 'Pekerjaan dengan kategori ' + kategori + ' sedang tidak tersedia'})
#         else:
#             response = make_response(jsonify({'message': 'Kategori ' + kategori + 'tidak ditemukan'}) )
#             response.status_code=404
#             return response 
#     except Exception as e:
#         return jsonify({'message': 'an error has ocuured', 'error': str(e)})

@app.route('/getJobDetail', methods = ['GET'])
def getJobDetail():
    data = request.get_json()
    jobId = data.get('id_pekerjaan')

    try:
        cursor.execute("SELECT * FROM pekerjaan WHERE id_pekerjaan = %d",(jobId))
        jobDetails = cursor.fetchone()
        if jobDetails:
            response = make_response(jsonify(jobDetails))
            response.status_code=200
            return response
        else:
            response = make_response(jsonify({'message': 'Pekerjaan tidak ditemukan'}) )
            response.status_code=404
            return response 
    except Exception as e: # ini dijadiin error code 500?
        response = make_response(jsonify({'message': 'an error has ocuured', 'error': str(e)}))
        response.status_code=500
        return response
    



## Run The App
if __name__ == '__main__':
    app.run(debug=True)



