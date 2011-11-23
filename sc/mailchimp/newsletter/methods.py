from Products.CMFCore.utils import getToolByName
from zope.interface import Interface
from zope import component, interface
from sc.mailchimp.newsletter.interfaces import IAccountConnector 
from sc.mailchimp.newsletter import MessageFactory as _
from sc.mailchimp.api import MailChimp

from plone.memoize.instance import memoize

class Connector(object):
    """
    """
    interface.implements(IAccountConnector)
    component.adapts(Interface)
    
    # check apikey
    ApiIsValid = False

    def __init__(self, context):
        self.context = context
        self.props = getToolByName(self.context, 'portal_properties').sc_mailchimp_newsletters_properties
        self.ssl_enabled = self.props.ssl_enabled
        self.ApiKey = self.props.apikey
        self.debugmode = self.props.debugmode
        self.APIKeyAccess(self.ApiKey)

    @memoize
    def getAccountDetails(self):
        if self.ApiIsValid:
            return self.mailChimp(method='getAccountDetails')

    def getPing(self):
        return self.mailChimp(method='ping')

    @memoize
    def getLists(self):
        if self.ApiIsValid:
            try:
                return self.mailChimp(method='lists')
            except:
                pass
        return []

    @memoize
    def APIKeyAccess(self, apikey):
        self.mailChimp = MailChimp(apikey=self.ApiKey,ssl=self.ssl_enabled,debug_mode=self.debugmode)
        try:
            if self.getPing() == "Everything's Chimpy!":
                self.ApiIsValid = True
        except:
            self.isValid = False
