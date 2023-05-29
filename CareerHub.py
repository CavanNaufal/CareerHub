from flask import Flask, request, jsonify, make_response, render_template
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
#menghandle request Methods OPTIONS
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

def listify(jobList:list):
    res = []
    for item in jobList:
        item_dict = {
            'id_pekerjaan': item[0],
            'posisi': item[1],
            'gaji': item[2],
            'nama_perusahaan': item[3],
            'nama_kategori': item[4],
            'success' : True
        }
        res.append(item_dict)
    return res

#######   ini dikerjain besok aja kah?
# def listing(letterList:list):
#     res = []
#     for item in letterList:
#         item_dict = {
#             'id_pekerjaan': item[0],
#             'posisi': item[1],
#             'gaji': item[2],
#             'nama_perusahaan': item[3],
#             'nama_kategori': item[4],
#             'success' : True
#         }
#         res.append(item_dict)
#     return res

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
    
    #headers = {'Content-Type':'application/json'}
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
                            (nama_pelamar,email_pelamar,password, alamat_pelamar, pengalaman,pendidikan))
        
            conn.commit()  #melakukan update database
            dictio = {'message': 'Registration successful','success':True}
            response = make_response(jsonify(dictio))
            response.status_code=200
            return response
    # except psycopg2.IntegrityError as e:
    #     conn.rollback()
    #     return jsonify({'message': 'Username or email already exists'})
        except Exception as e:
            print(str(e))
            response = make_response(jsonify({'message': 'an error has ocuured', 'error': str(e),'success':False}))
            response.status_code=500
            return response
    

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
            # dictio = dict(user)
            # dictio.update({'message':'Login Successful','success':True})
            response = make_response(jsonify(user))
            response.status_code=200
            return response
        else:
            dictio = {'message':'Invalid username or password','success':False}
            response = make_response(jsonify(dictio))
            response.status_code=404
            return response
    except Exception as e:
        print(str(e))
        response = make_response(jsonify({'message': 'an error has ocuured', 'error': str(e), 'success': False}))
        response.status_code=500
        return response

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
        dictio = {'message': 'Company Registration successful','success':True}
        response = make_response(jsonify(dictio))
        response.status_code=200
        return response
        
    except psycopg2.IntegrityError as e:
        conn.rollback()
        return jsonify({'message': 'Username already exists'})
    except Exception as e:
        print(str(e))
        response = make_response(jsonify({'message': 'an error has ocuured', 'error': str(e), 'success': False}))
        response.status_code=500
        return response
    
@app.route('/loginPerusahaan', methods=['POST'])
def loginPerusahaan():
    data = request.get_json()
    nama = data.get('nama_perusahaan')
    pswd = data.get('pswd_perusahaan')

    try:
        cursor.execute("SELECT * FROM perusahaan WHERE nama_perusahaan = %s AND pswd_perusahaan = %s", (nama,pswd))
        company = cursor.fetchone()
        
        if company:
            #dictio=Convert(company,is_success)
            # dictio.update({'message':'Login Company Successful','success':True})
            response = make_response(jsonify(dictio))
            response.status_code=200
            return response
        else:
            dictio = {'message':'Invalid username or password','success':False}
            response = make_response(jsonify(dictio))
            response.status_code=404
            return response
    except Exception as e:
        print(str(e))
        response = make_response(jsonify({'message': 'an error has ocuured', 'error': str(e),'success':False}))
        response.status_code=500
        return response
        
    

