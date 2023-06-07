import requests # подключаем библиотеку
a=[]
b=[]
l=[]
def ludia(o):
    if len(o)>11:
        l.append(o)
        return
    query = {
        "inn": o
    }
    # делаем запрос и получаем данные из него
    response = requests.post('https://dev.vdelo.pro/api/hackaton/kontur-focus/company/details', json=query)
    response = response.json()
    for i in range(len(response['message']['founders'])):
        if 'message' in response and 'founders' in response['message']:
            if('innfl' in response['message']['founders'][i-1]):
                a.append(response['message']['founders'][i-1]['innfl'])
            else:
                a.append(response['message']['founders'][i-1]['inn'])
def ludib(o):
    if len(o) > 11:
        l.append(o)
        return
    query = {   
        "inn": o
    }

    # делаем запрос и получаем данные из него
    response = requests.post('https://dev.vdelo.pro/api/hackaton/kontur-focus/company/details', json=query)
    response = response.json()
    for i in range(len(response['message']['founders'])):
        if 'message' in response and 'founders' in response['message']:
            if('innfl' in response['message']['founders'][i-1]):
                b.append(response['message']['founders'][i-1]['innfl'])
            else:
                b.append(response['message']['founders'][i-1]['inn'])
def rorp(u):
    query = {
        "inn": u
    }

    # делаем запрос и получаем данные из него
    response = requests.post('https://dev.vdelo.pro/api/hackaton/kontur-focus/person', json=query)

    response = response.json()
    return response
def svazkai(u):
    if len(u)<12:
        l.append(u)
        return
    query = {
        "inn": u
    }

    # делаем запрос и получаем данные из него
    response = requests.post('https://dev.vdelo.pro/api/hackaton/kontur-focus/person', json=query)

    response = response.json()
    return response
def aaaa(j,k):
    
    da=False
    # Объект запроса
    query = {
        "inn": j
    }

    # делаем запрос и получаем данные из него
    response = requests.post('https://dev.vdelo.pro/api/hackaton/kontur-focus/company/details', json=query)
    response = response.json() 
    for i in range(len(response['message']['founders'])):
        a.append(response['message']['founders'][i-1]['innfl'])
    a.append(response['message']['directors'][0]['innfl'])
    query = {
        "inn": k
    }

    # делаем запрос и получаем данные из него
    response = requests.post('https://dev.vdelo.pro/api/hackaton/kontur-focus/company/details', json=query)
    response = response.json()
    for i in range(len(response['message']['founders'])):
        b.append(response['message']['founders'][i-1]['innfl'])
    if not response['message']['directors'][0]['innfl'] == response['message']['founders'][i-1]['innfl']:
        b.append(response['message']['directors'][0]['innfl'])
    for m in a:
        for n in b:
            if m==n:
                da=True
                break
        if da == True:
            break
        return da

if not aaaa('6623134596','6670318625'):
    c=[a,b]
    a=[]
    b=[]
    for chislo in c:
        for i in chislo:
            r=rorp(i)
            if r != None:
                for j in range(len(r['message']['data'])):
                    if chislo==c[0]:
                        if not r['message']['data'][j-1]['inn'] in a:
                            a.append(r['message']['data'][j-1]['inn'])
                    else:
                        if not r['message']['data'][j-1]['inn'] in b:
                            b.append(r['message']['data'][j-1]['inn'])
c=[a,b]
a=[]
b=[]
for q in c[0]:
    ludia(q)
for q in c[1]:
    ludib(q)
c=[a,b]
a=[]
b=[]
for chislo in c:
    for i in chislo:
        r=svazkai(i)
        print(i)
        if i=='6660003190' or i=='6671118019' or i=='6681003313':
            continue
        if r!= None:
            # print(r['message']['data'][j-1]['inn'])
            for j in range(len(r['message']['data'])):
                # print(r['message']['data'][j-1]['inn'])
                if chislo==c[0]:
                    a.append(r['message']['data'][j-1]['inn'])
                else:
                    b.append(r['message']['data'][j-1]['inn'])
print(a,b)