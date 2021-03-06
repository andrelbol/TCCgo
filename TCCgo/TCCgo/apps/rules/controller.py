import json

from django.db import models
from django.db.models import Q

from .models import (
    Rule, RuleType
)

class RuleController(object):

    def __init__(self):
        pass

    def create(self, pattern, warning, name, scope, type, user):
        """ Create a rule and save it to the database """
        rule = self.get(name=name)
        if(rule is None): # Rule name doesn't exists in the database
            new_rule = Rule(pattern=pattern, warning=warning, name=name, scope=scope, user=user)
            new_rule.rule_type = RuleType.objects.get(type=type)
            new_rule.save()
            print("Regra " + name + " criada.")
            return new_rule;
        else: # Name already exists
            print("Esse nome de regra já existe no sistema.")
            return None


    def delete( self, user, id=None, name=None):
        """ Given a rule name or id, delete it from the database """
        rule = self.get(id=id, name=name)
        if(rule is not None):
            if(user == rule.user):
                rule.delete()
                print("Regra " + name + "deletada.\n")
                return True
            else:
                print("Um usuário não pode deletar a regra de outro")
                return 501
        else:
            print("A regra digitada não existe.\n")
            return True

    def update(self, user, old_name, new_name, new_pattern, new_warning, new_scope, new_type):
        """ Given rule name and new fields, update the rule """
        # Testing if the new name already exists in the database and it's not the same
        test_rule = self.get(name=new_name)
        if(test_rule is not None and old_name != new_name):
            print("O novo nome já existe no sistema")
            return 500

        # Updating rule
        rule = self.get(name=old_name)

        if(rule is not None):
            if(user == rule.user): # Current user owns the rule
                setattr(rule, 'name', new_name)
                setattr(rule, 'pattern', new_pattern)
                setattr(rule, 'warning', new_warning)
                setattr(rule, 'scope', new_scope)
                setattr(rule, 'rule_type', RuleType.objects.get(type=new_type))
                rule.save()
                print("Regra " + old_name + "atualizada.")
                return True
            else:
                print("Um usuário só pode atualizar suas prórpias regras")
                return 501
        else:
            print("A regra a ser atualizada não existe.\n")
            return False

    def get(self, id=None, name=None):
        """ Given a rule name or id, return it if exists """
        try:
            if(id is not None):
                rule = Rule.objects.get(id=id)
            elif(name is not None):
                rule = Rule.objects.get(name=name)
            else:
                print("Nenhum parâmentro foi passado para essa função.")
                rule = None
            return rule
        except Rule.DoesNotExist:
            print("O nome ou id de regra não existe.\n")
            return None

    def get_all(self, user):
        """ Return all Rules in the database linked to an especific user """
        all_rules = Rule.objects.all()
        all_rules = Rule.objects.all().filter(Q(user=user) | Q(scope='PU'))
        return all_rules

    def create_with_request(self, request):
        """ Given a request, create a rule with the data in it """
        data = json.loads(request.body.decode('utf-8'))
        name = data['rule_name']
        pattern = data['rule_pattern']
        warning = data['rule_warning']
        rule_type = data['rule_type']
        scope = data['rule_scope']
        user = request.user
        return self.create(pattern, warning, name, scope, rule_type, user)

    def delete_with_request(self, request):
        """ Given a request, delete the rule inside it """
        data = json.loads(request.body.decode("utf-8"))
        name = data['rule_name']
        user = request.user
        return self.delete(user, name=name)

    def filter_with_request(self, request):
        """ Given a request with a search text, filter rules by it"""
        filter_json = json.loads(request.body.decode('utf-8'))
        filter = filter_json['search_text']
        rules = Rule.objects.filter(Q(name__icontains=filter) | Q(pattern__icontains=filter))
        return rules

    def update_with_request(self, request):
        """ Given a request with new data to rule, update the rule with the new values """
        print("Corpo do json: " + request.body.decode('utf-8'))
        update_json = json.loads(request.body.decode('utf-8'))
        current_user = request.user
        old_name = update_json['old_name']
        new_name = update_json['new_name']
        new_pattern = update_json['new_pattern']
        new_warning = update_json['new_warning']
        new_scope = update_json['new_scope']
        new_type = update_json['new_type']
        return self.update(current_user, old_name, new_name, new_pattern, new_warning, new_scope, new_type)



class RuleTypeController(object):
    def create(self, type):
        """ Create a ruleType and save it to the database """
        new_rule_type = RuleType(type=type)
        new_rule_type.save()
        return new_rule_type

    def delete(self, id):
        """ Delete a rule type with the given id """
        rule_type = self.get(id=id)
        if(rule_type is not None):
            rule_type.delete()
            print("Tipo de regra " + type + " deletado.\n")
            return True
        else:
            print("O tipo de regra digitado não existe.\n")
            return False

    def get(self, id):
        """ Return a rule type with the given id """
        try:
            rule_type = RuleType.objects.get(id=id)
            return rule_type
        except RuleType.DoesNotExists:
            print("O tipo de regra digitado não existe.\n")
            return None

    def get_all(self):
        """ Return all rule types in the database """
        all_types = RuleType.objects.all()
        return all_types
