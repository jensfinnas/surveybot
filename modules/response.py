
class Response(object):
    """ Represents a possible respone to a bot statement
    """
    def __init__(self, user_inputs, next_statement):
        self.user_inputs = user_inputs
        self.next_statement = next_statement

    def _validate(self, surveybot, statement):
        if not isinstance(self.next_statement, int):
            raise ValueError("{} should have an integer value as next_statement".format(statement))

        # Make sure that next statement is a valid statement id
        # Will throw en error if id is faulty
        _statement = surveybot._get_statement_by_id(self.next_statement)
        if not _statement:
            raise ValueError("{} is not a valid statement_id".format(self.next_statement))

    def match(self,user_input):
        """ Check if the user input matches any of the allowed inputs
        """
        lower_user_inputs = [x.lower() for x in self.user_inputs]
        if user_input.lower() in lower_user_inputs:
            return self