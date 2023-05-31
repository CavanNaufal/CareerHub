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

#def listing
def listing(letterList:list):
    res=[]
    for item in letterList:
        item_dict={
            'id_lamaran' : item[0],
            'posisi' : item[1],
            'nama_pelamar':item[2],
            'pengalaman' : item[3],
            'pendidikan' : item[4],
            'tanggal_lamaran': item[5],
            'success': True
        }
        res.append(item_dict)
    return res

def userProfile(user:object):
    dictio={
        'id_pelamar':user[0],
        'nama_pelamar':user[1],
        'email_pelamar':user[2],
        'alamat_pelamar':user[3],
        'pengalaman' :user[4],
        'pendidikan' :user[5],
        'success' : True
    }
    return dictio

#def companyProfile(response)
def companyProfile(company:object):
    dictio={
        'id_perusahaan':company[0],
        'nama_perusahaan':company[1],
        'email_perusahaan':company[2],
        'deskripsi_perusahaan':company[3],
        'alamat_perusahaan' :company[4],
        'success' : True
    }
    return dictio


## TODO mikir tentang field yang akan ditampilkan di detail pekerjaan, detail lamaran dan detail ulasan