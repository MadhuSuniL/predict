import json , pickle
from sklearn.ensemble import RandomForestClassifier

def indian_currency_format(ruppes):
    final_ruppes = ""
    count = 0
    if ruppes < 1000:
        return str(ruppes)
    elif ruppes > 999 and ruppes < 9999:
        for i in str(ruppes):
            if count == 1:
                final_ruppes+=","+i
            else:
                final_ruppes+=i
            count += 1
        return final_ruppes
    elif ruppes > 9999 and ruppes < 99999:
        for i in str(ruppes):
            if count == 2:
                final_ruppes+=","+i
            else:
                final_ruppes+=i
            count += 1
        return final_ruppes
    else:
        for i in str(ruppes):
            if count == 1 or count == 3:
                final_ruppes+=","+i
            else:
                final_ruppes+=i
            count += 1
        return final_ruppes
    
    
    
def make_inputs(request):
    inputs = []

    name = request.data['name']
    ram = request.data['ram']
    rom = request.data['rom']
    size = request.data['size']
    dis_type = request.data['type']
    fcam = request.data['fcam']
    bcam = request.data['bcam']
    battery = request.data['battery']
    processor = request.data['proc']
    
    with open('data files/inputs.json') as fp:
        data = json.load(fp)
    
    data['roms'] = int(rom)    
    data['rams'] = int(ram)
    data['screen_sizes'] = float(size)   
    data['front_camera'] = int(fcam)    
    data['back_camera'] = int(bcam)    
    data['battary'] = int(battery)
    data[name] = 1
    data[dis_type] = 1
    data[processor] = 1   
    for val in data.values():
        inputs.append(val)    
    return inputs
    
    
    
    
    
def predict_price_value(inputs):
    
    with open('model/model','rb') as fp:
        model = pickle.load(fp)
        price = model.predict([inputs])[0]
        return price