@app.route('/findbyPosition',methods =['GET'])
def findbyPosition():
    data = request.get_json()
    posisi = data.get('posisi')
    
    try:
        cursor.execute("SELECT pekerjaan.id_pekerjaan, pekerjaan.posisi,pekerjaan.gaji,\
                            perusahaan.nama_perusahaan,kategori.nama_kategori \
                            FROM pekerjaan INNER JOIN perusahaan \
                            ON pekerjaan.id_perusahaan = perusahaan.id_perusahaan \
                            INNER JOIN kategori \
                            ON pekerjaan.id_kategori = kategori.id_kategori \
                            WHERE pekerjaan.posisi = %s", (posisi,))       
        joblist = cursor.fetchall()
        if joblist:
            print(joblist)
            dictio = listify(joblist)
            response = make_response(jsonify(dictio))
            response.status_code=200
            return response
        else:
            response = make_response(jsonify({'message': 'Pekerjaan dengan ' + posisi + ' sedang tidak tersedia','success':False}))
            response.status_code=404
            return response
    except Exception as e:
        print(str(e))
        response = make_response(jsonify({'message': 'an error has ocuured', 'error': str(e)}))
        response.status_code=500
        return response
        


@app.route('/findbyCompany', methods=['GET'])
def findbyCompany():
    data = request.get_json()
    nama_perusahaan = data.get('nama_perusahaan')
    
    try:
        cursor.execute("SELECT pekerjaan.id_pekerjaan, pekerjaan.posisi,pekerjaan.gaji,\
                            perusahaan.nama_perusahaan,kategori.nama_kategori \
                            FROM pekerjaan INNER JOIN perusahaan \
                            ON pekerjaan.id_perusahaan = perusahaan.id_perusahaan \
                            INNER JOIN kategori \
                            ON pekerjaan.id_kategori = kategori.id_kategori \
                            WHERE nama_perusahaan = %s", (nama_perusahaan,))
       
        joblist = cursor.fetchall()
        
        if joblist:
            dictio = listify(joblist)
            response = make_response(jsonify(dictio))
            response.status_code=200
            return response
        else:
            dictio = {'message': 'Perusahaan ' + nama_perusahaan + ' sedang tidak membuka lamaran','success': False}
            response = make_response(jsonify(dictio))
            response.status_code=404
            return response
    except Exception as e:
        print(str(e))
        response = make_response(jsonify({'message': 'an error has ocuured', 'error': str(e),'success':False}))
        response.status_code=500
        return response
#findbyCategory, findbyPosition dan findbyCompany kita single route?
@app.route('/findbyCategory', methods=['GET'])
def findbyCategory():
    data = request.get_json()
    nama_kategori = data.get('nama_kategori')

    try:
        cursor.execute("SELECT pekerjaan.id_pekerjaan,pekerjaan.posisi,pekerjaan.gaji,\
                            perusahaan.nama_perusahaan,kategori.nama_kategori\
                            FROM pekerjaan INNER JOIN perusahaan\
                            ON pekerjaan.id_perusahaan = perusahaan.id_perusahaan\
                            INNER JOIN kategori\
                            ON pekerjaan.id_kategori = kategori.id_kategori\
                            WHERE nama_kategori = %s", (nama_kategori,))
        joblist = cursor.fetchall()
        if joblist:
            dictio = listify(joblist)
            response = make_response(jsonify(dictio))
            response.status_code=200
            return response
        else:
            dictio = {'message': 'Pekerjaan kategori ' + nama_kategori + ' sedang tidak tersedia' ,'success': False}
            response = make_response(jsonify(dictio))
            response.status_code=404
            return response
    except Exception as e:
        print(str(e))
        response = make_response(jsonify({'message': 'an error has ocuured', 'error': str(e),'success': False}))
        response.status_code=500
        return response


@app.route('/getJobDetail', methods = ['GET'])
def getJobDetail():
    data = request.get_json()
    jobId = data.get('id_pekerjaan')

    try:
        cursor.execute("SELECT * FROM pekerjaan WHERE id_pekerjaan = %s",(jobId))   #ganti Query ini ntar
        jobDetails = cursor.fetchone()
        if jobDetails:
            print(jobDetails)
            dictio = {
                'id_pekerjaan': jobDetails[0],
                'id_perusahaan': jobDetails[1],
                'id_kategori': jobDetails[2],
                'posisi': jobDetails[3],
                'deskripsi': jobDetails[4],
                'kualifikasi': jobDetails[5],
                'gaji': jobDetails[6]
            }
            dictio.update({'success':True})
            response = make_response(jsonify(dictio))
            response.status_code=200
            return response
        else:
            response = make_response(jsonify({'message': 'Pekerjaan tidak ditemukan','success':False}) )
            response.status_code=404
            return response 
    except Exception as e: # ini dijadiin error code 500?
        print(str(e))
        response = make_response(jsonify({'message': 'an error has ocuured', 'error': str(e)}))
        response.status_code=500
        return response

