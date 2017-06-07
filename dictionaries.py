from collections import namedtuple
from ctypes import byref, create_unicode_buffer, windll
from ctypes.wintypes import DWORD
from itertools import count

UID_BUFFER_SIZE = 39
PROPERTY_BUFFER_SIZE = 256
ERROR_MORE_DATA = 234
ERROR_INVALID_PARAMETER = 87
ERROR_SUCCESS = 0
ERROR_NO_MORE_ITEMS = 259
ERROR_UNKNOWN_PRODUCT = 1605

PRODUCT_PROPERTIES = [u'Language',
                      u'ProductName',
                      u'PackageCode',
                      u'Transforms',
                      u'AssignmentType',
                      u'PackageName',
                      u'InstalledProductName',
                      u'VersionString',
                      u'RegCompany',
                      u'RegOwner',
                      u'ProductID',
                      u'ProductIcon',
                      u'InstallLocation',
                      u'InstallSource',
                      u'InstallDate',
                      u'Publisher',
                      u'LocalPackage',
                      u'HelpLink',
                      u'HelpTelephone',
                      u'URLInfoAbout',
                      u'URLUpdateInfo', ]

Product = namedtuple('Product', PRODUCT_PROPERTIES)


def get_property_for_product(product, property, buf_size=PROPERTY_BUFFER_SIZE):
    property_buffer = create_unicode_buffer(buf_size)
    size = DWORD(buf_size)
    result = windll.msi.MsiGetProductInfoW(product, property, property_buffer, byref(size))
    if result == ERROR_MORE_DATA:
        return get_property_for_product(product, property, 2 * buf_size)
    elif result == ERROR_SUCCESS:
        return property_buffer.value
    else:
        return None


def populate_product(uid):
    properties = []
    for property in PRODUCT_PROPERTIES:
        properties.append(get_property_for_product(uid, property))
    return Product(*properties)


def get_installed_products_uids():
    products = []
    for i in count(0):
        uid_buffer = create_unicode_buffer(UID_BUFFER_SIZE)
        result = windll.msi.MsiEnumProductsW(i, uid_buffer)
        if result == ERROR_NO_MORE_ITEMS:
            break
        products.append(uid_buffer.value)
    return products


def get_installed_products():
    products = []
    for puid in get_installed_products_uids():
        products.append(populate_product(puid))
    return products


def is_product_installed_uid(uid):
    buf_size = 256
    uid_buffer = create_unicode_buffer(uid)
    property = u'VersionString'
    property_buffer = create_unicode_buffer(buf_size)
    size = DWORD(buf_size)
    result = windll.msi.MsiGetProductInfoW(uid_buffer, property, property_buffer, byref(size))
    if result == ERROR_UNKNOWN_PRODUCT:
        return False
    else:
        return True


apps = get_installed_products()
for app in apps:
    print app.ProductName


def google_dict():
    gd = ['google', 'search for', 'search', 'look for', 'look', 'knowledge']
    return gd
