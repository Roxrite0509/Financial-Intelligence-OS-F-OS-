def route(question):
    if "rate" in question.lower():
        return "macro"
    return "bank"
