import requests

url = 'https://bff.viamichelin.com/graphql'
headers = {
    'Content-Type': 'application/json',
}
payload = {
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
            "id": "e7f67e0a",
            "type": "ACCOMMODATION",
            "poiFilters": []
        }
    }
}

response = requests.post(url, json=payload, headers=headers)
print(response.json())
