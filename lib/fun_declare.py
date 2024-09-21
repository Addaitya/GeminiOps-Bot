from google.generativeai.protos import FunctionDeclaration, Schema, Type

wiki_search_desc = FunctionDeclaration(
    name='wikipedia_search',
    description='Returns the search result in string format from the wikipedia website',
    parameters= Schema(
        type=Type.OBJECT,
        properties={
            'search_query': Schema(
                        type=Type.STRING, 
                        description='Contain search query to search on wikipedia website.'
                    )
        },
        required=['search_query']
    )
)

calculate_desc = FunctionDeclaration(
    name='calculate_expression',
    description='Returns the calculated number simple mathematical expression consisting of addition, subtraction, multiplication and dividsion operations. Using python for operation. Example input="5+6-3/3" output=2.66',
    parameters= Schema(
        type=Type.OBJECT,
        properties={
            'math_expression': Schema(
                type=Type.STRING,
                description='Takes simple mathematical expression as stringconsisting of addtion, subtraction, multiplication'
            )
        },
        required=['math_expression']
    )
)

currency_desc = FunctionDeclaration(
    name="get_exchange_rate",
    description="Get the exchange rate for currencies between countries",
    parameters= Schema(
        type=Type.OBJECT,
        properties={
            'currency_date': Schema(
                type=Type.STRING,
                description="A date that must always be in YYYY-MM-DD format or the value 'latest' if a time period is not specified"
            ),
            'currency_from': Schema(
                type=Type.STRING,
                description='The currency to convert from in ISO 4217 format'

            ),
            'currency_to': Schema(
                type=Type.STRING,
                description='The currency to convert to in ISO 4217 format'

            )
        },
        required=[ "currency_from", "currency_to",]
    )
)
