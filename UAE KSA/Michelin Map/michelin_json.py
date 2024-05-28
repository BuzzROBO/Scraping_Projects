import csv
import requests

# Define the GraphQL endpoint URL
url = 'https://bff.viamichelin.com/graphql'

# Define headers for the request
headers = {
    'Content-Type': 'application/json',
}

# Define the payload template
payload_template = {
    "operationName": "getPOI",
    "query": """
    query getPOI($input: GetPOIFromIdInput!) {
        getPOIFromId(input: $input) {
            poi {
                ...POIFragment
                __typename
            }
            nearbyCitiesHierarchies {
                label
                value
            }
            cityHierarchy {
                ...HierarchySegmentFragment
            }
        }
    }

    fragment POIFragment on POI {
        ... on BasePOI {
            __typename
            id
            srcPoiId
            name
            address {
                zipCode
                city
                country {
                    code
                }
            }
            coordinates {
                lat
                lng
            }
            urlIdentifier
        }
        ... on AccommodationPOI {
            stars
            bookUrl
            priceCategory {
                currency
                count
            }
            startingPrice {
                amount
                currency
            }
            review {
                mention
                score
                count
            }
            images {
                ...ImageFragment
            }
            description
            subType
            facilities
            datasheetId
            isAvailable
            currency
            id
        }
        ... on AccommodationMichelinPOI {
            images {
                ...ImageFragment
            }
            bookUrl
            priceCategory {
                currency
                count
            }
            description
            review {
                mention
                score
                count
            }
            subType
            facilities
            isAvailable
            startingPrice {
                amount
                currency
            }
            currency
            id
        }
        ... on ParkingPOI {
            redirectUrl: bookUrl
            splittedAddress {
                firstLine
                secondLine
            }
            id
        }
        ... on RestaurantPOI {
            images {
                ...ImageFragment
            }
            bookUrl
            averagePrice {
                amount
                currency
            }
            review {
                mention
                score
                count
            }
            theForkUrl
            id
        }
        ... on RestaurantMichelinPOI {
            redirectUrl: bookUrl
            images {
                ...ImageFragment
            }
            distinctionStars
            bibGourmand
            priceCategory {
                currency
                count
            }
            priceRange {
                min
                max
                currency
            }
            meals {
                cuisineTypes
            }
            description
            facilities
            theForkUrl
            id
        }
        ... on TourismPOI {
            redirectUrl: bookUrl
            images {
                ...ImageFragment
            }
            distinctionStars
            description
            phone
            id
        }
        ... on ServiceGasStationPOI {
            fuels {
                lastUpdatedAt
                prices {
                    type
                    price {
                        amount
                        currency
                    }
                    priceCategory
                    filterOptionId
                }
            }
            id
        }
        ... on ServiceEVPOI {
            spots_count
            payment_methods {
                id
                name
            }
            connectors {
                type
                name
                count
                spots {
                    power
                    count
                }
            }
            id
        }
        ... on ServiceRestStopPOI {
            variant
            fullAddress
            id
        }
        __typename
    }

    fragment HierarchySegmentFragment on HierarchySegment {
        value
        label
        __typename
    }

    fragment ImageFragment on Image {
        w160
        w320
        w640
        w960
        w1280
        w1920
        __typename
    }
    """,
    "variables": {
        "input": {
            "id": None,
            "type": None,
            "poiFilters": []
        }
    }
}

def fetch_poi(id, poi_type):
    # Create a payload by copying the template and setting the POI id and type
    payload = payload_template.copy()
    payload["variables"]["input"]["id"] = id
    payload["variables"]["input"]["type"] = poi_type

    # Make the POST request to the GraphQL endpoint
    response = requests.post(url, json=payload, headers=headers)
    
    # Check if the response status code is OK
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Query failed with status code {response.status_code}: {response.text}")

def get_poi(id):
    try:
        # Attempt to fetch as a tourism POI
        response = fetch_poi(id, "TOURISM")
        
        # If POI does not exist, try fetching as accommodation POI
        if 'errors' in response and any('Poi of id' in error['message'] for error in response['errors']):
            response = fetch_poi(id, "ACCOMMODATION")
        
        return response
    except Exception as e:
        print(f"Error: {e}")
        return None

def write_to_csv_row(file, poi):
    writer = csv.writer(file)
    print("-"*100)
    print("Name:",poi['name'])
    print("Address:",poi['address']['city'],poi['address']['country']['code'])
    print("Zipcode:",poi['address']['zipCode'] if 'zipCode' in poi else 'None')
    print("Review Score:",poi['address']['zipCode'] if 'zipCode' in poi else 'None')
    print("Review Count:",poi['review']['count'] if 'review' in poi else 'None')
    print("Latitude:",poi['coordinates']['lat'])
    print("Longitude:",poi['coordinates']['lng'])
    print("-"*100)
    writer.writerow([
        poi['name'],
        f"{poi['address']['city']}, {poi['address']['country']['code']}",
        poi['address']['city'],
        poi['address']['zipCode'] if 'zipCode' in poi else 'None',
        poi['review']['score'] if 'review' in poi else 'None',
        poi['review']['count'] if 'review' in poi else 'None',
        poi['coordinates']['lat'],
        poi['coordinates']['lng']
    ])

# Open the CSV file in append mode
with open('poi_data.csv', mode='a', newline='', encoding='utf-8') as csvfile:
    # Write the header only if the file is empty
    csvfile.seek(0, 2)  # Move the cursor to the end of the file
    if csvfile.tell() == 0:  # Check if the file is empty
        writer = csv.writer(csvfile)
        writer.writerow(["Name", "Address", "City", "Zipcode", "Average Review Score", "Total Review Count", "Latitude", "Longitude"])

    # Main loop to read IDs from the CSV file and fetch POI data
    with open('ids.csv', newline='', encoding='utf-8') as idsfile:
        reader = csv.reader(idsfile)
        for row in reader:
            id_to_check = row[0]  # Assuming the ID is in the first column
            print(f"Fetching data for ID: {id_to_check}")
            poi = get_poi(id_to_check)
            try:
                if poi:
                    poi_data = poi['data']['getPOIFromId']['poi']
                    write_to_csv_row(csvfile, poi_data)
                    #print(poi)
            except Exception as e:
                print(e)
                pass
