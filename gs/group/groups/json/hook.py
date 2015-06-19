# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2015 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
############################################################################
from __future__ import absolute_import, print_function, unicode_literals
from collections import OrderedDict
from json import dumps as to_json
from logging import getLogger
log = getLogger('gs.group.groups.json.hook')
from zope.cachedescriptors.property import Lazy
#from zope.component import createObject, queryMultiAdapter
from zope.formlib import form
from gs.content.form.api.json import SiteEndpoint
from gs.auth.token import log_auth_error
from .interfaces import IGetGroups
from gs.groups.allgroups import AllGroupsOnSite
from gs.group.privacy.interfaces import IGSGroupVisibility
from gs.group.type.set.interfaces import IUnsetType
from Products.GSGroup.interfaces import IGSMailingListInfo


class NoList(AttributeError):
    'There was no such list'


class GroupsHook(SiteEndpoint):
    '''The page that gets a list of the groups on the site'''
    label = 'Get the groups on the site'
    form_fields = form.Fields(IGetGroups, render_context=False)

    @form.action(label='Get', name='get', prefix='',
                 failure='handle_get_failure')
    def handle_get_groups(self, action, data):
        '''The form action for the *Get groups* page.

:param action: The button that was clicked.
:param dict data: The form data.'''
        retval = to_json(self.groups)
        return retval

    def handle_get_failure(self, action, data, errors):
        log_auth_error(self.context, self.request, errors)
        retval = self.build_error_response(action, data, errors)
        return retval

    @staticmethod
    def group_to_dict(groupInfo):
        groupUnset = IUnsetType(groupInfo.groupObj)
        groupVisiblity = IGSGroupVisibility(groupInfo)
        try:
            l = IGSMailingListInfo(groupInfo.groupObj)
        except AttributeError as ae:
            raise NoList(ae)

        retval = OrderedDict((
            ('id', groupInfo.id),
            ('name', groupInfo.name),
            ('url', groupInfo.url),
            ('email', l.get_property('mailto')),
            ('type', groupUnset.name),
            ('privacy', groupVisiblity.visibility), ))
        return retval

    @Lazy
    def groups(self):
        '''All the members of the GroupServer instance.'''
        retval = []
        for groupInfo in AllGroupsOnSite(self.context):
            try:
                r = self.group_to_dict(groupInfo)
            except NoList:
                continue
            retval.append(r)
        return retval
