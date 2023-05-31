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

#def userProfile(response)

#def companyProfile(response)



# dictio = {
#                 'id_pekerjaan': jobDetails[0],
#                 'id_perusahaan': jobDetails[1],
#                 'id_kategori': jobDetails[2],
#                 'posisi': jobDetails[3],
#                 'deskripsi': jobDetails[4],
#                 'kualifikasi': jobDetails[5],
#                 'gaji': jobDetails[6]
#             }


## TODO mikir tentang field yang akan ditampilkan di detail pekerjaan, detail lamaran dan detail ulasan