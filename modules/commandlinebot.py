# encoding: utf-8

from surveybot import SurveyBot
from statement import Statement
from response import Response

class CommandlineBot(SurveyBot):
    """ A command line implentation of a Survey Bot.
    """
    def say(self, statement, *arg, **kwargs):
        print "#%s: %s" % (statement.id, statement.body) 
        if not statement.is_last:
            user_input = raw_input()
            resp = statement.interpret(user_input)

            if isinstance(resp, Statement):
                self.say(resp)

            elif isinstance(resp, Response):
                if resp.next_statement:
                    next_statement = self._get_statement_by_id(resp.next_statement)
                    self.say(next_statement)


