from flask import Flask, request, jsonify, make_response, render_template
from flask_scss import Scss
import psycopg2
from models import listify, listing
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
Scss(app)

conn = psycopg2.connect(
    host="ep-sweet-tree-815718.ap-southeast-1.aws.neon.tech",  #neondb gw
    database="CareerHubDB", #
    user="ahmadgeneral86", #CareerHubDB
    password="eu6CwXJ9LRrB",
    port=5432 #
    #sslmode = True
)
cursor = conn.cursor()

### bikin route edit profile?

# @app.route('/',methods=['GET'])
# def hello():
#     return render_('templates','homepage.html')

@app.route('/', methods=['GET'])
def hello():
    return render_template('index.html')

@app.route('/error404', methods=['GET'])
def error404():
    return render_template('404.html')

@app.route('/registerPelamar', methods=['GET'])
def show_register_page():
    return render_template('registration.html')

@app.route('/loginPelamar', methods=['GET'])
def show_login_page():
    return render_template('loginPelamar.html')

@app.route('/getJobDetail', methods = ['GET'])
def show_jobdetail_page():
    return render_template('job-detail.html')

@app.route('/getJobList', methods = ['GET'])
def show_joblist_page():
    return render_template('job-list.html')


def checkColumn(columnName:str,tableName:str):
    query = f"SELECT column_name FROM information_schema.columns WHERE table_name = '{tableName}'"
    cursor.execute(query)
    columns = [row[0] for row in cursor.fetchall()]

    if columnName in columns:
        return True
    else:
        return False

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
    


