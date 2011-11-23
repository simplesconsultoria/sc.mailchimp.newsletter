.. contents:: Table of Contents
   :depth: 2

sc.mailchimp.newsletter
****************************************

Overview
--------

**sc.mailchimp.newsletter**  is a package integration MailChimp to Plone.

This package installs MailChimp functionalities to integration in an Plone site

Requirements
------------

    - Plone 4.0.x (http://plone.org/products/plone)
    - Plone 3.3.x (http://plone.org/products/plone)


Installation
------------
    
To enable this product,on a buildout based installation:

    1. Edit your buildout.cfg and add ``sc.mailchimp.newsletter``
       to the list of eggs to install ::

        [buildout]
        ...
        eggs = 
            sc.mailchimp.newsletter

* Not is necessary tell the plone.recipe.zope2instance recipe to install a ZCML slug.

After updating the configuration you need to run the ''bin/buildout'',
which will take care of updating your system.

Go to the 'Site Setup' page in the Plone interface and click on the
'Add/Remove Products' link.

Choose the product (check its checkbox) and click the 'Install' button.

Uninstall -- This can be done from the same management screen, but only
if you installed it from the quick installer.

Note: You may have to empty your browser cache and save your resource registries
in order to see the effects of the product installation.

Contributing
--------------

    Code repository and isssue tracker can be found at 
    `BitBucket <https://bitbucket.org/simplesconsultoria/sc.mailchimp.newsletter>`_

Sponsoring
----------

Development of this product was sponsored by :
    
    * `Simples Consultoria <http://www.simplesconsultoria.com.br/>`_.
    
Credits
-------
    
    * Cleber Santos (cleber at simplesconsultoria dot com dot br) - Idea and 
      implementation.
