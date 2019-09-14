import json


def convert_result_in_template_obj(result):
    result = json.loads(result)
    itinerarios = result['Itineraries']
    agents = result['Agents']
    data = []
    for itiner in itinerarios:
        for i in itiner['PricingOptions']:
            agente = 'Desconocido'
            imagen = 'http://via.placeholder.com/150x150/ccc/fff/thumb_cart_1.jpg'
            for agent in agents:
                print('i agentes %s' % i['Agents'][0])
                print('name %s' % agent['Id'])
                if i['Agents'][0] == agent['Id']:
                    print('agente es %s' % agent['Name'])
                    agente = agent['Name']
                    imagen = agent['ImageUrl']
                    break
            data.append({
                'precio': i['Price'],
                'url': i['DeeplinkUrl'],
                'agente': agente,
                'imagen': imagen
            })
    return data