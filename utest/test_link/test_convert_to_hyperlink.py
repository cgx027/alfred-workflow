import unittest
import mock
import json
# from utest.helper import (write_json, read_json, remove_file)
from link.convert_to_hyperlink import run

class TestConvert(unittest.TestCase):
    maxDiff = None

    def test_run(self):
        # data in (link_input, result_type, link_output, link_text)
        test_data = [ 
            (
                "https://bugzilla.eng.vmware.com/show_bug.cgi?id=2231863#c11",
                "hyperlink",
                "https://bugzilla.eng.vmware.com/show_bug.cgi?id=2231863#c11",
                "PR 2231863#c11"
            ),
            (
                "https://bugzilla.eng.vmware.com/show_bug.cgi?id=2231863",
                "hyperlink",
                "https://bugzilla.eng.vmware.com/show_bug.cgi?id=2231863",
                "PR 2231863"
            ),
            (
                "https://confluence.eng.vmware.com/display/CERTSH/Bugzilla+PR+Template",
                "hyperlink",
                "https://confluence.eng.vmware.com/display/CERTSH/Bugzilla+PR+Template",
                "Bugzilla PR Template"
            ),
            (
                "https://confluence.eng.vmware.com/pages/viewpage.action?spaceKey=CERTSH&title=Cert+Review+Case+Study",
                "hyperlink",
                "https://confluence.eng.vmware.com/pages/viewpage.action?spaceKey=CERTSH&title=Cert+Review+Case+Study",
                "Cert Review Case Study"
            ),
            (
                "https://confluence.eng.vmware.com/pages/viewpage.action?spaceKey=CERTSH",
                "hyperlink",
                "https://confluence.eng.vmware.com/pages/viewpage.action?spaceKey=CERTSH",
                "CERTSH"
            ),
            (
                "http://prme-vsanhol-observer-10.eng.vmware.com/vsanhol-nfs-vm/vsancert_logs/INT/all-flash/6_7_0/8169922/00050223/2018-07-03_22-15-35/VMWB-INT-4-VSANI-OCERT_1588451586290937714/testdata.json",
                "hyperlink",
                "http://prme-vsanhol-observer-10.eng.vmware.com/vsanhol-nfs-vm/vsancert_logs/INT/all-flash/6_7_0/8169922/00050223/2018-07-03_22-15-35/VMWB-INT-4-VSANI-OCERT_1588451586290937714/testdata.json",
                "testdata.json"
            ),
            (
                "https://wiki.eng.vmware.com/VSANCertification",
                "hyperlink",
                "https://wiki.eng.vmware.com/VSANCertification",
                "VSANCertification"
            ),
            (
                "https://wiki.eng.vmware.com/VSANCertification/VSANAnalytics/TestInfo",
                "hyperlink",
                "https://wiki.eng.vmware.com/VSANCertification/VSANAnalytics/TestInfo",
                "TestInfo"
            ),
            (
                "google.com google",
                "hyperlink",
                "google.com",
                "google"
            ),
            (
                "[wiki text]",
                "text",
                "[wiki text]",
                None
            ),
        ]

        for data in test_data:
            result_type, link, link_text = run(data[0])
            self.assertEqual((result_type, link, link_text), (data[1], data[2], data[3]))