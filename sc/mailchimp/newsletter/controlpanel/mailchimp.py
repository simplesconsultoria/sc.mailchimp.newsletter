# -*- coding:utf-8 -*-
from zope.schema import Bool, Int, TextLine, Tuple, Choice
from zope.component import adapts
from zope.interface import Interface, implements

from Products.CMFPlone.interfaces import IPloneSiteRoot
from Products.CMFPlone.utils import getToolByName
from Products.CMFDefault.formlib.schema import ProxyFieldProperty, SchemaAdapterBase

from zope.formlib.form import FormFields
from plone.app.controlpanel.form import ControlPanelForm
from plone.fieldsets.fieldsets import FormFieldsets

from sc.mailchimp.newsletter import MessageFactory as _

from zope.app.pagetemplate import viewpagetemplatefile
from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile

class IProvidersSchema(Interface):
    """ General Configurations """ 

    apikey = TextLine(
        title=_(u'API Key'),
        description=_(u'help_apikeys',
            default=u"Enter your key from MailChimp API - Information in: https://us2.admin.mailchimp.com/account/api/",
        ),
        required=True,
    )
    
    ssl_enabled = Bool(
        title=_(u"Enable SSL"),
        description=_(u'help_sslenable',
            default=u"If True use https protocol else use http protocol",
        ),
        default=True,
        required=False
    )

    debugmode = Bool(
        title=_(u"Enable debug mode"),
        description=_(u'help_debugmode',
            default=u"If True use debug mode",
        ),
        default=False,
        required=False
    )
                          
class BaseControlPanelAdapter(SchemaAdapterBase):
    """ Base control panel adapter """
   
    def __init__(self, context):
        super(BaseControlPanelAdapter, self).__init__(context)
        portal_properties = getToolByName(context, 'portal_properties')
        self.context = portal_properties.sc_mailchimp_newsletters_properties

class MChimpControlPanelAdapter(BaseControlPanelAdapter):
    """ control panel adapter """
    adapts(IPloneSiteRoot)
    implements(IProvidersSchema)
    
    apikey = ProxyFieldProperty(IProvidersSchema['apikey'])
    ssl_enabled = ProxyFieldProperty(IProvidersSchema['ssl_enabled'])
    debugmode = ProxyFieldProperty(IProvidersSchema['debugmode'])

baseset = FormFieldsets(IProvidersSchema)
baseset.id = 'baseset'
baseset.label = _(u'MailChimp Configuration')


class ProvidersControlPanel(ControlPanelForm):
    """ """
    base_template = ControlPanelForm.template
    template = ZopeTwoPageTemplateFile('templates/cpanel.pt')

    form_fields = FormFieldsets(baseset)
    
    label = _('MailChimp settings')
    description = _('Configure settings for sc.mailchimp.newsletter.')
    form_name = _('MailChimp Configuration')
