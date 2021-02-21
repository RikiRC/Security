import requests, json

rawSwaggerJson = requests.get('https://petstore.swagger.io/v2/swagger.json')
rawSwaggerJson = rawSwaggerJson.json()

paths = rawSwaggerJson['paths']
definitions = rawSwaggerJson['definitions']

baseUrl = 'https://' + rawSwaggerJson['host'] + rawSwaggerJson['basePath']

integerToReplace = 1
stringToReplace = 'test'

for path in paths:
    endpointUrl = baseUrl + path

    for method in paths[path]:
        contentType = None
        payload = {}

        for parameter in paths[path][method]['parameters']:
            schema = None

            if parameter['required'] == True:
                if parameter['in'] == 'path':
                    toReplace = '{'+parameter['name']+'}'
                    if parameter['type'] == 'integer':
                        endpointUrl = endpointUrl.replace(toReplace, str(integerToReplace))
                    elif parameter['type'] == 'string':
                        endpointUrl = endpointUrl.replace(toReplace, stringToReplace)
                elif parameter['in'] == 'query':
                    if parameter['type'] == 'integer':
                        payload[parameter['name']] = integerToReplace
                    if parameter['type'] == 'string':
                        payload[parameter['name']] = stringToReplace                    
                elif parameter['in'] == 'body':
                    try:
                        schema = definitions[parameter['schema']['$ref'].split('/')[-1]]
                    except:
                        try:
                            schema = definitions[parameter['schema']['items']['$ref'].split('/')[-1]]
                        except:
                            print('')
                    schemaProperties = schema['properties']
                    for schemaProperty in schemaProperties:
                        try:
                            if schemaProperties[schemaProperty]['type'] == 'integer':
                                payload[schemaProperty] = integerToReplace
                            elif schemaProperties[schemaProperty]['type'] == 'string':
                                payload[schemaProperty] = stringToReplace
                        except:
                            print('')
            else:
                print(parameter['name'] + ' is not required')

        if method == 'get':
             response = requests.get(endpointUrl)
             print(method + ' ' + endpointUrl + ' - ' + str(response.status_code))
        elif method == 'post':
            contentType = paths[path][method]['consumes'][0]
            headers = {'content-type': contentType}
            response = requests.post(endpointUrl, data=json.dumps(payload), headers=headers)
            print(method + ' ' + endpointUrl + ' - ' + str(response.status_code))
        elif method == 'put':
            contentType = paths[path][method]['consumes'][0]
            headers = {'content-type': contentType}
            response = requests.put(endpointUrl, data=json.dumps(payload), headers=headers)
            print(method + ' ' + endpointUrl + ' - ' + str(response.status_code))
        elif method == 'patch':
            contentType = paths[path][method]['consumes'][0]
            headers = {'content-type': contentType}
            response = requests.patch(endpointUrl, data=json.dumps(payload), headers=headers)
            print(method + ' ' + endpointUrl + ' - ' + str(response.status_code))
        elif method == 'delete':
            try:
                contentType = paths[path][method]['consumes'][0]
                headers = {'content-type': contentType}
            except:
                headers = None
            response = requests.delete(endpointUrl, data=json.dumps(payload), headers=headers)
            print(method + ' ' + endpointUrl + ' - ' + str(response.status_code))