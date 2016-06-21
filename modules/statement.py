# encoding: utf-8

from response import Response

class Statement(object):
    """ Represents a single thing that the bot says.
    """
    def __init__(self, body, id=None, image=None, responses=[]):
        if not isinstance(responses, list):
            raise ValueError("The statement should come with a LIST of possible user responses.")

        self.id = id
        self.body = body
        self.responses = []
        self.image = image

        for response in responses:
            if "next_statement" not in response:
                response["next_statement"] = None

            r = Response(response["user_inputs"], response["next_statement"])
            self.responses.append(r)

        self.is_last = len(self.responses) == 0

    def __repr__(self):
        return u"<Statement: '%s'>" % self.body
        

    def _validate(self, surveybot):
        """ Make sure that every response links to valid statements
        """
        for response in self.responses:
            response._validate(surveybot, self)

    def in_tree(self):
        """ Is this statement part of the tree?
            A statement can also be some kind of error message 
        """
        return not self.id == None

    def interpret(self, user_input):
        """ Look for a matching response to the user input
        """
        for response in self.responses:
            matching_response = response.match(user_input)
            if matching_response:
                return matching_response


        return Statement("Sorry I didn't understand")