@app.route('/loginPelamar', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email_pelamar')
    password = data.get('password')
    #print(email)
    try:
        # Mengecek apakah pengguna dengan username dan password yang diberikan ada dalam database
        cursor.execute("SELECT id_pelamar,nama_pelamar,email_pelamar,alamat_pelamar, pengalaman,pendidikan\
                        FROM pelamar WHERE email_pelamar = %s AND password = %s",(email, password))
        print(email)
        user = cursor.fetchone()

        if user:
            dictio = userProfile(user)
            # dictio.update({'message':'Login Successful','success':True})
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
        response = make_response(jsonify({'message': 'an error has ocuured', 'error': str(e), 'success': False}))
        response.status_code=500
        return response

#login dan registrasi perusahaan
@app.route('/registrasiPerusahaan',methods = ['POST'])
def registerPerusahaan():
    data = request.get_json()
    nama = data.get('nama_perusahaan')
    email = data.get('email_perusahaan')
    pswd = data.get('pswd_perusahaan')
    deskripsi = data.get('deskripsi_perusahaan')
    alamat = data.get('alamat_perusahaan')

    try:
        cursor.execute("INSERT INTO perusahaan VALUES(DEFAULT,%s,%s,%s,%s,%s)",(nama,email,pswd,deskripsi,alamat))
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
        cursor.execute("SELECT id_perusahaan,nama_perusahaan,email_perusahaan, deskripsi_perusahaan, alamat_perusahaan\
                        FROM perusahaan WHERE nama_perusahaan = %s AND pswd_perusahaan = %s", (nama,pswd))
        company = cursor.fetchone()
        
        if company:
            dictio=companyProfile(company)
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

@app.route('/editPelamar',methods=['PUT'])
def editPelamar():
    data = request.get_json()
    id_pelamar = data.get('id_pelamar')
    keychange = data.get('key')
    datachange = data.get('data')

    if checkColumn(keychange,"pelamar"):
        query = f"UPDATE pelamar SET {keychange} = %s WHERE id_pelamar = %s"
        try:
            cursor.execute(query,(datachange,id_pelamar))
            conn.commit()
            dictio = {'message':'Profil pengguna telah diupdate', 'success':True}
            response = make_response(jsonify(dictio))
            response.status_code=200
            return response
        except Exception as e: # ini dijadiin error code 500?
            conn.rollback()
            print(str(e))
            response = make_response(jsonify({'message': 'an error has ocuured', 'error': str(e),'success':False}))
            response.status_code=500
            return response
    else:
        response = make_response(jsonify({'message': 'invalid key','success':False}))
        response.status_code=404
        return response

@app.route('/editPerusahaan',methods=['PUT'])
def editPerusahaan():
    data = request.get_json()
    id_perusahaan = data.get('id_perusahaan')
    keychange = data.get('key')
    datachange = data.get('data')

    if checkColumn(keychange,"perusahaan"):
        query = f"UPDATE perusahaan SET {keychange} = %s WHERE id_perusahaan = %s"
        try:
            cursor.execute(query,(datachange,id_perusahaan))
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
    else:
        response = make_response(jsonify({'message': 'invalid key','success':False}))
        response.status_code=404
        return response

#nanti malem di test
@app.route('/',methods=['POST'])
def searchJob():
    data = request.get_json()
    keySearch= data.get('key')   
    dataSearch = data.get('data')
    query = f"SELECT pekerjaan.id_pekerjaan, pekerjaan.posisi,pekerjaan.gaji,\
                            perusahaan.nama_perusahaan,kategori.nama_kategori \
                            FROM pekerjaan INNER JOIN perusahaan \
                            ON pekerjaan.id_perusahaan = perusahaan.id_perusahaan \
                            INNER JOIN kategori \
                            ON pekerjaan.id_kategori = kategori.id_kategori \
                            WHERE {keySearch} = %s"
    #yang ditampilkan itu posisi, gaji, perusahaan, kategori, 
    try:
        cursor.execute(query,(dataSearch,))
        joblist = cursor.fetchall()
        if joblist:
            print(joblist)
            dictio = listify(joblist)
            response = make_response(jsonify(dictio))
            response.status_code=200
            return response
        else:
            response = make_response(jsonify({'message': 'Pekerjaan dengan ' + keySearch + '=' +dataSearch+ \
                                                ' sedang tidak tersedia','success':False }))
            response.status_code=404
            return response
    except Exception as e:
        print(str(e))
        response = make_response(jsonify({'message': 'an error has ocuured', 'error': str(e),'succes':False}))
        response.status_code=500
        return response

#ini mungkin berubah
@app.route('/getJobDetail', methods = ['GET'])
def getJobDetail():
    data = request.get_json()
    jobId = data.get('id_pekerjaan')

    try:
        cursor.execute("SELECT deskripsi,kualifikasi FROM pekerjaan WHERE id_pekerjaan = %s",(jobId))   #ganti Query ini ntar
        jobDetails = cursor.fetchone()
        if jobDetails:
            #print(jobDetails)
            dictio = {
                'deskripsi': jobDetails[0],
                'kualifikasi': jobDetails[1]
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
        response = make_response(jsonify({'message': 'an error has ocuured', 'error': str(e),'success': False}))
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
                        response = make_response(jsonify({'message': 'an error has ocuured', 'error': str(e),'success':False}))
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
    string = "letters/"+id_pekerjaan+id_pelamar+filename
    query = f"INSERT INTO lamaran VALUES(DEFAULT,%s,%s,%s,'0',%s)"
    try:
        cursor.execute(query,(id_pekerjaan,id_pelamar,tanggal,string))
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

    if checkColumn(keychange,"pekerjaan"):
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
    else:
        response = make_response(jsonify({'message': 'invalid key','success':False}))
        response.status_code=404
        return response

@app.route('/editLetter',methods = ['PUT'])
def editLetter():
    data = request.get_json()
    id_lamaran = data.get('id_lamaran')
    keychange = data.get('key')
    datachange = data.get('data')

    if checkColumn(keychange,"lamaran"):
        query = f"UPDATE lamaran SET {keychange} = %s WHERE id_lamaran = %s"
        try:
            cursor.execute(query,(datachange,id_lamaran))
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
    else:
        response = make_response(jsonify({'message': 'invalid key','success':False}))
        response.status_code=404
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

@app.route('/getAllLetter',methods=['GET']) #yang pakai method ini adalah company
def getAllLetter():
    data = request.get_json()
    id_perusahaan = data.get('id_perusahaan')
    query = f"SELECT lamaran.id_lamaran,pekerjaan.posisi,pelamar.nama_pelamar\
            ,pelamar.pengalaman,pelamar.pendidikan, lamaran.tanggal FROM lamaran\
            INNER JOIN pekerjaan ON lamaran.id_pekerjaan=pekerjaan.id_pekerjaan\
            INNER JOIN pelamar ON lamaran.id_pelamar=pelamar.id_pelamar\
            WHERE pekerjaan.id_perusahaan = %s"
    
    try:
        cursor.execute(query,(id_perusahaan,))
        letterList = cursor.fetchall()
        if letterList is not None:
            dictio = listing(letterList)
            response = make_response(jsonify(dictio))
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

@app.route('/getLetterDetails' ,methods=['GET'])
def letterDetail():
    data = request.get_json()
    letterId = data.get('id_lamaran')

    try:
        cursor.execute("SELECT * FROM lamaran WHERE id_lamaran = %s",(letterId))   #ganti Query ini ntar
        letterDetails = cursor.fetchone()
        if letterDetails:
            #print(jobDetails)
            # dictio = {
            #     'id_pekerjaan': jobDetails[0],
            #     'id_perusahaan': jobDetails[1],
            #     'id_kategori': jobDetails[2],
            #     'posisi': jobDetails[3],
            #     'deskripsi': jobDetails[4],
            #     'kualifikasi': jobDetails[5],
            #     'gaji': jobDetails[6]
            # }
            #dictio.update({'success':True})
            response = make_response(jsonify(letterDetails))
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


@app.route('/addRating',methods=['POST'])
def addRating():
    data = request.get_json()
    id_pekerjaan = data.get('id_pekerjaan')
    id_pelamar = data.get('id_pelamar')
    rating = data.get('rating')
    komentar = data.get('komentar')

    try:
        cursor.execute("INSERT INTO ulasan VALUES(DEFAULT,%s,%s,%s,%s)",(id_pekerjaan,id_pelamar,rating,komentar))
        conn.commit()
        dictio = {'message':'ulasan telah ditambahkan', 'success':True}
        response = make_response(jsonify(dictio))
        response.status_code=200
        return response
    except Exception as e: # ini dijadiin error code 500?
        print(str(e))
        response = make_response(jsonify({'message': 'an error has occured', 'error': str(e),'success':False}))
        response.status_code=500
        return response

@app.route('/editrating',methods=['PUT'])
def editRating():
    data=request.get_json()
    id_ulasan = data.get('id_ulasan')
    keychange = data.get('key')
    datachange = data.get('data')
    

    if checkColumn(keychange,"ulasan"):
        query = f"UPDATE ulasan SET {keychange} = %s WHERE id_pelamar = %s"
        try:
            cursor.execute(query,(datachange,id_ulasan))
            conn.commit()
            dictio = {'message':'ulasan telah diperbarui', 'success':True}
            response = make_response(jsonify(dictio))
            response.status_code=200
            return response
        except Exception as e: # ini dijadiin error code 500?
            print(str(e))
            response = make_response(jsonify({'message': 'an error has occured', 'error': str(e),'success':False}))
            response.status_code=500
            return response
    else:
        response = make_response(jsonify({'message': 'invalid key','success':False}))
        response.status_code=404
        return response

@app.route('/removeRating',methods=['DELETE'])
def removeRating():
    data=request.get_json()
    id_ulasan = data.get('id_ulasan')

    try:
        cursor.execute("DELETE FROM ulasan WHERE id_pelamar = %s",(id_ulasan,))
        conn.commit()
        dictio = {'message':'ulasan telah dihapus', 'success':True}
        response = make_response(jsonify(dictio))
        response.status_code=200
        return response
    except Exception as e: # ini dijadiin error code 500?
        print(str(e))
        response = make_response(jsonify({'message': 'an error has occured', 'error': str(e),'success':False}))
        response.status_code=500
        return response

## Run The App
if __name__ == '__main__':
    app.run(debug=True)



