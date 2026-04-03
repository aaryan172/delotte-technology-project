import json

def convertFromFormat1(jsonObject):
    try:
        locationParts = jsonObject["location"].split("/")
        if len(locationParts) != 5:
            raise ValueError(f"Location must have exactly 5 parts: {jsonObject['location']}")
        
        result = {
            'deviceID': jsonObject['deviceID'],
            'deviceType': jsonObject['deviceType'],
            'timestamp': jsonObject['timestamp'],
            'location': {
                'country': locationParts[0],
                'city': locationParts[1],
                'area': locationParts[2],
                'factory': locationParts[3],
                'section': locationParts[4]
            },
            'data': {
                'status': jsonObject['operationStatus'],
                'temperature': jsonObject['temp']
            }
        }
        return result
    except (KeyError, ValueError, IndexError) as e:
        print(f"Error processing object: {e}")
        return None

def main():
    # Load data-1.json (single object)
    with open('data-1.json', 'r') as f:
        data1 = json.load(f)
        converted1 = convertFromFormat1(data1)
    
    # Load data-2.json (list)
    with open('data-2.json', 'r') as f:
        data2_list = json.load(f)
        converted_list = [convertFromFormat1(item) for item in data2_list if convertFromFormat1(item) is not None]
    
    # Write to data-result.json
    with open('data-result.json', 'w') as f:
        json.dump(converted_list, f, indent=2)
    
    print("Conversion completed successfully. Check data-result.json")
    print(f"Converted data-1: {json.dumps(converted1, indent=2) if converted1 else 'Failed'}")

if __name__ == "__main__":
    main()