@app.route('/addJob',methods=['POST'])
def addJob():
    data = request.get_json()
    nama_perusahaan = data.get('nama_perusahaan') #ini dijadiin id_perusahaan ajah?
    kategori = data.get('kategori')  #ini dijadiin id_kategori ajah?
    posisi = data.get('posisi')
    deskripsi = data.get('deskripsi')
    kualifikasi = data.get('kualifikasi')
    gaji = data.get('gaji')

    try:
        cursor.execute("SELECT id_perusahaan FROM perusahaan WHERE nama_perusahaan = %s",(nama_perusahaan,))
        id_perusahaan = cursor.fetchone()
        if id_perusahaan is not None:
            try:
                cursor.execute("SELECT id_kategori FROM kategori WHERE nama_kategori = %s",(kategori,))
                id_kategori = cursor.fetchone()
                if id_kategori is not None:
                    try:
                        cursor.execute("INSERT INTO pekerjaan VALUES(DEFAULT,%s,%s,%s,%s,%s,%s)",    #potensi bug
                                       (id_perusahaan,id_kategori,posisi,deskripsi,kualifikasi,gaji))
                        conn.commit()
                        dictio = {'message':'Job ' +posisi+' telah ditambahkan', 'success':True}
                        response = make_response(jsonify(dictio))
                        response.status_code=200
                        return response
                    except Exception as e: # ini dijadiin error code 500?
                        conn.rollback()
                        print(str(e))
                        response = make_response(jsonify({'message': 'an error has ocuured', 'error': str(e)}))
                        response.status_code=500
                        return response
                else:
                    response = make_response(jsonify({'message': 'Kategori tidak ditemukan','success':False}) )
                    response.status_code=404
                    return response 
            except Exception as e: # ini dijadiin error code 500?
                print(str(e))
                response = make_response(jsonify({'message': 'an error has ocuured', 'error': str(e),'success':False}))
                response.status_code=500
                return response
        else:
            response = make_response(jsonify({'message': 'Perusahaan ' +nama_perusahaan+ ' tidak ditemukan','success':False}) )
            response.status_code=404
            return response 
    except Exception as e: # ini dijadiin error code 500?
        print(str(e))
        response = make_response(jsonify({'message': 'an error has ocuured', 'error': str(e), 'success': False}))
        response.status_code=500
        return response

@app.route('/addLetter',methods = ['POST'])
def addLetter():
    data = request.get_json()
    id_pekerjaan=data.get('id_pekerjaan')
    id_pelamar = data.get('id_pelamar')
    tanggal = data.get('tanggal') #ttransform tanggal
    filename = data.get('filename')
    query = f"INSERT INTO pelamar VALUES(DEFAULT,%s,%s,%s,0,'HRD/{filename}')"
    try:
        cursor.execute(query,(id_pekerjaan,id_pelamar,tanggal))
        conn.commit()
        dictio = {'message':'lamaran telah ditambahkan', 'success':True}
        response = make_response(jsonify(dictio))
        response.status_code=200
        return response
    except Exception as e: # ini dijadiin error code 500?
        conn.rollback()
        print(str(e))
        response = make_response(jsonify({'message': 'an error has occured', 'error': str(e),'success':False}))
        response.status_code=500
        return response
        

