# encoding: utf-8
import json
from statement import Statement
from response import Response

class SurveyBot(object):
    def __init__(self, statement_tree_source):
        """ statement_tree_source is the decision tree by which the bot will act
        """
        self.history = []

        with open(statement_tree_source) as json_file:

            self.statements = []
            for item in json.load(json_file):
                statement = Statement(item["body"], responses=item["responses"])
                self.statements.append(statement)

        self._validate()


    def _validate(self):
        # Make sure that all statements are valid (links to valid next statements etc)
        for statement in self.statements:
            statement._validate(self)

    def start(self):
        self.say(self.statements[0])

    def say(self, statement):
        if not statement.is_last:
            user_input = raw_input(statement.body)
            resp = statement.interpret(user_input)
            if isinstance(resp, Statement):
                self.say(Statement)

            elif isinstance(resp, Response):
                if resp.next_statement:
                    self.say(self.statements[resp.next_statement])
        else:
            print statement.body