import requests


def respon():
    url = "https://random-user.p.rapidapi.com/getuser"

    headers = {
        'x-rapidapi-host': "random-user.p.rapidapi.com",
        'x-rapidapi-key': "d6f5c401c9msh7f27cfe69d5f1f9p120948jsn2090fc891893"
    }

    response = requests.request("GET", url, headers=headers)

    # return response.json()['results'][0]['name']['title'] #ism qo'shimchasini qaytaradi
    # return response.json()['results'][0]['gender'] #jinsini qaytaradi
    return response.json()['results'][0]  # results ni qaytaradi
    # return response.json()['results'][0]['name']['first'] #ismini qaytaradi
    # return response.json()['results'][0]['name']['last'] #familiyasini qaytaradi
    # return response.json()['results'][0]['location']['street']['number'] #uy raqamini qaytaradi
    # return response.json()['results'][0]['location']['street']['name'] #ko'cha nomini qaytaradi
    # return response.json()['results'][0]['location'].keys() #shahar nomini qaytaradi
    # return response.json()['results'][0]['state'] #viloyat nomini qaytaradi
    # return response.json()['results'][0]['country'] #davlat nomini qaytaradi
    # return response.json()['results'][0]['postcode'] #post code raqamini qaytaradi
    # return response.json()['results'][0]['emial'] #emailini qaytaradi
    # return response.json()['results'][0]['picture']['large'] #profile rasmini qaytaradi
    # return response.json()['results'][0]['nat'] #millatini qaytaradi


if __name__ == "__main__":
    print(respon())
