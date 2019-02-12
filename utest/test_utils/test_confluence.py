import unittest
import mock
from utest.helper import (write_json, read_json, remove_file)
from utils.confluence import *

class TestFtpLogMove(unittest.TestCase):
    maxDiff = None

    def test_get_space_title(self):
        # https://confluence.eng.vmware.com/display/CERTSH/Bugzilla+PR+Template
        # https://confluence.eng.vmware.com/pages/viewpage.action?spaceKey=CERTSH&title=Cert+Review+Case+Study
        links_info = (
            ('https://confluence.eng.vmware.com/display/CERTSH/Bugzilla+PR+Template', 'CERTSH', 'Bugzilla PR Template'),
            ('https://confluence.eng.vmware.com/pages/viewpage.action?spaceKey=CERTSH&title=Cert+Review+Case+Study', 'CERTSH', 'Cert Review Case Study'),
        )

        for link_info in links_info:
            link, space, title = link_info
            self.assertEqual(get_space_title(link), (space, title))
