# encoding: utf-8
import json
from statement import Statement
from response import Response
import os

class SurveyBot(object):
    def __init__(self, statement_tree_source, image_folder=""):
        """ statement_tree_source is the decision tree by which the bot will act
        """

        with open(statement_tree_source) as json_file:
            self.statements = []
            for item in json.load(json_file):
                if "image" not in item:
                    image = None
                else:
                    image = os.getcwd() + "/" + image_folder + item["image"]

                statement = Statement(item["body"],
                    id=item["id"],
                    image=image,
                    responses=item["responses"])

                self.statements.append(statement)

        self._validate()


    def _validate(self):
        """ Make sure that all statements are valid (links to valid next statements etc)
            and images exist
        """
        for statement in self.statements:
            statement._validate(self)
            
            if statement.image:
                if not os.path.isfile(statement.image):
                    raise ValueError("Can't find image {}".format(statement.image))

    def _get_statement_by_id(self, statement_id):
        """ Get a statement by id
        """
        try:
            return [x for x in self.statements if x.id == statement_id][0]
        except IndexError:
            None
            

    def _get_statement_by_text(self, statement_body):
        """ Get the first statement that matches the body of the statement
        """
        try:
            return [x for x in self.statements if x.body == statement_body][0]
        except IndexError:
            return None
    
    def start_conversation(self, *args, **kwargs):
        self.say(self.statements[0], *args, **kwargs)
        


