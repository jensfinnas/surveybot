# encoding: utf-8
import json
from statement import Statement
from response import Response

class SurveyBot(object):
    def __init__(self, statement_tree_source):
        """ statement_tree_source is the decision tree by which the bot will act
        """
        with open(statement_tree_source) as json_file:
            self.statements = []
            for item in json.load(json_file):
                statement = Statement(item["body"], id=item["id"], responses=item["responses"])
                self.statements.append(statement)

        self._validate()


    def _validate(self):
        """ Make sure that all statements are valid (links to valid next statements etc)
        """
        for statement in self.statements:
            statement._validate(self)

    def _get_statement(self, statement_id):
        try:
            return [x for x in self.statements if x.id == statement_id][0]
        except IndexError:
            raise ValueError("{} is not a valid statement_id".format(statement_id))
    
    def start(self):
        self.say(self.statements[0])

    def say(self, statement):
        print statement.body
        if not statement.is_last:
            user_input = raw_input()
            resp = statement.interpret(user_input)
            if isinstance(resp, Statement):
                self.say(resp)

            elif isinstance(resp, Response):
                if resp.next_statement:
                    self.say(self.statements[resp.next_statement])
