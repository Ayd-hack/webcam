#!/usr/bin/python3

print("""
     <<<<<<<(WEBCAM-IP)>>>>>>>>>>
     |   888    888888888888888 |
     |   888    888888888888888 |
     |   888    888         888 |
     |   888    888         888 |
     |   888    888888888888888 |
     |   888    888888888888888 |
     |   888    888             |
     |   888    888             |
     |   888    888             |
     |   888    888             |
     |   888    888             |
     ----------------------------
     |                          |
     |   1 = Canada             |
     |   2 = France             |
     |   3 = German             |
     |   4 = Italy              |
     |   5 = Korea              |
     |   6 = Spain              |
     |   7 = Sweden             |
     |   8 = Taiwan             |
     |   9 = United Kingdom     |
     |   10 = United States     |
     ----------------------------
""")


select = input("Select your Number = ")

if select == "1":
    print("""
    167.114.9.81:8087          Montréal                 Canada
    99.247.154.61:80            Brampton                Canada
    74.56.182.180:8080        Montréal                 Canada
    """)

if select == "2":
    print("""
    81.56.198.164:8080    N/A                      France
    82.125.238.29:8080    Louchats                 France
    92.171.187.77:8083    Montluçon                France
    """)

if select == "3":
    print("""
    137.193.65.97:8080    Munich                   Germany
    188.193.167.206:8080  Weiden                   Germany
    188.194.97.147:8080   Ingolstadt               Germany
    79.239.36.62:8080     Oberhaching              Germany
    79.242.102.171:8081   Lobau                    Germany
    80.153.10.199:80      Heidenheim An Der Brenz  Germany
    84.182.78.138:8080    Koblenz                  Germany
    87.122.124.244:8081   Mannheim                 Germany
    87.139.109.109:8080   Asslar                   Germany
    87.145.63.172:8080    Willich                  Germany
    """)

if select == "4":
    print("""
    109.115.248.35:8083   Naples                   Italy
    195.32.51.132:8080    Scalenghe                Italy
    """)

if select == "5":
    print("""
    112.166.253.159:8080  N/A                      Korea, Republic of 
    115.22.130.117:5000   N/A                      Korea, Republic of
    14.56.232.149:8080    N/A                      Korea, Republic of
    222.113.39.201:8888   N/A                      Korea, Republic of 
    61.75.20.23:8080      Seoul                    Korea, Republic of 
    """)

if select == "6":
    print("""
    46.253.32.80:80       Falgóns                  Spain
    83.49.90.179:8080     Melilla                  Spain
    89.33.188.100:84      Murcia                   Spain
    """)

if select == "7":
    print("""
    77.110.41.214:80      Löberöd                  Sweden
    78.72.42.48:8080      Fritsla                  Sweden
    78.73.196.84:80       Kumla                    Sweden
    88.129.63.117:81      Kungsängen               Sweden
    """)

if select == "8":
    print("""
    114.32.131.232:8080   Taipei                   Taiwan
    140.116.177.34:8080   Tainan                   Taiwan
    218.161.78.91:8080    Taipei                   Taiwan
    """)

if select == "9":
    print("""
    146.200.13.116:8080   Southport                United Kingdom
    188.39.237.186:8080   Newcastle Upon Tyne      United Kingdom
    51.148.163.13:8080    N/A                      United Kingdom
    81.129.154.54:8081    Hertford                 United Kingdom
    81.133.233.117:8080   London                   United Kingdom
    81.133.95.150:8080    Bracknell                United Kingdom
    """)

if select == "10":
    print("""
    100.15.39.239:8080    Gainesville              United States
    104.159.165.125:8080  Duluth                   United States
    108.178.242.2:8080    Neoga                    United States
    108.207.231.79:8080   Wichita                  United States
    12.87.20.234:9090     N/A                      United States
    137.118.188.107:8080  Hays                     United States
    206.198.246.90:8081   N/A                      United States
    47.205.178.156:8081   Parrish                  United States 
    50.195.152.70:8080    N/A                      United States
    63.153.85.46:8080     Shelby                   United States
    65.126.126.74:8080    Mendon                   United States
    69.116.187.210:8090   Brooklyn                 United States
    71.208.210.57:8090    Cape Coral               United States
    71.233.232.150:8080   Provincetown             United States
    73.156.111.21:8090    Cape Coral               United States
    73.23.221.86:9002     Fort Myers               United States
    74.92.28.69:80        Haverhill                United States
    75.187.227.105:8080   Norwalk                  United States
    96.66.143.131:9000    Lehigh Acres             United States
    96.66.143.132:9000    Lehigh Acres             United States
    96.73.217.26:88       Atlanta                  United States
    97.92.145.127:8080    Scottsbluff              United States
    98.249.97.110:7777    Santa Fe                 United States
    """)

