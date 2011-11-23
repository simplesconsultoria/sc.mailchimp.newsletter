from zope.formlib import form
from zope import schema, component
from zope.interface import implements
from zope.component import getMultiAdapter
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName

from plone.app.portlets.portlets import base
from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.cache import render_cachekey

from plone.memoize.instance import memoize
from plone.memoize.compress import xhtml_compress

from sc.mailchimp.newsletter import MessageFactory as _
from sc.mailchimp.newsletter import interfaces


def availableLists(context):
    conn = interfaces.IAccountConnector(context,context)
    lists = conn.getLists()
    if hasattr(context,'data'):
        context.data.availableLists = [lst for lst in context.data.availableLists if lst in [i['id'] for i in lists['data']]]
    return SimpleVocabulary([SimpleTerm(value=li['id'], title=li['name']) for li in lists['data']])

class IMChimpPortlet(IPortletDataProvider):
    """
    """
    portletname = schema.TextLine(
        title=_(u'Title'),
        description=_(u'Title of the portlet')
    )
    
    availableLists = schema.List(
        title=_(u'Available lists'),
        description=_(u'Select available lists to subscribe to.'),
        required=True,
        min_length=1,
        value_type=schema.Choice(source='sc.mailchimp.newsletter.availableLists')
    )

class Assignment(base.Assignment):
    """
    """
    implements(IMChimpPortlet, interfaces.IProperties)

    _all_lists = {}
    
    def __init__(self, portletname=u'', availableLists=[]):
        self.portletname = portletname
        self.availableLists = availableLists

    @property
    def title(self):
        return _(u"NewsLetter")
    
    def getAvailableList(self):
        return self.availableLists

class Renderer(base.Renderer):
    """
    """
    _template = ViewPageTemplateFile('templates/mailchimp.pt')
    
    @property
    def name(self):
        return self.data.name or _(u"Subscribe to newsletter")

    def render(self):
        return xhtml_compress(self._template())

class AddForm(base.AddForm):
    """Portlet add form"""
    form_fields = form.Fields(IMChimpPortlet)
    
    def update(self):
        super(AddForm, self).update()
    
    def create(self, data):
        return Assignment(**data)

class EditForm(base.EditForm):
    """Portlet edit form"""
    def __call__(self):
        return super(EditForm, self).__call__()
    form_fields = form.Fields(IMChimpPortlet)
