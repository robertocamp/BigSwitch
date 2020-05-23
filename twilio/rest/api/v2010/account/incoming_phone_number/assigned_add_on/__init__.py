# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page
from twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.assigned_add_on_extension import AssignedAddOnExtensionList


class AssignedAddOnList(ListResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, account_sid, resource_sid):
        """
        Initialize the AssignedAddOnList

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the Account that created the resource
        :param resource_sid: The SID of the Phone Number that installed this Add-on

        :returns: twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.AssignedAddOnList
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.AssignedAddOnList
        """
        super(AssignedAddOnList, self).__init__(version)

        # Path Solution
        self._solution = {'account_sid': account_sid, 'resource_sid': resource_sid, }
        self._uri = '/Accounts/{account_sid}/IncomingPhoneNumbers/{resource_sid}/AssignedAddOns.json'.format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams AssignedAddOnInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.AssignedAddOnInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists AssignedAddOnInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.AssignedAddOnInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of AssignedAddOnInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of AssignedAddOnInstance
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.AssignedAddOnPage
        """
        data = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(method='GET', uri=self._uri, params=data, )

        return AssignedAddOnPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of AssignedAddOnInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of AssignedAddOnInstance
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.AssignedAddOnPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return AssignedAddOnPage(self._version, response, self._solution)

    def create(self, installed_add_on_sid):
        """
        Create the AssignedAddOnInstance

        :param unicode installed_add_on_sid: The SID that identifies the Add-on installation

        :returns: The created AssignedAddOnInstance
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.AssignedAddOnInstance
        """
        data = values.of({'InstalledAddOnSid': installed_add_on_sid, })

        payload = self._version.create(method='POST', uri=self._uri, data=data, )

        return AssignedAddOnInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            resource_sid=self._solution['resource_sid'],
        )

    def get(self, sid):
        """
        Constructs a AssignedAddOnContext

        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.AssignedAddOnContext
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.AssignedAddOnContext
        """
        return AssignedAddOnContext(
            self._version,
            account_sid=self._solution['account_sid'],
            resource_sid=self._solution['resource_sid'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a AssignedAddOnContext

        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.AssignedAddOnContext
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.AssignedAddOnContext
        """
        return AssignedAddOnContext(
            self._version,
            account_sid=self._solution['account_sid'],
            resource_sid=self._solution['resource_sid'],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.AssignedAddOnList>'


class AssignedAddOnPage(Page):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, response, solution):
        """
        Initialize the AssignedAddOnPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param account_sid: The SID of the Account that created the resource
        :param resource_sid: The SID of the Phone Number that installed this Add-on

        :returns: twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.AssignedAddOnPage
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.AssignedAddOnPage
        """
        super(AssignedAddOnPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of AssignedAddOnInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.AssignedAddOnInstance
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.AssignedAddOnInstance
        """
        return AssignedAddOnInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            resource_sid=self._solution['resource_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.AssignedAddOnPage>'


class AssignedAddOnContext(InstanceContext):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, account_sid, resource_sid, sid):
        """
        Initialize the AssignedAddOnContext

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the Account that created the resource to fetch
        :param resource_sid: The SID of the Phone Number that installed this Add-on
        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.AssignedAddOnContext
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.AssignedAddOnContext
        """
        super(AssignedAddOnContext, self).__init__(version)

        # Path Solution
        self._solution = {'account_sid': account_sid, 'resource_sid': resource_sid, 'sid': sid, }
        self._uri = '/Accounts/{account_sid}/IncomingPhoneNumbers/{resource_sid}/AssignedAddOns/{sid}.json'.format(**self._solution)

        # Dependents
        self._extensions = None

    def fetch(self):
        """
        Fetch the AssignedAddOnInstance

        :returns: The fetched AssignedAddOnInstance
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.AssignedAddOnInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return AssignedAddOnInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            resource_sid=self._solution['resource_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the AssignedAddOnInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )

    @property
    def extensions(self):
        """
        Access the extensions

        :returns: twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.assigned_add_on_extension.AssignedAddOnExtensionList
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.assigned_add_on_extension.AssignedAddOnExtensionList
        """
        if self._extensions is None:
            self._extensions = AssignedAddOnExtensionList(
                self._version,
                account_sid=self._solution['account_sid'],
                resource_sid=self._solution['resource_sid'],
                assigned_add_on_sid=self._solution['sid'],
            )
        return self._extensions

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.AssignedAddOnContext {}>'.format(context)


class AssignedAddOnInstance(InstanceResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, payload, account_sid, resource_sid, sid=None):
        """
        Initialize the AssignedAddOnInstance

        :returns: twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.AssignedAddOnInstance
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.AssignedAddOnInstance
        """
        super(AssignedAddOnInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'resource_sid': payload.get('resource_sid'),
            'friendly_name': payload.get('friendly_name'),
            'description': payload.get('description'),
            'configuration': payload.get('configuration'),
            'unique_name': payload.get('unique_name'),
            'date_created': deserialize.rfc2822_datetime(payload.get('date_created')),
            'date_updated': deserialize.rfc2822_datetime(payload.get('date_updated')),
            'uri': payload.get('uri'),
            'subresource_uris': payload.get('subresource_uris'),
        }

        # Context
        self._context = None
        self._solution = {
            'account_sid': account_sid,
            'resource_sid': resource_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: AssignedAddOnContext for this AssignedAddOnInstance
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.AssignedAddOnContext
        """
        if self._context is None:
            self._context = AssignedAddOnContext(
                self._version,
                account_sid=self._solution['account_sid'],
                resource_sid=self._solution['resource_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: The unique string that identifies the resource
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account that created the resource
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def resource_sid(self):
        """
        :returns: The SID of the Phone Number that installed this Add-on
        :rtype: unicode
        """
        return self._properties['resource_sid']

    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the resource
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def description(self):
        """
        :returns: A short description of the Add-on functionality
        :rtype: unicode
        """
        return self._properties['description']

    @property
    def configuration(self):
        """
        :returns: A JSON string that represents the current configuration
        :rtype: dict
        """
        return self._properties['configuration']

    @property
    def unique_name(self):
        """
        :returns: An application-defined string that uniquely identifies the resource
        :rtype: unicode
        """
        return self._properties['unique_name']

    @property
    def date_created(self):
        """
        :returns: The RFC 2822 date and time in GMT that the resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The RFC 2822 date and time in GMT that the resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def uri(self):
        """
        :returns: The URI of the resource, relative to `https://api.twilio.com`
        :rtype: unicode
        """
        return self._properties['uri']

    @property
    def subresource_uris(self):
        """
        :returns: A list of related resources identified by their relative URIs
        :rtype: unicode
        """
        return self._properties['subresource_uris']

    def fetch(self):
        """
        Fetch the AssignedAddOnInstance

        :returns: The fetched AssignedAddOnInstance
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.AssignedAddOnInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the AssignedAddOnInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    @property
    def extensions(self):
        """
        Access the extensions

        :returns: twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.assigned_add_on_extension.AssignedAddOnExtensionList
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.assigned_add_on_extension.AssignedAddOnExtensionList
        """
        return self._proxy.extensions

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.AssignedAddOnInstance {}>'.format(context)
