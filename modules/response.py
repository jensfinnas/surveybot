
class Response(object):
    """ Represents a possible respone to a bot statement
    """
    def __init__(self, user_inputs, next_statement):
        self.user_inputs = user_inputs
        self.next_statement = next_statement

    def _validate(self, surveybot, statement):
        if not isinstance(self.next_statement, int):
            raise ValueError("{} should have an integer value as next_statement".format(statement))

        # Make sure that next statement is valid
        if self.next_statement >= len(surveybot.statements):
            raise ValueError("next_statement {} for '{}' is out of range. There are only {} statements this bot.".format(self.next_statement, statement.body, len(surveybot.statements)))

    def match(self,user_input):
        """ Check if the user input matches any of the allowed inputs
        """
        lower_user_inputs = [x.lower() for x in self.user_inputs]
        if user_input.lower() in lower_user_inputs:
            return self