import getpass
import requests
from bs4 import BeautifulSoup
from prettytable import ALL
from prettytable import PrettyTable

password = getpass.getpass("Enter password: ")
if password == "11" or " ":
    nik = input("Enter employee IDs (separated by commas): ")
    nik_list = nik.split(',')
    data = []
    for n in nik_list:
        url = f"https://intranet.sat.co.id/hc/public/atasan/catatan/lang/id/nikKary/{n}"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        data_karyawan = soup.find_all(class_="dataKaryawan")
        if len(data_karyawan) < 1:
            data.append([n,"-","-","-","-","-"])
        else:
            for d in data_karyawan:
                nik = d.find(string="NIK :").find_next().get_text().strip()
                nama = d.find(string="Nama Karyawan :").find_next().get_text().strip()
                tanggal_masuk = d.find(string="Tanggal Masuk :").find_next().get_text().strip()
                jabatan = d.find(string="Jabatan :").find_next().get_text().strip()
                divisi = d.find(string="Divisi / Dept. :").find_next().get_text().strip()
                branch = d.find(string="HO / Branch :").find_next().get_text().strip()
                data.append([nik,nama,tanggal_masuk,jabatan,divisi,branch,"556677"])
    #file_name = input("Enter the output file name: ")
    x = PrettyTable()
    x.field_names = ["NIK", "Nama Karyawan", "Tanggal Masuk", "Jabatan", "Divisi", "Branch", "Password"]

    for row in data:
        x.add_row(row)

    #with open(file_name, "w") as f:
        #f.write(x.get_string(hrules=ALL))
    print(x)
        #print("Data saved to " + file_name)
        #print(x)
else:
    print("Incorrect password, please try again.")
