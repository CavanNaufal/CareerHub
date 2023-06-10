####models.py
class Parse:
    def __init__(self,success:bool,arr,msg):
        self.success = success
        self.payload = arr
        self.message = msg

def listify(jobList:list):
    res = []
    for item in jobList:
        item_dict = {
            'id_pekerjaan': item[0],
            'posisi': item[1],
            'gaji': item[2],
            'nama_perusahaan': item[3],
            'nama_kategori': item[4]
        }
        res.append(item_dict)
    ret = Parse(True,res,"OK")
    return ret

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
            'tanggal_lamaran': item[5]
        }
        res.append(item_dict)
    ret = Parse(True,res,"OK")
    return ret

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