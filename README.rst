========================
``gs.group.groups.json``
========================
---------------------------------
The list of groups in JSON format
---------------------------------

:Author: `Michael JasonSmith`_
:Contact: Michael JasonSmith <mpj17@onlinegroups.net>
:Date: 2015-06-12
:Organization: `GroupServer.org`_
:Copyright: This document is licensed under a
  `Creative Commons Attribution-Share Alike 4.0 International License`_
  by `OnlineGroups.net`_.

..  _Creative Commons Attribution-Share Alike 4.0 International License:
    http://creativecommons.org/licenses/by-sa/4.0/

This product provides a *webhook* to retrieve the list of groups
on a GroupServer_ site. The hook_ should be used with care.

Hook
====

The hook, ``gs-group-groups.json``, is in the site context. Like
all GroupServer hooks it takes a token as an argument [#auth]_
and the name of an action (it is actually a form button):

.. code-block:: console

   $ wget --post-data="token=thisIsAToken&get=Get" \
     http://groups.example.com/gs-group-groups.json

The token is normally listed in the ``etc/gsconfig.ini`` file.
The `return value`_ is a JSON object.

:Caution:
   The hook returns *all* groups, including the secret ones, and
   the *existence* of some groups may be controversial. That is
   why the **secret** group privacy level exists. Be very
   cautious about disclosing the list of groups unfiltered.

.. _return value:

JSON Return value
-----------------

A list of JSON objects is returned. Each object within the list
represents a group, and has the following fields set.


``id``:
  The unique identifier for the group.

``name``:
  The name of the group (the title).

``url``:
  The URL for the group.

``email``:
  The email address for the group,

``type``:
  The type of group.

``privacy``:
  The group privacy.

Resources
=========

- Code repository:
  https://github.com/groupserver/gs.group.groups.json
- Questions and comments to
  http://groupserver.org/groups/development
- Report bugs at https://redmine.iopen.net/projects/groupserver

.. [#auth] https://github.com/groupserver/gs.auth.token

.. _GroupServer: http://groupserver.org/
.. _GroupServer.org: http://groupserver.org/
.. _OnlineGroups.Net: https://onlinegroups.net
.. _Michael JasonSmith: http://groupserver.org/p/mpj17

..  LocalWords:  json webhook
