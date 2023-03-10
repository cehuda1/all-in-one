from termcolor import colored
import requests
import warnings
from concurrent.futures import ThreadPoolExecutor, as_completed

warnings.filterwarnings("ignore")

list_file = input("Enter the name of the domain list (ex: listdomain.txt)\nDomain List: ")

session = requests.Session()
session.max_redirects = 3

result = []

def check_domain(domain):
    try:
        r = session.get('https://' + domain, verify=False)
        if r.status_code == 200:
            print(colored(f"https://{domain}", 'green'))
            return f"https://{domain}"
        else:
            try:
                r = session.get('http://' + domain)
                if r.status_code == 200:
                    print(colored(f"http://{domain}", 'green'))
                    return f"http://{domain}"
                else:
                    if r.status_code == 400:
                        print(colored(f"http://{domain}", 'red'))
                    elif r.status_code == 301 or r.status_code == 302:
                        if "location" in r.headers:
                            if r.headers["location"] == "https://internettepat.telkomsel.com/dns?":
                                print(colored(f"http://{domain}", 'red'))
                            else:
                                print(colored(f"http://{domain} redirect ", 'yellow'))
                    else:
                        print(colored(f"http://{domain}", 'red'))
            except Exception as e:
                  print(f"Error while checking {domain}, {e}")
    except Exception as e:
        pass

with open(list_file, 'r') as file:
    domains = file.read().splitlines()
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(check_domain, domain) for domain in domains]
        for future in as_completed(futures):
            result.append(future.result())

save_result = input("Do you want to save the result? [y/n] ")
if future.result() != None:
    result.append(future.result())
if save_result.lower() == "y":
    file_name = input("Enter output file name: ")
    with open(file_name, 'w') as output_file:
        for domain in result:
            if domain != None:
                output_file.write(f"{domain}\n")
    print(f"File {file_name} saved.")
else:
    print("Result not saved.")