@app.route('/editJob',methods=['PUT'])
def editJob():
    data = request.get_json()
    id_pekerjaan = data.get('id_pekerjaan')
    keychange = data.get('key')
    datachange = data.get('data')
    query = f"UPDATE pekerjaan SET {keychange} = %s WHERE id_pekerjaan = %s"
    try:
        cursor.execute(query,(datachange,id_pekerjaan))
        conn.commit()
        dictio = {'message':'Job  telah diupdate', 'success':True}
        response = make_response(jsonify(dictio))
        response.status_code=200
        return response
    except Exception as e: # ini dijadiin error code 500?
        conn.rollback()
        print(str(e))
        response = make_response(jsonify({'message': 'an error has ocuured', 'error': str(e),'success':False}))
        response.status_code=500
        return response

@app.route('/editLetter',methods = ['PUT'])
def editLetter():
    data = request.get_json()
    id_pekerjaan = data.get('id_pekerjaan')
    keychange = data.get('key')
    datachange = data.get('data')
    query = f"UPDATE lamaran SET {keychange} = %s WHERE id_pekerjaan = %s"
    try:
        cursor.execute(query,(datachange,id_pekerjaan))
        conn.commit()
        dictio = {'message':'lamaran  telah diupdate', 'success':True}
        response = make_response(jsonify(dictio))
        response.status_code=200
        return response
    except Exception as e: # ini dijadiin error code 500?
        conn.rollback()
        print(str(e))
        response = make_response(jsonify({'message': 'an error has occured', 'error': str(e),'success':False}))
        response.status_code=500
        return response
    


@app.route('/removeJob', methods=['DELETE'])
def removeJob():
    data = request.get_json()
    id_pekerjaan = data.get('id_pekerjaan')
    
    try:
        cursor.execute("DELETE FROM pekerjaan WHERE id_pekerjaan = %s",(id_pekerjaan,))
        conn.commit()
        dictio = {'message':'lowongan  telah dihapus', 'success':True}
        response = make_response(jsonify(dictio))
        response.status_code=200
        return response
    except Exception as e: # ini dijadiin error code 500?
        print(str(e))
        response = make_response(jsonify({'message': 'an error has occured', 'error': str(e),'success':False}))
        response.status_code=500
        return response


@app.route('/removeLetter',methods=['DELETE'])
def removeLetter():
    data = request.get_json()
    id_lamaran = data.get('id_lamaran')

    try:
        cursor.execute("DELETE FROM lamaran WHERE id_lamaran = %s",(id_lamaran,))
        conn.commit()
        dictio = {'message':'lamaran  telah dihapus', 'success':True}
        response = make_response(jsonify(dictio))
        response.status_code=200
        return response
    except Exception as e: # ini dijadiin error code 500?
        print(str(e))
        response = make_response(jsonify({'message': 'an error has occured', 'error': str(e),'success':False}))
        response.status_code=500
        return response

@app.route('/getAllLetter',methods=['GET'])
def getAllLetter():
    data = request.get_json()
    id_perusahaan = data.get('id_perusahaan')
    query = f"SELECT lamaran.id_lamaran,lamaran.id_pekerjaan,pekerjaan.id_perusahaan\
            ,pelamar.nama_pelamar FROM lamaran\
            INNER JOIN pekerjaan ON lamaran.id_pekerjaan=pekerjaan.id_pekerjaan\
            INNER JOIN pelamar ON lamaran.id_pelamar=pelamar.id_pelamar\
            WHERE pekerjaan.id_perusahaan = %s"
    
    try:
        cursor.execute(query,(id_perusahaan,))
        letterList = cursor.fetchall()
        if letterList is not None:
            response = make_response(jsonify(letterList))
            response.status_code=200
            return response
        else:
            response = make_response(jsonify({'message': 'tidak ada lamaran yang masuk','success':False}) )
            response.status_code=404
            return response 
    except Exception as e: # ini dijadiin error code 500?
        print(str(e))
        response = make_response(jsonify({'message': 'an error has occured', 'error': str(e),'success':False}))
        response.status_code=500
        return response


## Run The App
if __name__ == '__main__':
    app.run(debug=True)



