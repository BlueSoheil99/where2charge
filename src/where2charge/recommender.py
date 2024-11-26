__all__ = ['get_suggestions']


from logic import googleAPI_handler, analyzer, database



def get_suggestions(address: str) -> Dict:
    locations = googleAPI_handler.get_locations(address)
    data = database.get_data(locations)
    #todo: merge data with locations
    suggestions = analyzer.get_suggestions(locations)
    return suggestions  ## return JSON object containing suggestions