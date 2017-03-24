import requests
def convert(url,c):
    r = requests.get(url)
    result=(c*float(r.json()['rate']));
    print("the converted currency is %f "%result);
    return (str(result));
    
if __name__=="__main__":
    a = raw_input('Enter currency to convert from?');
    a = a.upper();
    b = raw_input('Enter currency to convert to?');
    b = b.upper();
    c = float(raw_input('Enter value to convert?'));
    url=(('https://currency-api.appspot.com/api/%s/%s.json')%(a,b));
    print("url where i query from %s"%str(url));
    convert(url,c);
    
    
    
