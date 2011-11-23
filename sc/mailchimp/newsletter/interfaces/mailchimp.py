# -*- coding: utf-8 -*-
from zope.interface import Interface
from plone.theme.interfaces import IDefaultPloneLayer
from zope import schema

from zope.i18nmessageid import MessageFactory
_ = MessageFactory('sc.mailchimp.newsletter')

class IMailChimpLayer(Interface):
    """
    """

class IAccountConnector(Interface):
    """
    """

    def __init__(self, context):
        """ 
        """

    def getAccountDetails(self):
        """
        """

    def getPing(self):
        """
        """

    def getLists(self):
        """
        """

    def APIKeyAccess(self, apikey):
        """
        """

class IProperties(Interface):
    """
    """
    
    def getAvailableList (self):
        """
        """
