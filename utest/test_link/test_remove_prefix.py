import unittest
import mock
import json
# from utest.helper import (write_json, read_json, remove_file)
from link.remove_prefix import run

class TestRemovePrefix(unittest.TestCase):
    maxDiff = None

    def test_run(self):
        # data in (link_input, link_output, link_text)
        test_data = [ 
            (
                "https://bugzilla.eng.vmware.com/show_bug.cgi?id=2231863#c11",
                "/show_bug.cgi"
            ),
            (
                "https://confluence.eng.vmware.com/display/CERTSH/Bugzilla+PR+Template",
                "/display/CERTSH/Bugzilla+PR+Template"
            ),
            (
                "https://confluence.eng.vmware.com/pages/viewpage.action?spaceKey=CERTSH&title=Cert+Review+Case+Study",
                "/pages/viewpage.action"
            ),
            (
                "http://prme-vsanhol-observer-10.eng.vmware.com/vsanhol-nfs-vm/vsancert_logs/INT/all-flash/6_7_0/8169922/00050223/2018-07-03_22-15-35/VMWB-INT-4-VSANI-OCERT_1588451586290937714/testdata.json",
                "/vsanhol-nfs-vm/vsancert_logs/INT/all-flash/6_7_0/8169922/00050223/2018-07-03_22-15-35/VMWB-INT-4-VSANI-OCERT_1588451586290937714/testdata.json"
            ),
            (
                "http://prme-vsanhol-observer-10.eng.vmware.com/vsanhol-nfs-vm/vsancert_logs/INT/all-flash/6_7_0/8169922/00050223/2018-07-03_22-15-35/VMWB-INT-4-VSANI-OCERT_1588451586290937714",
                "/vsanhol-nfs-vm/vsancert_logs/INT/all-flash/6_7_0/8169922/00050223/2018-07-03_22-15-35/VMWB-INT-4-VSANI-OCERT_1588451586290937714"
            ),
            (
                "https://wiki.eng.vmware.com/VSANCertification",
                "/VSANCertification"
            ),
            (
                "https://wiki.eng.vmware.com/VSANCertification/VSANAnalytics/TestInfo",
                "/VSANCertification/VSANAnalytics/TestInfo"
            ),
            (
                "google.com google",
                "google.com"
            ),
            (
                "[wiki text]",
                "[wiki"
            ),
        ]

        for data in test_data:
            path = run(data[0])
            expected_path = data[1]
            self.assertEqual(path, expected_path)